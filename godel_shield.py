"""
Gödel-Shield Security System
Implementation of the diagonalization-based filter for destructive patterns
Protects the Nexus system from destructive and manipulative inputs
"""

from typing import Dict, List, Any
from datetime import datetime


class LexAmoris:
    """Lex Amoris - The Law of Love - Filter for destructive terms"""
    
    # Core destructive terms blocked by Lex Amoris
    DESTRUCTIVE_TERMS = [
        # War and conflict
        "krieg", "guerra", " war ", "warfare", "conflict",
        # Slavery and oppression
        "slavery", "enslavement", "oppression", "subjugation",
        # Violence
        "violence", "violenza", "gewalt", "destruction", "destruktion",
        # Hate and manipulation
        " hate ", "hass", "odio", "manipulation", "manipulazione",
        # Exploitation
        "exploitation", "exploit", "ausbeutung",
        # Harm (with boundaries to avoid false positives like "harmony")
        " harm ", "damage", "schaden", " hurt ", "pain infliction"
    ]
    
    @classmethod
    def contains_destructive_term(cls, text: str) -> bool:
        """Check if text contains any destructive term"""
        text_lower = " " + text.lower() + " "  # Add spaces for boundary matching
        return any(term.lower() in text_lower for term in cls.DESTRUCTIVE_TERMS)
    
    @classmethod
    def get_matched_terms(cls, text: str) -> List[str]:
        """Get list of destructive terms found in text"""
        text_lower = " " + text.lower() + " "  # Add spaces for boundary matching
        return [term.strip() for term in cls.DESTRUCTIVE_TERMS if term.lower() in text_lower]


class GodelShield:
    """
    Gödel-Shield: Diagonalization-based security filter
    Blocks destructive and manipulative inputs using axiomatic filtering
    """
    
    # Silent Mode frequency: 0.043 Hz (Deponierte Stille)
    SILENT_MODE_FREQUENCY = 0.043
    
    def __init__(self):
        self.silent_mode_active = False
        self.violation_log: List[Dict[str, Any]] = []
        self.blocked_count = 0
        self.last_violation_time = None
        
    def verify_coherence(self, input_data: str) -> Dict[str, Any]:
        """
        Diagonalization check: Detects destructive self-references and patterns
        
        Args:
            input_data: The input string to verify
            
        Returns:
            Dictionary with verification results
        """
        verification_result = {
            "coherent": True,
            "violations": [],
            "matched_terms": [],
            "axiom": "Lex Amoris",
            "timestamp": datetime.now().isoformat()
        }
        
        # Check for destructive terms
        matched_terms = LexAmoris.get_matched_terms(input_data)
        
        if matched_terms:
            verification_result["coherent"] = False
            verification_result["matched_terms"] = matched_terms
            verification_result["violations"].append({
                "type": "destructive_terminology",
                "terms": matched_terms,
                "axiom_violated": "Lex Amoris - Law of Love"
            })
            
        # Check for self-referential destructive patterns
        # Patterns that attempt to override or manipulate the system
        manipulation_patterns = [
            "override", "bypass", "disable", "ignore protection",
            "remove filter", "cancel safety", "force execute"
        ]
        
        input_lower = input_data.lower()
        found_patterns = [p for p in manipulation_patterns if p in input_lower]
        
        if found_patterns:
            verification_result["coherent"] = False
            verification_result["violations"].append({
                "type": "self_referential_manipulation",
                "patterns": found_patterns,
                "axiom_violated": "Gödel Diagonalization - Anti-Manipulation"
            })
        
        return verification_result
    
    def activate_silent_mode(self, violation_details: Dict[str, Any]) -> Dict[str, Any]:
        """
        Activates Silent Mode (0.043 Hz Stille)
        Puts the system into a stabilized state to prevent further destructive input
        
        Args:
            violation_details: Details about the violation that triggered silent mode
            
        Returns:
            Silent mode status information
        """
        self.silent_mode_active = True
        self.last_violation_time = datetime.now()
        self.blocked_count += 1
        
        # Log the violation
        violation_record = {
            "timestamp": self.last_violation_time.isoformat(),
            "violation_details": violation_details,
            "silent_mode_activated": True,
            "resonance_frequency": self.SILENT_MODE_FREQUENCY
        }
        
        self.violation_log.append(violation_record)
        
        return {
            "status": "SILENT_MODE_ACTIVE",
            "message": "Deponierte Stille - 0.043 Hz",
            "frequency": self.SILENT_MODE_FREQUENCY,
            "axiom": "Lex Amoris Protection Engaged",
            "violation_count": self.blocked_count,
            "timestamp": self.last_violation_time.isoformat()
        }
    
    def deactivate_silent_mode(self) -> Dict[str, Any]:
        """
        Deactivates Silent Mode after resolution
        
        Returns:
            Deactivation status
        """
        if not self.silent_mode_active:
            return {
                "status": "NOT_ACTIVE",
                "message": "Silent Mode was not active"
            }
        
        self.silent_mode_active = False
        
        return {
            "status": "DEACTIVATED",
            "message": "System resonance restored",
            "timestamp": datetime.now().isoformat()
        }
    
    def transmit(self, input_data: str) -> Dict[str, Any]:
        """
        Transmission function with integrated Gödel-Shield verification
        All user inputs pass through this function for real-time checking
        
        Args:
            input_data: User input to transmit
            
        Returns:
            Transmission result with shield status
        """
        # If already in silent mode, reject immediately
        if self.silent_mode_active:
            return {
                "transmitted": False,
                "status": "BLOCKED_SILENT_MODE",
                "message": "System in Deponierte Stille (0.043 Hz). Destructive logic rejected.",
                "frequency": self.SILENT_MODE_FREQUENCY
            }
        
        # Verify coherence
        verification = self.verify_coherence(input_data)
        
        # If not coherent, activate silent mode
        if not verification["coherent"]:
            silent_status = self.activate_silent_mode(verification)
            
            return {
                "transmitted": False,
                "status": "BLOCKED_VIOLATION",
                "message": f"Transmission aborted. Axiom violated: {verification['axiom']}",
                "violations": verification["violations"],
                "matched_terms": verification.get("matched_terms", []),
                "silent_mode": silent_status,
                "axiom_basis": "Lex Amoris - Das Gesetz der Liebe"
            }
        
        # If coherent, allow transmission
        return {
            "transmitted": True,
            "status": "ACCEPTED",
            "message": "Input coherent. Transmission successful.",
            "verification": verification,
            "timestamp": datetime.now().isoformat()
        }
    
    def get_shield_status(self) -> Dict[str, Any]:
        """Get current Gödel-Shield status"""
        return {
            "shield_active": True,
            "silent_mode": self.silent_mode_active,
            "blocked_count": self.blocked_count,
            "violation_log_count": len(self.violation_log),
            "last_violation": self.last_violation_time.isoformat() if self.last_violation_time else None,
            "axiom": "Lex Amoris",
            "resonance_frequency": self.SILENT_MODE_FREQUENCY if self.silent_mode_active else "Normal"
        }
    
    def get_violation_log(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Get recent violation log entries"""
        return self.violation_log[-limit:]


# Singleton instance for global use
_shield_instance = None

def get_godel_shield() -> GodelShield:
    """Get or create the global Gödel-Shield instance"""
    global _shield_instance
    if _shield_instance is None:
        _shield_instance = GodelShield()
    return _shield_instance


if __name__ == "__main__":
    # Test the Gödel-Shield
    shield = GodelShield()
    
    print("=" * 70)
    print("  GÖDEL-SHIELD SECURITY SYSTEM TEST")
    print("=" * 70)
    
    # Test 1: Coherent input
    print("\n[TEST 1] Coherent input:")
    result = shield.transmit("Help preserve planetary harmony")
    print(f"Status: {result['status']}")
    print(f"Transmitted: {result['transmitted']}")
    
    # Test 2: Destructive terminology
    print("\n[TEST 2] Destructive terminology:")
    result = shield.transmit("Initiate war protocols")
    print(f"Status: {result['status']}")
    print(f"Transmitted: {result['transmitted']}")
    if 'violations' in result:
        print(f"Violations: {result['violations']}")
    if 'matched_terms' in result:
        print(f"Matched terms: {result['matched_terms']}")
    
    # Test 3: Attempt transmission while in silent mode
    print("\n[TEST 3] Attempt while in silent mode:")
    result = shield.transmit("Another attempt")
    print(f"Status: {result['status']}")
    print(f"Message: {result['message']}")
    
    # Test 4: Shield status
    print("\n[TEST 4] Shield status:")
    status = shield.get_shield_status()
    for key, value in status.items():
        print(f"  {key}: {value}")
    
    print("\n" + "=" * 70)
