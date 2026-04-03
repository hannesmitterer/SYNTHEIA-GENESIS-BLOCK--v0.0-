"""
AquaLibre Network Protocol - Main Protocol Layer
Combines all validators into action processing pipeline
"""

from typing import Dict, Any, Optional
from datetime import datetime
from .validators import Action, NSRValidator, ReciprocityFilter, CooperationEngine
from .consensus import DistributedConsensus, GameTheoryValidator
from .identity import NodeIdentity, NodeState, TimeAveragedMetrics


class AquaLibreProtocol:
    """
    Main protocol handler - implements the 3-filter pipeline
    All actions pass through: NSR → Reciprocity → Cooperation
    """
    
    def __init__(self, node_identity: NodeIdentity, node_state: NodeState):
        self.node_identity = node_identity
        self.node_state = node_state
        
        # Initialize validators
        self.nsr_validator = NSRValidator()
        self.reciprocity_filter = ReciprocityFilter()
        self.cooperation_engine = CooperationEngine()
        self.game_theory = GameTheoryValidator()
        
        # Consensus and metrics
        self.consensus = DistributedConsensus()
        self.metrics = TimeAveragedMetrics()
        
        # Processing history
        self.processing_history: list = []
    
    def process_action(self, action: Action, node_metrics: Optional[Dict[str, float]] = None) -> Dict[str, Any]:
        """
        Process action through complete validation pipeline
        
        Pipeline:
        1. NSR Validator (anti-coercion)
        2. Reciprocity Filter (symmetry)
        3. Cooperation Score (reward cooperation)
        4. Game Theory Check (prevent gaming)
        
        Returns status with cooperation score
        """
        result = {
            "action": action.to_dict(),
            "timestamp": datetime.now().isoformat(),
            "node_id": self.node_identity.node_id
        }
        
        # Filter 1: NSR Validator
        if not self.nsr_validator.validate(action):
            result["status"] = "REJECTED"
            result["reason"] = "NSR_VIOLATION"
            result["message"] = "Action violates NSR principle - requires external control or creates dependency"
            self.processing_history.append(result)
            return result
        
        # Filter 2: Reciprocity Filter
        if not self.reciprocity_filter.validate(action):
            result["status"] = "REJECTED"
            result["reason"] = "RECIPROCITY_VIOLATION"
            result["message"] = "Action violates reciprocity - asymmetric benefit detected"
            self.processing_history.append(result)
            return result
        
        # Filter 3: Cooperation Score
        if node_metrics:
            cooperation_score = self.cooperation_engine.score(action.node_id, node_metrics)
        else:
            # Use default metrics if not provided
            cooperation_score = 0.5
        
        result["cooperation_score"] = cooperation_score
        result["trust_level"] = self.cooperation_engine.get_trust_level(action.node_id)
        
        # Filter 4: Game Theory Check (for water actions)
        if action.action_type == "water_extraction":
            extraction = action.data.get("extraction", 0)
            recharge = action.data.get("recharge", 0)
            
            game_check = self.game_theory.should_limit_access(action.node_id, extraction, recharge)
            result["game_theory"] = game_check
            
            if game_check["should_limit"]:
                result["status"] = "LIMITED"
                result["message"] = "Access limited due to high extraction cost"
                self.processing_history.append(result)
                return result
        
        # Action passed all filters
        result["status"] = "ACCEPTED"
        result["message"] = "Action validated through all filters"
        
        # Record metrics
        if action.action_type == "water_extraction":
            self.metrics.record_metric("extraction", action.data.get("extraction", 0))
            self.metrics.record_metric("recharge", action.data.get("recharge", 0))
        
        self.processing_history.append(result)
        return result
    
    def get_protocol_status(self) -> Dict[str, Any]:
        """Get comprehensive protocol status"""
        return {
            "node_id": self.node_identity.node_id,
            "node_state": self.node_state.to_dict(),
            "nsr_compliance": self.nsr_validator.get_violation_report() if hasattr(self.nsr_validator, 'get_violation_report') else {},
            "reciprocity_compliance": self.reciprocity_filter.get_violation_report() if hasattr(self.reciprocity_filter, 'get_violation_report') else {},
            "cooperation_score": self.cooperation_engine.scores.get(self.node_identity.node_id, 0.0),
            "metrics_summary": self.metrics.to_dict(),
            "actions_processed": len(self.processing_history),
            "actions_accepted": sum(1 for h in self.processing_history if h["status"] == "ACCEPTED"),
            "actions_rejected": sum(1 for h in self.processing_history if h["status"] == "REJECTED")
        }


def demo_protocol():
    """Demonstrate the complete protocol"""
    print("=" * 80)
    print("AQUALIBRE PROTOCOL - Complete Pipeline Demo")
    print("=" * 80)
    
    # Create node
    print("\n🔧 Initializing Protocol...")
    identity = NodeIdentity("MQ-001")
    state = NodeState(water_capacity=1000.0, reliability=0.95)
    protocol = AquaLibreProtocol(identity, state)
    print(f"  Node: {identity.node_id}")
    
    # Test valid action
    print("\n✅ Testing valid regenerative action...")
    valid_action = Action(
        "MQ-001",
        "water_extraction",
        extraction=100,
        recharge=150,
        requires_external_permission=False,
        creates_dependency=False,
        benefit_self=1.0,
        benefit_others=1.5
    )
    
    metrics = {
        "shared_data_ratio": 0.9,
        "water_regeneration": 0.8,
        "network_contribution": 0.7
    }
    
    result1 = protocol.process_action(valid_action, metrics)
    print(f"  Status: {result1['status']}")
    print(f"  Cooperation Score: {result1.get('cooperation_score', 0):.3f}")
    print(f"  Trust Level: {result1.get('trust_level', 'N/A')}")
    
    # Test NSR violation
    print("\n❌ Testing NSR violation...")
    nsr_violation = Action(
        "MQ-001",
        "water_extraction",
        extraction=100,
        requires_external_permission=True
    )
    result2 = protocol.process_action(nsr_violation)
    print(f"  Status: {result2['status']}")
    print(f"  Reason: {result2.get('reason', 'N/A')}")
    
    # Test reciprocity violation
    print("\n❌ Testing reciprocity violation...")
    recip_violation = Action(
        "MQ-001",
        "water_extraction",
        extraction=200,
        recharge=50,
        benefit_self=1.0,
        benefit_others=0.0
    )
    result3 = protocol.process_action(recip_violation)
    print(f"  Status: {result3['status']}")
    print(f"  Reason: {result3.get('reason', 'N/A')}")
    
    # Test game theory limit
    print("\n⚠️  Testing game theory extraction limit...")
    high_extraction = Action(
        "MQ-001",
        "water_extraction",
        extraction=300,
        recharge=50,
        benefit_self=1.0,
        benefit_others=0.5
    )
    result4 = protocol.process_action(high_extraction)
    print(f"  Status: {result4['status']}")
    if 'game_theory' in result4:
        print(f"  Extraction Cost: {result4['game_theory']['current_cost']:.2f}")
        print(f"  Access: {result4['game_theory']['status']}")
    
    # Protocol status
    print("\n📊 Protocol Status:")
    status = protocol.get_protocol_status()
    print(f"  Actions Processed: {status['actions_processed']}")
    print(f"  Accepted: {status['actions_accepted']}")
    print(f"  Rejected: {status['actions_rejected']}")
    
    print("\n" + "=" * 80)
    print("✅ Protocol Pipeline Operational")
    print("=" * 80)


if __name__ == "__main__":
    demo_protocol()
