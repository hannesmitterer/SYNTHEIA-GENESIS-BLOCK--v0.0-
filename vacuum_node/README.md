# SYNTHEIA Vacuum Node Module

**Version**: 2.5  
**Status**: Production Ready ✓

## Overview

The Vacuum Node module provides autonomous reputation tracking, blockchain integration, adaptive shield tuning, and automated reporting for the SYNTHEIA Genesis Block system.

## Features

### 🏆 Reputation Tracking (v2.1)
- Node performance monitoring based on pH and mycelium metrics
- 7-day rolling window for historical analysis
- Dynamic weight calculation (0.1 - 1.0)
- Persistent JSON storage

### 🎯 Beta Adjustment (v2.2)
- Reputation-weighted parameter tuning
- Adaptive correction based on telemetry
- pH target: 6.5 ± 0.3
- Mycelium target: ≥ 0.85

### ⛓️ Blockchain Snapshots (v2.3)
- Daily system state collection
- Root hash aggregation
- Blockchain transaction submission
- Local snapshot backup

### 🛡️ Adaptive Shield Tuning (v2.4)
- Latency-based frequency adjustment
- Default range: 50-60 Hz
- Expanded range: 45-65 Hz (high latency)
- IPFS configuration anchoring

### 📊 Automated Reports (v2.5)
- Daily KPI compilation
- Markdown format output
- IPFS anchoring with CID
- Reputation score tables

## Modules

### `reputation.py`
Node reputation tracking and weight calculation.

```python
from vacuum_node.reputation import update, weight

# Update reputation with latest telemetry
update("node1", ph=6.5, myzel=0.87)

# Get current weight
w = weight("node1")  # Returns 0.1 - 1.0
```

### `distributor.py`
Beta parameter adjustment with reputation weighting.

```python
from vacuum_node.distributor import adjust_beta

# Adjust beta with reputation weighting
new_beta = adjust_beta("node1", ph=6.4, myzel=0.86, beta=0.2)
```

### `blockchain.py`
Blockchain transaction interface.

```python
from vacuum_node.blockchain import Chain

chain = Chain("http://blockchain:8545")
tx_id = chain.submit_transaction({"type": "data", "content": "..."})
```

### `ipfs_anchor.py`
IPFS content anchoring.

```python
from vacuum_node.ipfs_anchor import anchor_ipfs

cid = anchor_ipfs({"key": "value"}, "/path/to/data")
print(f"Anchored at: {cid}")
```

### `snapshot.py`
System state snapshot collection.

```bash
python -m vacuum_node.snapshot
```

### `shield_tuner.py`
Adaptive shield frequency tuning.

```bash
python -m vacuum_node.shield_tuner
```

### `report.py`
24-hour report generation.

```bash
python -m vacuum_node.report
```

## Installation

### Via pip (development)
```bash
pip install -r requirements_vacuum_node.txt
export PYTHONPATH=/path/to/repo:$PYTHONPATH
```

### Via Docker
```bash
docker build -f Dockerfile.vacuum_node -t vacuum-node:latest .
docker run vacuum-node:latest python -m vacuum_node.snapshot
```

### Via Kubernetes
```bash
kubectl apply -f k8s/
```

## Configuration

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `CHAIN_ENDPOINT` | `http://blockchain:8545` | Blockchain RPC endpoint |
| `IPFS_ENDPOINT` | `http://ipfs:5001` | IPFS API endpoint |
| `METRICS_ENDPOINT` | `http://monitoring:9090/...` | Prometheus metrics |
| `MANIFEST_PATH` | `/etc/vacuum/ghp-manifest.json` | GHP manifest location |
| `TELEMETRY_PATH` | `/var/lib/vacuum/telemetry_summary.json` | Telemetry data |
| `REPORT_DIR` | `/tmp` | Report output directory |

### File Paths

| Path | Purpose | Auto-created |
|------|---------|--------------|
| `/etc/vacuum/reputation.json` | Reputation data | Yes |
| `/etc/vacuum/shield_config.json` | Shield configuration | Yes |
| `/var/lib/vacuum/snapshots/` | Snapshot storage | Yes |
| `/var/lib/vacuum/reports/` | Report output | Yes |

## Kubernetes CronJobs

### Consensus Snapshot
- **Schedule**: Daily at 00:00 UTC
- **File**: `k8s/consensus-snapshot.yaml`
- **Purpose**: System state blockchain anchoring

### Shield Tuner
- **Schedule**: Every 6 hours
- **File**: `k8s/shield-tuner.yaml`
- **Purpose**: Adaptive frequency adjustment

### Daily Report
- **Schedule**: Daily at 02:00 UTC
- **File**: `k8s/daily-report.yaml`
- **Purpose**: KPI report generation

## Testing

### Run All Tests
```bash
python3 -m py_compile vacuum_node/*.py
```

### Import Test
```bash
python3 -c "from vacuum_node import reputation, distributor, blockchain"
```

### Module Tests
```bash
# Test reputation
python3 -c "from vacuum_node.reputation import weight; print(weight('test'))"

# Test distributor
python3 -c "from vacuum_node.distributor import adjust_beta; print(adjust_beta('test', 6.5, 0.85, 0.2))"
```

## Monitoring

### Check CronJob Status
```bash
kubectl get cronjobs -n vacuum
kubectl get jobs -n vacuum
```

### View Logs
```bash
kubectl logs -n vacuum job/<job-name>
```

### Metrics
- Grafana dashboard: `ghp/reports`
- Shield metrics: `shield/metrics`

## Troubleshooting

### Import Errors
```bash
export PYTHONPATH=/app:$PYTHONPATH
python3 -c "import vacuum_node"
```

### File Permissions
```bash
chmod 755 /etc/vacuum /var/lib/vacuum
```

### Network Issues
```bash
curl http://blockchain:8545
curl http://ipfs:5001/api/v0/version
```

## API Reference

### Reputation Functions

#### `update(node_id: str, ph: float, myzel: float) -> None`
Update reputation based on latest telemetry.

#### `weight(node_id: str) -> float`
Calculate reputation weight (0.1 - 1.0).

### Distributor Functions

#### `adjust_beta(node_id: str, ph: float, myzel: float, beta: float) -> float`
Adjust beta parameter with reputation weighting.

### Blockchain Functions

#### `Chain.submit_transaction(data: dict) -> str`
Submit transaction to blockchain.

#### `Chain.get_transaction(tx_hash: str) -> dict`
Retrieve transaction details.

### IPFS Functions

#### `anchor_ipfs(data: Union[str, bytes, dict], path: str) -> str`
Anchor data to IPFS and return CID.

#### `get_from_ipfs(cid: str) -> bytes`
Retrieve data from IPFS by CID.

## Dependencies

- Python 3.9+
- requests >= 2.28.0
- jinja2 >= 3.1.0 (optional)

## License

See LICENSE file in repository root.

## Documentation

- **Quick Start**: `QUICK_DEPLOY.md`
- **Full Deployment**: `DEPLOYMENT_v2.1-v2.5.md`
- **Implementation Details**: `IMPLEMENTATION_SUMMARY_v2.1-v2.5.md`

## Support

For issues, questions, or contributions:
- GitHub Issues: [Repository Issues](https://github.com/hannesmitterer/SYNTHEIA-GENESIS-BLOCK--v0.0-/issues)
- Documentation: See docs in repository root

---

Built with ❤️ for the SYNTHEIA Genesis Block project
