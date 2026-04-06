import json
import os
import datetime
from typing import Dict, Any

# Import jinja2 if available, otherwise use simple string formatting
try:
    from jinja2 import Template
    HAS_JINJA2 = True
except ImportError:
    HAS_JINJA2 = False
    print("Warning: jinja2 not available, using simple formatting")

REPORT_TEMPLATE = """
# Global Harmony Report – {{ date }}

## KPIs
- **Fläche aktiv**: {{ area }} ha
- **Resonanz U**: {{ u }} Hz (ΔU = {{ delta_u }} Hz)
- **Myzel‑Signal**: {{ myzel }} (≥ 0.85)
- **pH‑Durchschnitt**: {{ ph }} (6.5 ± 0.3)

## Reputation‑Durchschnitt
{{ reputation_table }}

*Report anchored on IPFS:* {{ ipfs_cid }}
"""


def load_telemetry_data() -> Dict[str, Any]:
    """Load telemetry summary data"""
    telemetry_path = os.getenv("TELEMETRY_PATH", "/var/lib/vacuum/telemetry_summary.json")
    
    try:
        with open(telemetry_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Telemetry file not found at {telemetry_path}, using defaults")
        return {
            "area_ha": 1000,
            "resonance_u": 1088.20,
            "myzel_avg": 0.87,
            "ph_avg": 6.48
        }


def load_reputation_data() -> Dict[str, float]:
    """Load reputation data"""
    from vacuum_node.reputation import _load
    
    try:
        rep_data = _load()
        # Calculate weight for each node
        from vacuum_node.reputation import weight
        return {nid: weight(nid) for nid in rep_data.keys()}
    except Exception as e:
        print(f"Error loading reputation data: {e}")
        return {}


def generate():
    """Generate the 24-hour report"""
    # Load data
    data = load_telemetry_data()
    rep = load_reputation_data()

    # Build reputation table
    if rep:
        reputation_rows = "\n".join(
            f"| {nid} | {round(w, 2)} |" for nid, w in rep.items()
        )
        rep_table = f"| Node | Weight |\n|------|--------|\n{reputation_rows}"
    else:
        rep_table = "| Node | Weight |\n|------|--------|\n| (no data) | - |"

    # Prepare template variables
    template_vars = {
        "date": datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC"),
        "area": data.get("area_ha", 0),
        "u": data.get("resonance_u", 0),
        "delta_u": abs(data.get("resonance_u", 1088.20) - 1088.20),
        "myzel": round(data.get("myzel_avg", 0), 3),
        "ph": round(data.get("ph_avg", 0), 3),
        "reputation_table": rep_table,
        "ipfs_cid": "pending"
    }

    # Render template
    if HAS_JINJA2:
        rendered = Template(REPORT_TEMPLATE).render(**template_vars)
    else:
        # Simple string formatting fallback
        rendered = REPORT_TEMPLATE
        for key, value in template_vars.items():
            rendered = rendered.replace("{{ " + key + " }}", str(value))

    # Write temporary file
    report_dir = os.getenv("REPORT_DIR", "/tmp")
    os.makedirs(report_dir, exist_ok=True)
    path = os.path.join(report_dir, "ghp_report.md")
    
    with open(path, "w") as f:
        f.write(rendered)

    # Anchor on IPFS
    try:
        from vacuum_node.ipfs_anchor import anchor_ipfs
        with open(path, "rb") as f:
            content = f.read()
        cid = anchor_ipfs(content, "/report/24h")
        
        # Replace placeholder with actual CID
        with open(path, "r") as f:
            content = f.read().replace("pending", cid)
        with open(path, "w") as f:
            f.write(content)
        
        print(f"Report generated and anchored: {cid}")
        print(f"Report saved to: {path}")
    except Exception as e:
        print(f"Error anchoring report: {e}")
        print(f"Report saved locally to: {path}")

    return path


if __name__ == "__main__":
    generate()
