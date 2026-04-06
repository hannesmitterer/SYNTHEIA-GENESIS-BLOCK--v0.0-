import json
import os
from vacuum_node.ipfs_anchor import anchor_ipfs

CONFIG_PATH = "/etc/vacuum/shield_config.json"

def load_cfg():
    try:
        with open(CONFIG_PATH) as f:
            return json.load(f)
    except FileNotFoundError:
        # Return default configuration
        return {
            "band_start": 50,
            "band_end": 60,
            "version": "2.4"
        }

def save_cfg(cfg):
    try:
        os.makedirs(os.path.dirname(CONFIG_PATH), exist_ok=True)
        with open(CONFIG_PATH, "w") as f:
            json.dump(cfg, f, indent=2)
        # optional: anchor the new config on IPFS for immutability
        anchor_ipfs(cfg, "/shield/config")
    except Exception as e:
        print(f"Error saving shield config: {e}")

def adaptive_tuning(avg_latency_ms: float):
    """
    Adaptively tune shield frequency band based on latency
    
    Args:
        avg_latency_ms: Average latency in milliseconds
    """
    cfg = load_cfg()
    # default band: 50‑60 Hz, expand if latency > 150 ms
    if avg_latency_ms > 150:
        cfg["band_start"] = max(45, cfg["band_start"] - 5)
        cfg["band_end"]   = min(65, cfg["band_end"]   + 5)
        print(f"High latency detected ({avg_latency_ms}ms), expanding band to {cfg['band_start']}-{cfg['band_end']} Hz")
    else:
        cfg["band_start"] = 50
        cfg["band_end"]   = 60
        print(f"Normal latency ({avg_latency_ms}ms), resetting band to {cfg['band_start']}-{cfg['band_end']} Hz")
    save_cfg(cfg)


def main():
    """Main entry point for shield tuner"""
    import requests
    
    # Fetch metrics from monitoring endpoint
    metrics_endpoint = os.getenv("METRICS_ENDPOINT", "http://monitoring:9090/api/v1/query?query=avg_shield_latency")
    
    try:
        response = requests.get(metrics_endpoint, timeout=30)
        if response.status_code == 200:
            data = response.json()
            # Extract latency value from Prometheus response
            if data.get("status") == "success" and data.get("data", {}).get("result"):
                result = data["data"]["result"][0]
                latency = float(result["value"][1])
                print(f"Fetched latency: {latency}ms")
                adaptive_tuning(latency)
            else:
                print("No metrics data available, using default latency")
                adaptive_tuning(100.0)  # default
        else:
            print(f"Metrics endpoint returned {response.status_code}")
            adaptive_tuning(100.0)
    except Exception as e:
        print(f"Error fetching metrics: {e}")
        adaptive_tuning(100.0)  # fallback


if __name__ == "__main__":
    main()
