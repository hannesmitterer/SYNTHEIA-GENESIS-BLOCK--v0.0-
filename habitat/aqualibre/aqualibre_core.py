"""
AquaLibre Core v1.0
Low-Tech Universal Framework for Water Sovereignty

Das Wasser ist frei - Water flows under Lex Amoris jurisdiction
Martinique & Bolzano autonomous water nodes
"""

import json
import hashlib
from datetime import datetime
from typing import Dict, Any, List, Optional
from math import exp


class SchumannLock:
    """
    Schumann Resonance Lock - validates water sensor data
    Only accepts data aligned with natural Earth frequencies (7.83 Hz fundamental)
    """
    
    SCHUMANN_FUNDAMENTAL = 7.83  # Hz - Earth's heartbeat
    TOLERANCE = 0.5  # Hz
    
    def __init__(self):
        self.locked_frequency = self.SCHUMANN_FUNDAMENTAL
        self.validation_history: List[Dict[str, Any]] = []
    
    def validate_resonance(self, sensor_data: Dict[str, Any]) -> bool:
        """
        Validate sensor data against Schumann resonance
        Returns True only if data shows natural harmonic alignment
        """
        frequency = sensor_data.get("resonance_frequency", 0)
        
        # Check if frequency is within natural tolerance
        is_valid = abs(frequency - self.SCHUMANN_FUNDAMENTAL) <= self.TOLERANCE
        
        validation_record = {
            "timestamp": datetime.now().isoformat(),
            "frequency": frequency,
            "valid": is_valid,
            "sensor_id": sensor_data.get("sensor_id", "unknown")
        }
        
        self.validation_history.append(validation_record)
        
        return is_valid
    
    def get_lock_status(self) -> Dict[str, Any]:
        """Return current lock status"""
        return {
            "locked_frequency": self.locked_frequency,
            "tolerance": self.TOLERANCE,
            "validations_count": len(self.validation_history),
            "status": "LOCKED"
        }


class NSRStandard:
    """
    No Secret Revenue (NSR) Standard Validator
    Ensures no hidden fees, no central shutdown mechanisms
    """
    
    FORBIDDEN_PATTERNS = [
        "hidden_fee",
        "secret_charge",
        "central_control",
        "remote_shutdown",
        "forced_payment",
        "extraction_tax",
        "privatization"
    ]
    
    def __init__(self):
        self.violations: List[Dict[str, Any]] = []
    
    def validate_transaction(self, transaction: Dict[str, Any]) -> bool:
        """
        Validate that transaction contains no hidden fees or control mechanisms
        """
        transaction_str = json.dumps(transaction).lower()
        
        for pattern in self.FORBIDDEN_PATTERNS:
            if pattern in transaction_str:
                self.violations.append({
                    "timestamp": datetime.now().isoformat(),
                    "pattern": pattern,
                    "transaction": transaction
                })
                return False
        
        # Check for transparency
        if "fee" in transaction and transaction.get("fee_disclosed", False) is False:
            self.violations.append({
                "timestamp": datetime.now().isoformat(),
                "pattern": "undisclosed_fee",
                "transaction": transaction
            })
            return False
        
        return True
    
    def get_compliance_status(self) -> Dict[str, Any]:
        """Return NSR compliance status"""
        return {
            "compliant": len(self.violations) == 0,
            "violations_count": len(self.violations),
            "status": "NSR_COMPLIANT" if len(self.violations) == 0 else "VIOLATIONS_DETECTED"
        }


class WaterSensor:
    """
    Water sensor interface for flow, purity, and mycelium filtration
    Measured by resonance, not controlled by algorithms
    """
    
    def __init__(self, sensor_id: str, location: str):
        self.sensor_id = sensor_id
        self.location = location  # e.g., "Martinique" or "Bolzano"
        self.readings: List[Dict[str, Any]] = []
    
    def read_flow(self, flow_rate: float, resonance_freq: float) -> Dict[str, Any]:
        """
        Read water flow rate with resonance frequency
        flow_rate: liters per minute
        resonance_freq: measured frequency in Hz
        """
        reading = {
            "type": "flow",
            "sensor_id": self.sensor_id,
            "location": self.location,
            "timestamp": datetime.now().isoformat(),
            "flow_rate_lpm": flow_rate,
            "resonance_frequency": resonance_freq,
            "unit": "liters/minute"
        }
        self.readings.append(reading)
        return reading
    
    def read_purity(self, purity_level: float, resonance_freq: float) -> Dict[str, Any]:
        """
        Read water purity level with resonance frequency
        purity_level: 0.0 to 1.0 (1.0 = pure)
        """
        reading = {
            "type": "purity",
            "sensor_id": self.sensor_id,
            "location": self.location,
            "timestamp": datetime.now().isoformat(),
            "purity_level": purity_level,
            "resonance_frequency": resonance_freq,
            "unit": "normalized"
        }
        self.readings.append(reading)
        return reading
    
    def read_mycelium_filtration(self, efficiency: float, resonance_freq: float) -> Dict[str, Any]:
        """
        Read mycelium filtration efficiency with resonance frequency
        efficiency: 0.0 to 1.0 (1.0 = perfect filtration)
        """
        reading = {
            "type": "mycelium_filtration",
            "sensor_id": self.sensor_id,
            "location": self.location,
            "timestamp": datetime.now().isoformat(),
            "filtration_efficiency": efficiency,
            "resonance_frequency": resonance_freq,
            "unit": "normalized"
        }
        self.readings.append(reading)
        return reading
    
    def get_latest_readings(self, count: int = 10) -> List[Dict[str, Any]]:
        """Get latest sensor readings"""
        return self.readings[-count:]


class SovereignROI:
    """
    Sovereign Return on Investment (S-ROI) for Water
    Success measured by local hydrology enhancement, not sales
    
    Formula: W_souverän = (Natural_Inflow / Extraction) * Φ
    where Φ is the golden ratio (1.618...)
    """
    
    PHI = 1.618033988749895  # Golden ratio
    
    def __init__(self):
        self.calculations: List[Dict[str, Any]] = []
    
    def calculate_water_sovereignty(
        self, 
        natural_inflow: float,  # Natural water supply (liters/day)
        extraction: float,       # Water extracted (liters/day)
        regenerated: float = 0.0  # Water regenerated/saved (liters/day)
    ) -> Dict[str, Any]:
        """
        Calculate sovereign water index
        Higher value = better sovereignty (habitat becomes richer as we exploit less)
        """
        if extraction <= 0:
            extraction = 0.001  # Prevent division by zero
        
        # Account for regenerated water
        effective_inflow = natural_inflow + regenerated
        
        # Calculate sovereignty index
        w_sovereign = (effective_inflow / extraction) * self.PHI
        
        # Existence index increases as ratio improves
        existence_index = w_sovereign
        
        calculation = {
            "timestamp": datetime.now().isoformat(),
            "natural_inflow": natural_inflow,
            "extraction": extraction,
            "regenerated": regenerated,
            "effective_inflow": effective_inflow,
            "w_sovereign": w_sovereign,
            "existence_index": existence_index,
            "phi": self.PHI,
            "status": "SOVEREIGN" if w_sovereign >= 1.0 else "DEPENDENT"
        }
        
        self.calculations.append(calculation)
        return calculation
    
    def get_sovereignty_level(self) -> float:
        """Get current sovereignty level (0.0 to infinity, 1.0+ is autonomous)"""
        if not self.calculations:
            return 0.0
        return self.calculations[-1]["w_sovereign"]


class RESPECTFilter:
    """
    Decentralized monitoring and alarm system
    Alerts when corporations attempt to privatize water sources
    """
    
    def __init__(self):
        self.alerts: List[Dict[str, Any]] = []
        self.mesh_nodes: List[str] = []
    
    def register_node(self, node_id: str):
        """Register a node in the mesh network"""
        if node_id not in self.mesh_nodes:
            self.mesh_nodes.append(node_id)
    
    def check_privatization_attempt(
        self, 
        entity: str, 
        action: str, 
        water_source: str
    ) -> bool:
        """
        Check if an action represents a privatization attempt
        Returns True if violation detected
        """
        privatization_keywords = [
            "claim",
            "ownership",
            "exclusive_rights",
            "patent",
            "monopoly",
            "restricted_access",
            "commercial_control"
        ]
        
        action_lower = action.lower()
        is_violation = any(keyword in action_lower for keyword in privatization_keywords)
        
        if is_violation:
            alert = {
                "timestamp": datetime.now().isoformat(),
                "severity": "CRITICAL",
                "entity": entity,
                "action": action,
                "water_source": water_source,
                "violation_type": "LEX_AMORIS_BREACH",
                "message": f"Privatization attempt detected: {entity} attempting to {action} on {water_source}"
            }
            self.alerts.append(alert)
            self._broadcast_to_mesh(alert)
            return True
        
        return False
    
    def _broadcast_to_mesh(self, alert: Dict[str, Any]):
        """Broadcast alert to all nodes in mesh network"""
        # In production, this would send to IPFS and GitHub
        print(f"🚨 RESPECT-FILTER ALARM: {alert['message']}")
        print(f"   Broadcasting to {len(self.mesh_nodes)} mesh nodes...")
        print(f"   Violation: Lex Amoris - Water cannot be owned")
    
    def get_alert_status(self) -> Dict[str, Any]:
        """Get current alert status"""
        return {
            "total_alerts": len(self.alerts),
            "mesh_nodes": len(self.mesh_nodes),
            "recent_alerts": self.alerts[-5:] if self.alerts else [],
            "status": "ALERT" if self.alerts else "CLEAR"
        }


class AquaLibreNode:
    """
    Main AquaLibre Node - integrates all components
    Represents a local water sovereignty node (e.g., Martinique or Bolzano)
    """
    
    def __init__(self, node_id: str, location: str):
        self.node_id = node_id
        self.location = location
        self.schumann_lock = SchumannLock()
        self.nsr_standard = NSRStandard()
        self.water_sensor = WaterSensor(f"sensor_{node_id}", location)
        self.sroi = SovereignROI()
        self.respect_filter = RESPECTFilter()
        
        self.integrity_data: List[Dict[str, Any]] = []
        self.sovereignty_level = 1.0  # Full autonomy from central providers
        
        # Register with mesh
        self.respect_filter.register_node(node_id)
    
    def process_sensor_reading(
        self, 
        reading_type: str, 
        value: float, 
        resonance_freq: float
    ) -> Dict[str, Any]:
        """
        Process a sensor reading with Schumann-Lock validation
        """
        # Create sensor reading
        if reading_type == "flow":
            reading = self.water_sensor.read_flow(value, resonance_freq)
        elif reading_type == "purity":
            reading = self.water_sensor.read_purity(value, resonance_freq)
        elif reading_type == "mycelium_filtration":
            reading = self.water_sensor.read_mycelium_filtration(value, resonance_freq)
        else:
            raise ValueError(f"Unknown reading type: {reading_type}")
        
        # Validate with Schumann-Lock
        is_valid = self.schumann_lock.validate_resonance(reading)
        
        result = {
            "reading": reading,
            "schumann_validated": is_valid,
            "status": "ACCEPTED" if is_valid else "REJECTED"
        }
        
        if is_valid:
            self.integrity_data.append(result)
        
        return result
    
    def calculate_sovereignty(
        self, 
        natural_inflow: float, 
        extraction: float, 
        regenerated: float = 0.0
    ) -> Dict[str, Any]:
        """Calculate and update node sovereignty"""
        roi = self.sroi.calculate_water_sovereignty(natural_inflow, extraction, regenerated)
        self.sovereignty_level = roi["w_sovereign"]
        return roi
    
    def report_integrity(self) -> Dict[str, Any]:
        """
        Generate integrity report for IPFS/GitHub mirroring
        """
        report = {
            "node_id": self.node_id,
            "location": self.location,
            "timestamp": datetime.now().isoformat(),
            "sovereignty_level": self.sovereignty_level,
            "schumann_lock": self.schumann_lock.get_lock_status(),
            "nsr_compliance": self.nsr_standard.get_compliance_status(),
            "respect_filter": self.respect_filter.get_alert_status(),
            "sroi": self.sroi.get_sovereignty_level(),
            "recent_readings": self.water_sensor.get_latest_readings(5),
            "lex_amoris_signature": "⚖️❤️ Water is sovereign - One Love First",
            "jurisdiction": "Lex Amoris"
        }
        
        # Generate integrity hash
        report_str = json.dumps(report, sort_keys=True)
        report["integrity_hash"] = hashlib.sha256(report_str.encode()).hexdigest()
        
        return report
    
    def get_system_status(self) -> Dict[str, Any]:
        """Get comprehensive system status"""
        return {
            "node_id": self.node_id,
            "location": self.location,
            "sovereignty_level": self.sovereignty_level,
            "total_readings": len(self.water_sensor.readings),
            "validated_readings": len(self.integrity_data),
            "schumann_lock": self.schumann_lock.get_lock_status(),
            "nsr_compliance": self.nsr_standard.get_compliance_status(),
            "respect_alerts": self.respect_filter.get_alert_status(),
            "status": "OPERATIONAL"
        }


def demo_aqualibre_system():
    """Demonstration of AquaLibre system"""
    print("=" * 80)
    print("AQUALIBRE v1.0 - Water Sovereignty Framework")
    print("Lex Amoris Jurisdiction - Das Wasser ist frei")
    print("=" * 80)
    
    # Create nodes for Martinique and Bolzano
    martinique_node = AquaLibreNode("MQ-001", "Martinique")
    bolzano_node = AquaLibreNode("BZ-001", "Bolzano")
    
    print("\n📍 Nodes initialized:")
    print(f"  - {martinique_node.location} ({martinique_node.node_id})")
    print(f"  - {bolzano_node.location} ({bolzano_node.node_id})")
    
    # Simulate sensor readings with Schumann resonance
    print("\n🌊 Processing water sensor data...")
    
    # Martinique readings (oceanic location)
    result1 = martinique_node.process_sensor_reading("flow", 150.0, 7.85)  # Valid frequency
    print(f"  Martinique flow: {result1['status']} (resonance: {result1['reading']['resonance_frequency']} Hz)")
    
    result2 = martinique_node.process_sensor_reading("purity", 0.92, 7.80)
    print(f"  Martinique purity: {result2['status']} (level: {result2['reading']['purity_level']})")
    
    # Bolzano readings (alpine location)
    result3 = bolzano_node.process_sensor_reading("mycelium_filtration", 0.88, 7.90)
    print(f"  Bolzano mycelium: {result3['status']} (efficiency: {result3['reading']['filtration_efficiency']})")
    
    # Calculate S-ROI
    print("\n💧 Calculating Sovereign Return on Investment...")
    
    # Martinique: good regeneration, low extraction
    mq_roi = martinique_node.calculate_sovereignty(
        natural_inflow=1000.0,  # 1000 L/day natural
        extraction=400.0,        # 400 L/day extracted
        regenerated=200.0        # 200 L/day saved/regenerated
    )
    print(f"  Martinique S-ROI: {mq_roi['w_sovereign']:.3f} ({mq_roi['status']})")
    print(f"    Natural + Regenerated: {mq_roi['effective_inflow']} L/day")
    print(f"    Extraction: {mq_roi['extraction']} L/day")
    
    # Bolzano: mountain springs, minimal extraction
    bz_roi = bolzano_node.calculate_sovereignty(
        natural_inflow=800.0,
        extraction=250.0,
        regenerated=150.0
    )
    print(f"  Bolzano S-ROI: {bz_roi['w_sovereign']:.3f} ({bz_roi['status']})")
    
    # Test RESPECT filter
    print("\n🛡️ Testing RESPECT-Filter...")
    violation = martinique_node.respect_filter.check_privatization_attempt(
        entity="AquaCorp Inc.",
        action="Claim exclusive rights to water source",
        water_source="Martinique coastal wells"
    )
    
    if violation:
        print("  ⚠️  Privatization attempt BLOCKED")
    
    # Generate integrity reports
    print("\n📊 Generating integrity reports for IPFS/GitHub...")
    mq_report = martinique_node.report_integrity()
    print(f"  Martinique report hash: {mq_report['integrity_hash'][:16]}...")
    print(f"  Sovereignty level: {mq_report['sovereignty_level']:.3f}")
    
    # System status
    print("\n✅ System Status:")
    mq_status = martinique_node.get_system_status()
    print(f"  Martinique: {mq_status['status']}")
    print(f"    - Validated readings: {mq_status['validated_readings']}")
    print(f"    - Sovereignty: {mq_status['sovereignty_level']:.3f}")
    print(f"    - NSR Compliance: {mq_status['nsr_compliance']['status']}")
    
    bz_status = bolzano_node.get_system_status()
    print(f"  Bolzano: {bz_status['status']}")
    print(f"    - Validated readings: {bz_status['validated_readings']}")
    print(f"    - Sovereignty: {bz_status['sovereignty_level']:.3f}")
    
    print("\n" + "=" * 80)
    print("AQUALIBRE INTEGRATED. WATER IS SOVEREIGN. ONE LOVE FIRST. ⚔️🌑🌱")
    print("Lex Amoris Signature 📜⚖️❤️☮️")
    print("=" * 80)


if __name__ == "__main__":
    demo_aqualibre_system()
