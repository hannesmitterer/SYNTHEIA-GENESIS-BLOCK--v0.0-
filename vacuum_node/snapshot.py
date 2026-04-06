import os
import json
import hashlib
import requests
from datetime import datetime
from vacuum_node.blockchain import Chain


def main():
    """
    Collect current system state and submit snapshot to blockchain
    """
    # Sammle aktuelle System‑State (Root‑Hash, Reputation‑Scores, U‑Mittelwert)
    manifest_path = os.getenv("MANIFEST_PATH", "/etc/vacuum/ghp-manifest.json")
    
    try:
        with open(manifest_path) as f:
            manifest = json.load(f)
    except FileNotFoundError:
        print(f"Manifest not found at {manifest_path}, creating minimal snapshot")
        manifest = {"rootHash": "genesis", "regions": []}

    rep = {}
    for node in manifest.get("regions", []):
        # simplified: just fetch weight
        from vacuum_node.reputation import weight
        try:
            rep[node["id"]] = weight(node["id"])
        except Exception:
            rep[node.get("id", "unknown")] = 0.1  # default weight
    
    snapshot = {
        "root": manifest.get("rootHash", "unknown"),
        "reputation": rep,
        "timestamp": datetime.utcnow().isoformat(),
        "version": "2.3"
    }
    
    snap_hash = hashlib.sha256(json.dumps(snapshot, sort_keys=True).encode()).hexdigest()
    snapshot["hash"] = snap_hash

    # Write to blockchain
    chain_endpoint = os.getenv("CHAIN_ENDPOINT", "http://blockchain:8545")
    chain = Chain(chain_endpoint)
    tx = chain.submit_transaction({"type": "snapshot", "hash": snap_hash, "data": snapshot})
    
    print(f"Submitted snapshot tx {tx}")
    print(f"Snapshot hash: {snap_hash}")
    print(f"Reputation scores: {rep}")
    
    # Optionally save snapshot locally
    snapshot_dir = "/var/lib/vacuum/snapshots"
    try:
        os.makedirs(snapshot_dir, exist_ok=True)
        snapshot_file = os.path.join(snapshot_dir, f"snapshot_{snap_hash[:8]}.json")
        with open(snapshot_file, "w") as f:
            json.dump(snapshot, f, indent=2)
        print(f"Snapshot saved to {snapshot_file}")
    except Exception as e:
        print(f"Could not save snapshot locally: {e}")


if __name__ == "__main__":
    main()
