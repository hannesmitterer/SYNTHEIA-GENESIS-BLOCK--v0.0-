# SYNTHEIA v2.1-v2.5 Roll-out Deployment Guide

This document describes the deployment of the reputation module, blockchain snapshots, adaptive shield tuning, and automated reporting system.

## Overview

The roll-out package includes five major components:

1. **v2.1**: Reputation Module - Node weighting based on pH and mycelium metrics
2. **v2.2**: Beta Adjustment - Reputation-weighted parameter tuning
3. **v2.3**: Blockchain Snapshots - Daily consensus state anchoring
4. **v2.4**: Adaptive Shield Tuning - Dynamic frequency band adjustment
5. **v2.5**: 24-Hour Reports - Automated report generation with IPFS anchoring

## File Structure

```
vacuum_node/
├── __init__.py           # Module initialization
├── reputation.py         # Reputation tracking and weighting (v2.1)
├── distributor.py        # Beta adjustment with reputation (v2.2)
├── blockchain.py         # Blockchain integration
├── ipfs_anchor.py        # IPFS anchoring functionality
├── snapshot.py           # Snapshot collection and submission (v2.3)
├── shield_tuner.py       # Adaptive shield frequency tuning (v2.4)
└── report.py             # 24-hour report generator (v2.5)

k8s/
├── consensus-snapshot.yaml  # Daily snapshot CronJob
├── shield-tuner.yaml        # 6-hourly shield tuning CronJob
└── daily-report.yaml        # Daily report generation CronJob
```

## Prerequisites

### Python Dependencies
The modules require the following Python packages:
- `requests` - HTTP client for API calls
- `jinja2` (optional) - Template rendering for reports

Install with:
```bash
pip install requests jinja2
```

### Kubernetes Resources
Ensure the following exist in your cluster:
- ConfigMap `ghp-manifest` with key `rootHash`
- Service endpoints:
  - `blockchain:8545` - Blockchain RPC endpoint
  - `ipfs:5001` - IPFS API endpoint
  - `monitoring:9090` - Prometheus metrics endpoint

### File System Structure
The following directories should be available:
```
/etc/vacuum/
├── reputation.json          # Reputation data (will be created)
├── ghp-manifest.json        # Global Harmony Protocol manifest
└── shield_config.json       # Shield configuration (will be created)

/var/lib/vacuum/
├── telemetry_summary.json   # Telemetry aggregates
├── snapshots/               # Snapshot storage
└── reports/                 # Report output directory
```

## Deployment Steps

### 1. Prepare the Repository
Ensure all changes are committed and pushed:
```bash
git log --oneline -5
# Should show commits v2.1 through v2.5
```

### 2. Build Docker Image
Build and push the updated vacuum-node image:
```bash
cd /path/to/SYNTHEIA-GENESIS-BLOCK--v0.0-
docker build -t duckai/vacuum-node:latest .
docker push duckai/vacuum-node:latest
```

**Note**: You'll need to create a `Dockerfile` if one doesn't exist. Example:
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY vacuum_node/ /app/vacuum_node/
COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "-m", "vacuum_node"]
```

### 3. Create ConfigMap for Reputation (Optional)
If you want to manage reputation data via ConfigMap:
```bash
kubectl create configmap reputation \
  --from-literal=data='{}' \
  -n vacuum
```

### 4. Deploy CronJobs
Apply all Kubernetes manifests:
```bash
kubectl apply -f k8s/consensus-snapshot.yaml
kubectl apply -f k8s/shield-tuner.yaml
kubectl apply -f k8s/daily-report.yaml
```

Verify the CronJobs are created:
```bash
kubectl get cronjobs -n vacuum
```

Expected output:
```
NAME                  SCHEDULE        SUSPEND   ACTIVE   LAST SCHEDULE   AGE
consensus-snapshot    0 */24 * * *    False     0        <none>          1m
shield-tuner          0 */6 * * *     False     0        <none>          1m
daily-ghp-report      0 2 * * *       False     0        <none>          1m
```

### 5. Update Existing Deployment
If you have an existing `argilla-distributor` deployment, restart it to use the new reputation-weighted beta adjustment:
```bash
kubectl rollout restart deployment argilla-distributor -n vacuum
```

## Monitoring

### Check CronJob Execution
Monitor job executions:
```bash
# List recent jobs
kubectl get jobs -n vacuum

# Check job logs
kubectl logs -n vacuum job/consensus-snapshot-<timestamp>
kubectl logs -n vacuum job/shield-tuner-<timestamp>
kubectl logs -n vacuum job/daily-ghp-report-<timestamp>
```

### Verify Reputation Data
Check reputation file contents (if accessible):
```bash
kubectl exec -it <pod-name> -n vacuum -- cat /etc/vacuum/reputation.json
```

### Monitor Snapshots
Snapshots are stored in `/var/lib/vacuum/snapshots/` and submitted to the blockchain. Check blockchain transactions for type "snapshot".

### View Reports
Reports are saved to `/var/lib/vacuum/reports/ghp_report.md` and anchored to IPFS. The IPFS CID is printed in the job logs.

## Manual Testing

### Test Reputation Module
```bash
# Enter a pod
kubectl exec -it <pod-name> -n vacuum -- python3

# In Python REPL
from vacuum_node.reputation import update, weight
update("node1", 6.5, 0.87)
print(weight("node1"))
```

### Test Snapshot Generation
```bash
kubectl exec -it <pod-name> -n vacuum -- \
  python3 -m vacuum_node.snapshot
```

### Test Shield Tuner
```bash
kubectl exec -it <pod-name> -n vacuum -- \
  python3 -m vacuum_node.shield_tuner
```

### Test Report Generator
```bash
kubectl exec -it <pod-name> -n vacuum -- \
  python3 -m vacuum_node.report
```

## Rollback

If you need to rollback any component:

### Rollback Code Changes
```bash
# Rollback to before v2.1
git revert 61187a4  # v2.5
git revert 566931d  # v2.4
git revert 8089b35  # v2.3
git revert 7c99b61  # v2.1, v2.2
```

### Remove CronJobs
```bash
kubectl delete cronjob consensus-snapshot -n vacuum
kubectl delete cronjob shield-tuner -n vacuum
kubectl delete cronjob daily-ghp-report -n vacuum
```

## Troubleshooting

### CronJob Not Running
Check the schedule and ensure the CronJob is not suspended:
```bash
kubectl describe cronjob <name> -n vacuum
```

### Module Import Errors
Ensure the vacuum_node package is in the Python path:
```bash
export PYTHONPATH=/app:$PYTHONPATH
```

### File Permission Errors
Ensure the pod has write access to required directories:
```bash
kubectl exec -it <pod-name> -n vacuum -- ls -la /etc/vacuum
kubectl exec -it <pod-name> -n vacuum -- ls -la /var/lib/vacuum
```

### Network Connection Issues
Test connectivity to required services:
```bash
kubectl exec -it <pod-name> -n vacuum -- curl http://blockchain:8545
kubectl exec -it <pod-name> -n vacuum -- curl http://ipfs:5001
kubectl exec -it <pod-name> -n vacuum -- curl http://monitoring:9090
```

## Configuration

### Reputation Parameters
Edit `vacuum_node/reputation.py`:
- `WINDOW_DAYS`: How many days of history to keep (default: 7)
- `MIN_WEIGHT`: Minimum node weight (default: 0.1)
- `MAX_WEIGHT`: Maximum node weight (default: 1.0)

### Shield Tuning Thresholds
Edit `vacuum_node/shield_tuner.py`:
- Latency threshold: 150ms (line 43)
- Frequency range: 45-65 Hz (lines 45-46)

### CronJob Schedules
Edit the respective YAML files in `k8s/`:
- `consensus-snapshot.yaml`: Default "0 */24 * * *" (daily)
- `shield-tuner.yaml`: Default "0 */6 * * *" (every 6 hours)
- `daily-report.yaml`: Default "0 2 * * *" (daily at 02:00 UTC)

## Next Steps

1. **Monitor System Performance**: Watch Grafana dashboards for `ghp/reports` and `shield/metrics`
2. **Review Generated Reports**: Check `/var/lib/vacuum/reports/` for daily reports
3. **Verify Blockchain Anchoring**: Confirm snapshots appear in the blockchain
4. **Fine-tune Parameters**: Adjust reputation scoring and shield tuning thresholds based on observed behavior
5. **Scale Testing**: Test with increased load to validate performance improvements

## Support

For issues or questions:
- Check the logs: `kubectl logs -n vacuum <pod-name>`
- Review the commit history for implementation details
- Consult the Global Harmony Protocol documentation

---

**Version**: 2.5  
**Last Updated**: 2026-04-06  
**Components**: Reputation (v2.1), Beta Adjustment (v2.2), Snapshots (v2.3), Shield Tuning (v2.4), Reports (v2.5)
