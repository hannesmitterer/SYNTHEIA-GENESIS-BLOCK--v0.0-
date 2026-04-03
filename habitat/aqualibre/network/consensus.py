"""
AquaLibre Network Protocol - Distributed Consensus
No central gatekeeper, but collective decision-making
"""

from typing import Dict, Any, List, Callable
from datetime import datetime


class DistributedConsensus:
    """
    Distributed consensus mechanism
    Decisions made collectively without central authority
    """
    
    CONSENSUS_THRESHOLD = 0.66  # 66% agreement required
    
    def __init__(self):
        self.validators: List[Any] = []
        self.decisions: List[Dict[str, Any]] = []
    
    def register_validator(self, validator):
        """Register a validator node"""
        if validator not in self.validators:
            self.validators.append(validator)
    
    def validate_distributed(self, action: Any, weight_func: Callable = None) -> Dict[str, Any]:
        """
        Validate action through distributed consensus
        
        Args:
            action: Action to validate
            weight_func: Optional function to weight votes (e.g., by node reliability)
        
        Returns:
            Dictionary with consensus result
        """
        if not self.validators:
            return {
                "consensus": False,
                "reason": "NO_VALIDATORS",
                "votes": []
            }
        
        votes = []
        total_weight = 0
        approve_weight = 0
        
        for validator in self.validators:
            vote = validator.validate(action)
            weight = 1.0
            
            if weight_func and hasattr(validator, 'get_weight'):
                weight = weight_func(validator)
            
            votes.append({
                "validator": str(validator),
                "vote": vote,
                "weight": weight
            })
            
            total_weight += weight
            if vote:
                approve_weight += weight
        
        # Calculate weighted consensus
        if total_weight > 0:
            consensus_ratio = approve_weight / total_weight
        else:
            consensus_ratio = 0.0
        
        has_consensus = consensus_ratio >= self.CONSENSUS_THRESHOLD
        
        decision = {
            "timestamp": datetime.now().isoformat(),
            "action": action.to_dict() if hasattr(action, 'to_dict') else str(action),
            "consensus": has_consensus,
            "consensus_ratio": consensus_ratio,
            "threshold": self.CONSENSUS_THRESHOLD,
            "total_validators": len(self.validators),
            "approve_votes": sum(1 for v in votes if v["vote"]),
            "reject_votes": sum(1 for v in votes if not v["vote"]),
            "votes": votes
        }
        
        self.decisions.append(decision)
        
        return decision
    
    def get_decision_history(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Get recent consensus decisions"""
        return self.decisions[-limit:]


class GameTheoryValidator:
    """
    Game theory checks - prevents gaming the system
    Makes exploitation automatically unattractiv

e
    """
    
    EXTRACTION_COST_THRESHOLD = 2.0  # Max extraction cost before limitation
    
    def __init__(self):
        self.cost_history: Dict[str, List[float]] = {}
    
    def calculate_extraction_cost(self, node_id: str, extraction: float, recharge: float) -> float:
        """
        Calculate cost of extraction
        Higher cost = more extractive behavior
        """
        if recharge == 0:
            recharge = 0.001  # Prevent division by zero
        
        cost = extraction / (recharge + 1)
        
        # Record in history
        if node_id not in self.cost_history:
            self.cost_history[node_id] = []
        
        self.cost_history[node_id].append(cost)
        
        # Keep only last 100
        if len(self.cost_history[node_id]) > 100:
            self.cost_history[node_id] = self.cost_history[node_id][-100:]
        
        return cost
    
    def should_limit_access(self, node_id: str, extraction: float, recharge: float) -> Dict[str, Any]:
        """
        Determine if node access should be limited due to high extraction cost
        """
        cost = self.calculate_extraction_cost(node_id, extraction, recharge)
        
        # Calculate average cost
        avg_cost = sum(self.cost_history[node_id]) / len(self.cost_history[node_id]) if self.cost_history.get(node_id) else cost
        
        should_limit = cost > self.EXTRACTION_COST_THRESHOLD
        
        return {
            "node_id": node_id,
            "current_cost": cost,
            "average_cost": avg_cost,
            "threshold": self.EXTRACTION_COST_THRESHOLD,
            "should_limit": should_limit,
            "extraction": extraction,
            "recharge": recharge,
            "status": "LIMITED_ACCESS" if should_limit else "FULL_ACCESS"
        }
    
    def get_node_behavior_analysis(self, node_id: str) -> Dict[str, Any]:
        """Analyze node behavior pattern"""
        if node_id not in self.cost_history or not self.cost_history[node_id]:
            return {"status": "INSUFFICIENT_DATA"}
        
        costs = self.cost_history[node_id]
        avg_cost = sum(costs) / len(costs)
        
        # Determine behavior pattern
        if avg_cost < 0.5:
            pattern = "HIGHLY_REGENERATIVE"
        elif avg_cost < 1.0:
            pattern = "BALANCED"
        elif avg_cost < 2.0:
            pattern = "EXTRACTIVE"
        else:
            pattern = "HIGHLY_EXTRACTIVE"
        
        return {
            "node_id": node_id,
            "average_cost": avg_cost,
            "pattern": pattern,
            "records": len(costs),
            "recent_trend": "IMPROVING" if len(costs) > 5 and costs[-1] < costs[-5] else "STABLE"
        }
