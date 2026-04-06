# SYNTHEIA v2.1-v2.5 Quick Deploy

## One-Liner Deployment

```bash
# Build and deploy everything
docker build -f Dockerfile.vacuum_node -t duckai/vacuum-node:latest . && \
docker push duckai/vacuum-node:latest && \
kubectl apply -f k8s/ && \
kubectl rollout restart deployment argilla-distributor -n vacuum
```

## Individual Commands

### Build Docker Image
```bash
docker build -f Dockerfile.vacuum_node -t duckai/vacuum-node:latest .
docker push duckai/vacuum-node:latest
```

### Deploy Kubernetes Jobs
```bash
kubectl apply -f k8s/consensus-snapshot.yaml
kubectl apply -f k8s/shield-tuner.yaml
kubectl apply -f k8s/daily-report.yaml
```

### Restart Deployment
```bash
kubectl rollout restart deployment argilla-distributor -n vacuum
```

## Verify Installation

```bash
# Check CronJobs
kubectl get cronjobs -n vacuum

# Expected output:
# NAME                  SCHEDULE        SUSPEND   ACTIVE
# consensus-snapshot    0 */24 * * *    False     0
# shield-tuner          0 */6 * * *     False     0
# daily-ghp-report      0 2 * * *       False     0
```

## Quick Test

```bash
# Test reputation module
kubectl exec -it <pod> -n vacuum -- python3 -c "from vacuum_node.reputation import weight; print(weight('test'))"

# Trigger snapshot manually
kubectl create job --from=cronjob/consensus-snapshot manual-snapshot-test -n vacuum

# View logs
kubectl logs -n vacuum job/manual-snapshot-test
```

## Rollback

```bash
# Remove CronJobs
kubectl delete -f k8s/

# Revert code
git revert HEAD~6..HEAD
```

## Support

- Full documentation: `DEPLOYMENT_v2.1-v2.5.md`
- Implementation details: `IMPLEMENTATION_SUMMARY_v2.1-v2.5.md`
- Issue tracking: GitHub Issues

---
Version: 2.5 | Date: 2026-04-06
