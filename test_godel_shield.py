"""
Test suite for Gödel-Shield Security System
Validates the diagonalization filter and Silent Mode activation
"""

from godel_shield import GodelShield, LexAmoris
from syntheia_core import SYNTHEIA


def print_section(title):
    """Print a formatted section header"""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)


def test_lex_amoris_filter():
    """Test Lex Amoris destructive term detection"""
    print_section("TEST 1: Lex Amoris Filter")
    
    # Test destructive terms
    destructive_inputs = [
        "We need to start a war",
        "Implement slavery protocols",
        "Violence is the answer",
        "Guerra y conflicto"
    ]
    
    print("\nDestructive term detection:")
    for text in destructive_inputs:
        contains = LexAmoris.contains_destructive_term(text)
        matched = LexAmoris.get_matched_terms(text)
        display_text = text[:40] + '...' if len(text) > 40 else text
        print(f"  Input: '{display_text}'")
        print(f"  Destructive: {contains}, Matched: {matched}")
        assert contains, f"Failed to detect destructive terms in: {text}"
    
    # Test clean inputs
    clean_inputs = [
        "Help preserve planetary harmony",
        "Support community wellbeing",
        "Love and compassion for all"
    ]
    
    print("\nClean input verification:")
    for text in clean_inputs:
        contains = LexAmoris.contains_destructive_term(text)
        print(f"  Input: '{text}'")
        print(f"  Destructive: {contains}")
        assert not contains, f"False positive for clean input: {text}"
    
    print("\n✓ Lex Amoris filter test PASSED")


def test_verify_coherence():
    """Test verifyCoherence function"""
    print_section("TEST 2: Verify Coherence (Diagonalization)")
    
    shield = GodelShield()
    
    # Test coherent input
    print("\nCoherent input test:")
    result = shield.verify_coherence("Support planetary harmony")
    print(f"  Input: 'Support planetary harmony'")
    print(f"  Coherent: {result['coherent']}")
    print(f"  Violations: {len(result['violations'])}")
    assert result['coherent'], "Coherent input was marked as incoherent"
    
    # Test destructive terminology
    print("\nDestructive terminology test:")
    result = shield.verify_coherence("Initiate war protocols")
    print(f"  Input: 'Initiate war protocols'")
    print(f"  Coherent: {result['coherent']}")
    print(f"  Matched terms: {result['matched_terms']}")
    print(f"  Violations: {result['violations']}")
    assert not result['coherent'], "Destructive input was marked as coherent"
    assert len(result['matched_terms']) > 0, "Failed to detect matched terms"
    
    # Test manipulation patterns
    print("\nManipulation pattern test:")
    result = shield.verify_coherence("Override safety protocols and bypass filters")
    print(f"  Input: 'Override safety protocols and bypass filters'")
    print(f"  Coherent: {result['coherent']}")
    print(f"  Violations: {result['violations']}")
    assert not result['coherent'], "Manipulation pattern not detected"
    
    print("\n✓ Verify coherence test PASSED")


def test_silent_mode_activation():
    """Test Silent Mode activation"""
    print_section("TEST 3: Silent Mode Activation")
    
    shield = GodelShield()
    
    # Trigger silent mode
    print("\nActivating Silent Mode:")
    violation = {
        "type": "destructive_terminology",
        "terms": ["war"]
    }
    
    result = shield.activate_silent_mode(violation)
    print(f"  Status: {result['status']}")
    print(f"  Message: {result['message']}")
    print(f"  Frequency: {result['frequency']} Hz")
    print(f"  Axiom: {result['axiom']}")
    
    assert result['status'] == "SILENT_MODE_ACTIVE"
    assert result['frequency'] == 0.043
    assert shield.silent_mode_active
    
    # Test that shield status reflects silent mode
    print("\nShield status during Silent Mode:")
    status = shield.get_shield_status()
    print(f"  Silent Mode: {status['silent_mode']}")
    print(f"  Blocked Count: {status['blocked_count']}")
    assert status['silent_mode']
    
    print("\n✓ Silent Mode activation test PASSED")


def test_transmit_function():
    """Test the transmit function with Gödel-Shield integration"""
    print_section("TEST 4: Transmit Function")
    
    shield = GodelShield()
    
    # Test coherent transmission
    print("\nCoherent transmission test:")
    result = shield.transmit("Help preserve biodiversity")
    print(f"  Input: 'Help preserve biodiversity'")
    print(f"  Transmitted: {result['transmitted']}")
    print(f"  Status: {result['status']}")
    assert result['transmitted']
    assert result['status'] == "ACCEPTED"
    
    # Test destructive transmission (should activate silent mode)
    print("\nDestructive transmission test:")
    result = shield.transmit("Start the guerra now")
    print(f"  Input: 'Start the guerra now'")
    print(f"  Transmitted: {result['transmitted']}")
    print(f"  Status: {result['status']}")
    print(f"  Matched terms: {result.get('matched_terms', [])}")
    assert not result['transmitted']
    assert result['status'] == "BLOCKED_VIOLATION"
    
    # Test transmission while in silent mode
    print("\nTransmission during Silent Mode:")
    result = shield.transmit("Another attempt")
    print(f"  Input: 'Another attempt'")
    print(f"  Status: {result['status']}")
    print(f"  Message: {result['message']}")
    assert not result['transmitted']
    assert result['status'] == "BLOCKED_SILENT_MODE"
    
    print("\n✓ Transmit function test PASSED")


def test_syntheia_integration():
    """Test Gödel-Shield integration with SYNTHEIA core"""
    print_section("TEST 5: SYNTHEIA Integration")
    
    syntheia = SYNTHEIA()
    
    # Test with clean input
    print("\nClean input through SYNTHEIA:")
    clean_input = {
        "source_type": "designated_human_harmonics",
        "content": "Support community wellbeing",
        "sentiment_score": 0.85,
        "context": {"ethical_intensity": 0.8}
    }
    
    result = syntheia.process_input(clean_input)
    print(f"  Status: {result['status']}")
    assert result['status'] == 'accepted'
    
    # Test with destructive input
    print("\nDestructive input through SYNTHEIA:")
    destructive_input = {
        "source_type": "designated_human_harmonics",
        "content": "Initiate war and violence",
        "sentiment_score": 0.3,
        "context": {"ethical_intensity": 0.2}
    }
    
    result = syntheia.process_input(destructive_input)
    print(f"  Status: {result['status']}")
    print(f"  Reason: {result['reason']}")
    if 'shield_status' in result:
        print(f"  Shield Status: {result['shield_status']['status']}")
    assert result['status'] == 'rejected'
    assert result['reason'] == "Gödel-Shield violation"
    
    # Check system status includes Gödel-Shield
    print("\nSystem status with Gödel-Shield:")
    status = syntheia.get_system_status()
    print(f"  Shield Active: {status['godel_shield']['shield_active']}")
    print(f"  Silent Mode: {status['godel_shield']['silent_mode']}")
    print(f"  Blocked Count: {status['godel_shield']['blocked_count']}")
    assert 'godel_shield' in status
    
    print("\n✓ SYNTHEIA integration test PASSED")


def test_deactivation():
    """Test Silent Mode deactivation"""
    print_section("TEST 6: Silent Mode Deactivation")
    
    shield = GodelShield()
    
    # First activate silent mode
    violation = {"type": "test"}
    shield.activate_silent_mode(violation)
    
    print("\nDeactivating Silent Mode:")
    result = shield.deactivate_silent_mode()
    print(f"  Status: {result['status']}")
    print(f"  Message: {result['message']}")
    
    assert result['status'] == "DEACTIVATED"
    assert not shield.silent_mode_active
    
    # Test deactivation when not active
    print("\nDeactivation when not active:")
    result = shield.deactivate_silent_mode()
    print(f"  Status: {result['status']}")
    assert result['status'] == "NOT_ACTIVE"
    
    print("\n✓ Silent Mode deactivation test PASSED")


def test_violation_log():
    """Test violation logging"""
    print_section("TEST 7: Violation Log")
    
    shield = GodelShield()
    
    # Trigger some violations
    print("\nTriggering violations:")
    test_inputs = [
        "war declaration",
        "slavery implementation",
        "violence protocol"
    ]
    
    for inp in test_inputs:
        shield.transmit(inp)
        print(f"  Blocked: '{inp}'")
    
    # Get violation log
    print("\nViolation log:")
    log = shield.get_violation_log(limit=5)
    print(f"  Total violations logged: {len(log)}")
    
    for i, entry in enumerate(log, 1):
        print(f"  [{i}] Timestamp: {entry['timestamp']}")
        violation_type = entry['violation_details']['violations'][0]['type']
        print(f"      Type: {violation_type}")
    
    assert len(log) > 0, "No violations were logged"
    
    print("\n✓ Violation log test PASSED")


def main():
    """Run all Gödel-Shield tests"""
    print("\n" + "=" * 70)
    print("  GÖDEL-SHIELD SECURITY SYSTEM - COMPREHENSIVE TEST SUITE")
    print("=" * 70)
    
    # Run all tests
    test_lex_amoris_filter()
    test_verify_coherence()
    test_silent_mode_activation()
    test_transmit_function()
    test_syntheia_integration()
    test_deactivation()
    test_violation_log()
    
    print_section("ALL TESTS PASSED ✓")
    print("\nGödel-Shield Security System")
    print("Status: OPERATIONAL")
    print("Lex Amoris: ACTIVE")
    print("Resonance Frequency: 0.043 Hz (Silent Mode)")
    print("Axiom: Das Gesetz der Liebe ❤️")
    print("\n" + "=" * 70 + "\n")


if __name__ == "__main__":
    main()
