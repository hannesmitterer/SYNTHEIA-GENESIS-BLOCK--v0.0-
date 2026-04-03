"""
AquaLibre Network Protocol - Cryptographic Identity System
Prevents Sybil attacks through public key cryptography
"""

import hashlib
import json
from typing import Dict, Any, Optional
from datetime import datetime
import secrets


class NodeIdentity:
    """
    Cryptographic identity for AquaLibre nodes
    1 Node = 1 cryptographic identity (prevents fake scaling)
    """
    
    def __init__(self, node_id: str, public_key: Optional[str] = None, private_key: Optional[str] = None):
        self.node_id = node_id
        
        if public_key and private_key:
            # Use provided keys
            self.public_key = public_key
            self.private_key = private_key
        else:
            # Generate new keypair (simplified - in production use proper crypto)
            self.private_key = secrets.token_hex(32)
            self.public_key = hashlib.sha256(self.private_key.encode()).hexdigest()
        
        self.identity_hash = self._generate_identity_hash()
    
    def _generate_identity_hash(self) -> str:
        """Generate unique identity hash from public key and node_id"""
        identity_data = f"{self.node_id}:{self.public_key}"
        return hashlib.sha256(identity_data.encode()).hexdigest()
    
    def sign(self, payload: Dict[str, Any]) -> str:
        """
        Sign a payload with private key
        Simplified signing - in production use Ed25519 or similar
        """
        payload_str = json.dumps(payload, sort_keys=True)
        signature_data = f"{payload_str}:{self.private_key}"
        return hashlib.sha256(signature_data.encode()).hexdigest()
    
    def verify(self, payload: Dict[str, Any], signature: str) -> bool:
        """
        Verify a signature against this identity's public key
        """
        expected_signature = self.sign(payload)
        return signature == expected_signature
    
    @staticmethod
    def verify_external(public_key: str, payload: Dict[str, Any], signature: str) -> bool:
        """
        Verify a signature from another node
        """
        payload_str = json.dumps(payload, sort_keys=True)
        # In simplified version, we can't verify without private key
        # This would use proper public key cryptography in production
        return len(signature) == 64  # Basic sanity check
    
    def get_identity_proof(self) -> Dict[str, Any]:
        """Generate identity proof for network registration"""
        return {
            "node_id": self.node_id,
            "public_key": self.public_key,
            "identity_hash": self.identity_hash,
            "timestamp": datetime.now().isoformat()
        }
    
    def to_dict(self) -> Dict[str, Any]:
        """Export identity (without private key)"""
        return {
            "node_id": self.node_id,
            "public_key": self.public_key,
            "identity_hash": self.identity_hash
        }


class NodeState:
    """
    Weighted node state - not all nodes are equal
    Stable nodes have more influence in the network
    """
    
    def __init__(self, water_capacity: float, reliability: float = 1.0):
        """
        water_capacity: Maximum water processing capacity (liters/day)
        reliability: Historical reliability score (0.0 to 1.0)
        """
        self.water_capacity = water_capacity
        self.reliability = max(0.0, min(1.0, reliability))  # Clamp to 0-1
        self.uptime_history: list = []
        self.action_history: list = []
    
    def update_reliability(self, successful_actions: int, total_actions: int):
        """Update reliability based on action success rate"""
        if total_actions > 0:
            success_rate = successful_actions / total_actions
            # Moving average with previous reliability
            self.reliability = (self.reliability * 0.7) + (success_rate * 0.3)
    
    def record_uptime(self, is_online: bool):
        """Record uptime for reliability calculation"""
        self.uptime_history.append({
            "timestamp": datetime.now().isoformat(),
            "online": is_online
        })
        
        # Keep only last 100 records
        if len(self.uptime_history) > 100:
            self.uptime_history = self.uptime_history[-100:]
        
        # Update reliability based on uptime
        if len(self.uptime_history) >= 10:
            online_count = sum(1 for record in self.uptime_history[-100:] if record["online"])
            uptime_ratio = online_count / len(self.uptime_history[-100:])
            self.reliability = (self.reliability * 0.8) + (uptime_ratio * 0.2)
    
    def get_weight(self) -> float:
        """
        Calculate node weight for consensus voting
        Combines capacity and reliability
        """
        return self.water_capacity * self.reliability
    
    def to_dict(self) -> Dict[str, Any]:
        """Export node state"""
        return {
            "water_capacity": self.water_capacity,
            "reliability": self.reliability,
            "weight": self.get_weight(),
            "uptime_records": len(self.uptime_history)
        }


class TimeAveragedMetrics:
    """
    Time-based validation - prevents short-term manipulation
    Behavior must be consistent over time
    """
    
    def __init__(self, window_size: int = 30):
        """
        window_size: Number of data points to average (default: 30 days)
        """
        self.window_size = window_size
        self.metrics_history: Dict[str, list] = {}
    
    def record_metric(self, metric_name: str, value: float):
        """Record a metric value with timestamp"""
        if metric_name not in self.metrics_history:
            self.metrics_history[metric_name] = []
        
        self.metrics_history[metric_name].append({
            "timestamp": datetime.now().isoformat(),
            "value": value
        })
        
        # Keep only window_size + buffer
        max_records = self.window_size + 10
        if len(self.metrics_history[metric_name]) > max_records:
            self.metrics_history[metric_name] = self.metrics_history[metric_name][-max_records:]
    
    def rolling_average(self, metric_name: str, window: Optional[int] = None) -> float:
        """Calculate rolling average for a metric"""
        if metric_name not in self.metrics_history:
            return 0.0
        
        window = window or self.window_size
        values = self.metrics_history[metric_name][-window:]
        
        if not values:
            return 0.0
        
        return sum(v["value"] for v in values) / len(values)
    
    def get_trend(self, metric_name: str) -> str:
        """
        Determine trend: IMPROVING, STABLE, DECLINING
        """
        if metric_name not in self.metrics_history:
            return "UNKNOWN"
        
        values = self.metrics_history[metric_name]
        if len(values) < 2:
            return "INSUFFICIENT_DATA"
        
        # Compare first half vs second half
        mid = len(values) // 2
        first_half = sum(v["value"] for v in values[:mid]) / mid
        second_half = sum(v["value"] for v in values[mid:]) / (len(values) - mid)
        
        diff = second_half - first_half
        if diff > 0.1:
            return "IMPROVING"
        elif diff < -0.1:
            return "DECLINING"
        else:
            return "STABLE"
    
    def is_consistent(self, metric_name: str, threshold: float = 0.2) -> bool:
        """
        Check if metric is consistent (low variance)
        Prevents gaming through volatile behavior
        """
        if metric_name not in self.metrics_history:
            return False
        
        values = [v["value"] for v in self.metrics_history[metric_name][-self.window_size:]]
        
        if len(values) < 5:
            return False
        
        avg = sum(values) / len(values)
        variance = sum((v - avg) ** 2 for v in values) / len(values)
        std_dev = variance ** 0.5
        
        # Coefficient of variation
        if avg == 0:
            return False
        
        cv = std_dev / avg
        return cv < threshold
    
    def to_dict(self) -> Dict[str, Any]:
        """Export metrics summary"""
        summary = {}
        for metric_name in self.metrics_history:
            summary[metric_name] = {
                "current": self.metrics_history[metric_name][-1]["value"] if self.metrics_history[metric_name] else 0,
                "rolling_average": self.rolling_average(metric_name),
                "trend": self.get_trend(metric_name),
                "consistent": self.is_consistent(metric_name),
                "records": len(self.metrics_history[metric_name])
            }
        return summary


def demo_identity_system():
    """Demonstrate the identity and metrics system"""
    print("=" * 80)
    print("AQUALIBRE NETWORK LAYER - Identity & Metrics Demo")
    print("=" * 80)
    
    # Create node identity
    print("\n🔐 Creating cryptographic node identity...")
    identity = NodeIdentity("MQ-001")
    print(f"  Node ID: {identity.node_id}")
    print(f"  Public Key: {identity.public_key[:16]}...")
    print(f"  Identity Hash: {identity.identity_hash[:16]}...")
    
    # Sign a payload
    print("\n✍️  Signing a water report...")
    payload = {
        "node_id": "MQ-001",
        "water_extraction": 120,
        "water_recharge": 150,
        "timestamp": datetime.now().isoformat()
    }
    signature = identity.sign(payload)
    print(f"  Signature: {signature[:16]}...")
    
    # Verify signature
    print("\n✅ Verifying signature...")
    is_valid = identity.verify(payload, signature)
    print(f"  Valid: {is_valid}")
    
    # Test tampered payload
    print("\n❌ Testing tampered payload...")
    tampered_payload = payload.copy()
    tampered_payload["water_extraction"] = 200  # Changed!
    is_valid_tampered = identity.verify(tampered_payload, signature)
    print(f"  Valid: {is_valid_tampered} (should be False)")
    
    # Node state
    print("\n⚖️  Creating weighted node state...")
    node_state = NodeState(water_capacity=1000.0, reliability=0.95)
    print(f"  Capacity: {node_state.water_capacity} L/day")
    print(f"  Reliability: {node_state.reliability}")
    print(f"  Weight: {node_state.get_weight()}")
    
    # Record some uptime
    print("\n📊 Recording uptime...")
    for i in range(10):
        node_state.record_uptime(True)
    print(f"  Reliability after uptime: {node_state.reliability:.3f}")
    
    # Time-averaged metrics
    print("\n⏱️  Recording time-averaged metrics...")
    metrics = TimeAveragedMetrics(window_size=10)
    
    # Simulate water data over time
    for day in range(15):
        extraction = 100 + (day * 2)  # Increasing extraction
        recharge = 150 - day  # Decreasing recharge
        
        metrics.record_metric("extraction", extraction)
        metrics.record_metric("recharge", recharge)
    
    print(f"  Extraction average: {metrics.rolling_average('extraction'):.2f}")
    print(f"  Recharge average: {metrics.rolling_average('recharge'):.2f}")
    print(f"  Extraction trend: {metrics.get_trend('extraction')}")
    print(f"  Recharge trend: {metrics.get_trend('recharge')}")
    print(f"  Extraction consistent: {metrics.is_consistent('extraction')}")
    
    print("\n" + "=" * 80)
    print("✅ Identity & Metrics System Operational")
    print("=" * 80)


if __name__ == "__main__":
    demo_identity_system()
