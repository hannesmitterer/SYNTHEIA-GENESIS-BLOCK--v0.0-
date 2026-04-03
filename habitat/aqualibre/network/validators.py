"""
AquaLibre Network Protocol - Validation Engines
NSRValidator, ReciprocityFilter, CooperationEngine
"""

from typing import Dict, Any, List
from datetime import datetime


class Action:
    """Represents an action to be validated in the network"""
    
    def __init__(self, node_id: str, action_type: str, **kwargs):
        self.node_id = node_id
        self.action_type = action_type
        self.timestamp = datetime.now().isoformat()
        self.data = kwargs
        
        # Computed properties
        self.requires_external_permission = kwargs.get("requires_external_permission", False)
        self.creates_dependency = kwargs.get("creates_dependency", False)
        self.benefit_self = kwargs.get("benefit_self", 0.0)
        self.benefit_others = kwargs.get("benefit_others", 0.0)
    
    def to_dict(self) -> Dict[str, Any]:
        """Export action as dictionary"""
        return {
            "node_id": self.node_id,
            "action_type": self.action_type,
            "timestamp": self.timestamp,
            **self.data
        }


class NSRValidator:
    """
    No Secret Revenue / NSR Validator
    Anti-Coercion: Prevents external control and dependencies
    """
    
    def __init__(self):
        self.violations: List[Dict[str, Any]] = []
    
    def validate(self, action: Action) -> bool:
        """Validate action against NSR principles"""
        violations = []
        
        if action.requires_external_permission:
            violations.append({"type": "external_permission", "message": "Requires external permission"})
        
        if action.creates_dependency:
            violations.append({"type": "forced_dependency", "message": "Creates forced dependency"})
        
        if violations:
            self.violations.append({
                "timestamp": datetime.now().isoformat(),
                "action": action.to_dict(),
                "violations": violations
            })
            return False
        
        return True


class ReciprocityFilter:
    """Lex Amoris - Reciprocity Filter"""
    
    def __init__(self):
        self.violations: List[Dict[str, Any]] = []
        self.min_reciprocity_ratio = 0.5
    
    def validate(self, action: Action) -> bool:
        """Validate action for reciprocity"""
        violations = []
        
        if action.benefit_self > 0 and action.benefit_others == 0:
            violations.append({"type": "asymmetric_benefit", "message": "Benefits only self"})
        
        if action.action_type == "water_extraction":
            extraction = action.data.get("extraction", 0)
            recharge = action.data.get("recharge", 0)
            
            if extraction > 0:
                reciprocity_ratio = recharge / extraction
                
                if reciprocity_ratio < self.min_reciprocity_ratio:
                    violations.append({"type": "low_reciprocity", "ratio": reciprocity_ratio})
        
        if violations:
            self.violations.append({
                "timestamp": datetime.now().isoformat(),
                "action": action.to_dict(),
                "violations": violations
            })
            return False
        
        return True


class CooperationEngine:
    """One Love - Cooperation Engine"""
    
    def __init__(self):
        self.scores: Dict[str, float] = {}
        self.cooperation_history: Dict[str, List[Dict[str, Any]]] = {}
    
    def score(self, node_id: str, metrics: Dict[str, float]) -> float:
        """Calculate cooperation score"""
        shared_data_ratio = metrics.get("shared_data_ratio", 0.0)
        water_regeneration = metrics.get("water_regeneration", 0.0)
        network_contribution = metrics.get("network_contribution", 0.0)
        
        score = (
            shared_data_ratio * 0.4 +
            water_regeneration * 0.4 +
            network_contribution * 0.2
        )
        
        score = max(0.0, min(1.0, score))
        self.scores[node_id] = score
        
        return score
    
    def get_trust_level(self, node_id: str) -> str:
        """Determine trust level"""
        if node_id not in self.scores:
            return "UNKNOWN"
        
        score = self.scores[node_id]
        if score >= 0.8:
            return "HIGH_TRUST"
        elif score >= 0.6:
            return "MODERATE_TRUST"
        elif score >= 0.4:
            return "LOW_TRUST"
        else:
            return "UNTRUSTED"
    
    def is_reference_node(self, node_id: str, threshold: float = 0.75) -> bool:
        """Check if node qualifies as reference node"""
        if node_id not in self.scores:
            return False
        return self.scores[node_id] >= threshold
