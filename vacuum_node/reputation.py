# vacuum_node/reputation.py
import json
from datetime import datetime, timedelta

# Persistente Datei (kann später in ein ConfigMap/Secret migriert werden)
REP_FILE = "/etc/vacuum/reputation.json"
WINDOW_DAYS = 7          # Bewertung über die letzte Woche
MIN_WEIGHT = 0.1
MAX_WEIGHT = 1.0

def _load():
    try:
        with open(REP_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def _save(data):
    with open(REP_FILE, "w") as f:
        json.dump(data, f, indent=2)

def update(node_id: str, ph: float, myzel: float) -> None:
    """Update reputation based on latest telemetry."""
    data = _load()
    now = datetime.utcnow().isoformat()
    entry = {"ts": now, "ph": ph, "myzel": myzel}
    data.setdefault(node_id, []).append(entry)

    # keep only last WINDOW_DAYS
    cutoff = datetime.utcnow() - timedelta(days=WINDOW_DAYS)
    data[node_id] = [
        e for e in data[node_id] if datetime.fromisoformat(e["ts"]) >= cutoff
    ]
    _save(data)

def weight(node_id: str) -> float:
    """Calculate a weight between MIN_WEIGHT and MAX_WEIGHT."""
    data = _load().get(node_id, [])
    if not data:
        return MIN_WEIGHT

    # Scoring: close to target pH (6.5) und myzel ≥ 0.85
    ph_scores = [1 - abs(6.5 - e["ph"]) / 0.5 for e in data]   # 0‑1
    myzel_scores = [min(e["myzel"] / 0.85, 1.0) for e in data]
    avg_score = sum(ph_scores + myzel_scores) / (2 * len(data))

    # Linear map 0‑1 → MIN‑MAX
    return MIN_WEIGHT + avg_score * (MAX_WEIGHT - MIN_WEIGHT)
