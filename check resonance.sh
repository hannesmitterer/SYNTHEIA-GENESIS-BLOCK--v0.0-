#!/bin/bash
# Lex Amoris Cluster Vitality Check

echo "--- [NSR] MESH RESONANCE STATUS ---"
# 1. Prüfe IPFS Cluster Peers
echo "[1] Checking P2P Connectivity..."
ipfs-cluster-ctl peers ls | grep -E "PeerID|Name"

# 2. Prüfe Pin-Synchronität
echo -e "\n[2] Checking Data Anchoring..."
ipfs-cluster-ctl pin ls | tail -n 5

# 3. Prüfe WireGuard Tunnel
echo -e "\n[3] Checking VPN Latency (10.10.0.x)..."
for i in {1..12}; do
    ping -c 1 -W 1 10.10.0.$i > /dev/null
    if [ $? -eq 0 ]; then
        echo "Node $i: ONLINE"
    else
        echo "Node $i: OFFLINE (Dissonanz)"
    fi
done

echo "------------------------------------"
echo "Lex Amoris Signature: 📜⚖️❤️☮️"
