"""
AquaLibre Network Layer Tests
Tests for identity, validators, consensus, and protocol
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'habitat/aqualibre/network'))

from identity import NodeIdentity, NodeState, TimeAveragedMetrics
from validators import Action, NSRValidator, ReciprocityFilter, CooperationEngine
from consensus import DistributedConsensus, GameTheoryValidator


def test_node_identity():
    """Test cryptographic node identity"""
    print("Testing NodeIdentity...")
    
    # Create identity
    identity = NodeIdentity("TEST-001")
    assert identity.node_id == "TEST-001"
    assert len(identity.public_key) == 64
    assert len(identity.identity_hash) == 64
    
    # Test signing
    payload = {"test": "data", "value": 123}
    signature = identity.sign(payload)
    assert len(signature) == 64
    
    # Test verification
    is_valid = identity.verify(payload, signature)
    assert is_valid == True, "Signature should verify"
    
    # Test tampered payload
    tampered = {"test": "data", "value": 999}
    is_valid_tampered = identity.verify(tampered, signature)
    assert is_valid_tampered == False, "Tampered payload should not verify"
    
    print("  ✓ NodeIdentity test PASSED")


def test_node_state():
    """Test weighted node state"""
    print("Testing NodeState...")
    
    state = NodeState(water_capacity=1000.0, reliability=0.9)
    assert state.water_capacity == 1000.0
    assert state.reliability == 0.9
    assert state.get_weight() == 900.0
    
    # Test reliability update
    state.update_reliability(80, 100)
    assert state.reliability >= 0.76, "Reliability should update based on weighted average"
    
    # Test uptime recording
    for i in range(20):  # Need more records to affect reliability
        state.record_uptime(True)
    # Reliability should stay high or improve slightly with good uptime
    assert state.reliability >= 0.75, "Good uptime should maintain high reliability"
    
    print("  ✓ NodeState test PASSED")


def test_time_averaged_metrics():
    """Test time-averaged metrics"""
    print("Testing TimeAveragedMetrics...")
    
    metrics = TimeAveragedMetrics(window_size=10)
    
    # Record some metrics
    for i in range(15):
        metrics.record_metric("extraction", 100 + i * 10)
        metrics.record_metric("recharge", 150 - i * 5)
    
    # Test rolling average
    ext_avg = metrics.rolling_average("extraction")
    assert ext_avg > 100, "Average should be calculated"
    
    # Test trend
    ext_trend = metrics.get_trend("extraction")
    assert ext_trend == "IMPROVING", f"Expected IMPROVING, got {ext_trend}"
    
    rech_trend = metrics.get_trend("recharge")
    assert rech_trend == "DECLINING", f"Expected DECLINING, got {rech_trend}"
    
    print("  ✓ TimeAveragedMetrics test PASSED")


def test_nsr_validator():
    """Test NSR Validator"""
    print("Testing NSRValidator...")
    
    nsr = NSRValidator()
    
    # Test valid autonomous action
    valid = Action("TEST-001", "water_extraction",
                  requires_external_permission=False,
                  creates_dependency=False)
    assert nsr.validate(valid) == True, "Autonomous action should pass"
    
    # Test invalid action (requires permission)
    invalid = Action("TEST-001", "water_extraction",
                    requires_external_permission=True)
    assert nsr.validate(invalid) == False, "Permission-requiring action should fail"
    
    print("  ✓ NSRValidator test PASSED")


def test_reciprocity_filter():
    """Test Reciprocity Filter"""
    print("Testing ReciprocityFilter...")
    
    recip = ReciprocityFilter()
    
    # Test valid reciprocal action
    valid = Action("TEST-001", "water_extraction",
                  extraction=100, recharge=150,
                  benefit_self=1.0, benefit_others=1.5)
    assert recip.validate(valid) == True, "Reciprocal action should pass"
    
    # Test invalid one-sided action
    invalid = Action("TEST-001", "water_extraction",
                    extraction=200, recharge=50,
                    benefit_self=1.0, benefit_others=0.0)
    assert recip.validate(invalid) == False, "One-sided action should fail"
    
    print("  ✓ ReciprocityFilter test PASSED")


def test_cooperation_engine():
    """Test Cooperation Engine"""
    print("Testing CooperationEngine...")
    
    coop = CooperationEngine()
    
    # Test high cooperation score
    high_metrics = {
        "shared_data_ratio": 0.9,
        "water_regeneration": 0.85,
        "network_contribution": 0.8
    }
    high_score = coop.score("TEST-001", high_metrics)
    assert high_score >= 0.8, f"High cooperation should score >= 0.8, got {high_score}"
    assert coop.get_trust_level("TEST-001") == "HIGH_TRUST"
    
    # Test low cooperation score
    low_metrics = {
        "shared_data_ratio": 0.2,
        "water_regeneration": 0.3,
        "network_contribution": 0.1
    }
    low_score = coop.score("TEST-002", low_metrics)
    assert low_score < 0.4, f"Low cooperation should score < 0.4, got {low_score}"
    
    # Test reference node
    assert coop.is_reference_node("TEST-001") == True, "High score should be reference node"
    assert coop.is_reference_node("TEST-002") == False, "Low score should not be reference node"
    
    print("  ✓ CooperationEngine test PASSED")


def test_game_theory_validator():
    """Test Game Theory Validator"""
    print("Testing GameTheoryValidator...")
    
    game = GameTheoryValidator()
    
    # Test low extraction cost (balanced)
    result1 = game.should_limit_access("TEST-001", extraction=100, recharge=150)
    assert result1["should_limit"] == False, "Balanced extraction should not limit"
    assert result1["status"] == "FULL_ACCESS"
    
    # Test high extraction cost (extractive)
    result2 = game.should_limit_access("TEST-002", extraction=300, recharge=50)
    assert result2["should_limit"] == True, "High extraction should limit"
    assert result2["status"] == "LIMITED_ACCESS"
    
    print("  ✓ GameTheoryValidator test PASSED")


def test_distributed_consensus():
    """Test distributed consensus"""
    print("Testing DistributedConsensus...")
    
    consensus = DistributedConsensus()
    
    # Register validators
    nsr = NSRValidator()
    recip = ReciprocityFilter()
    consensus.register_validator(nsr)
    consensus.register_validator(recip)
    
    # Test consensus on valid action
    valid_action = Action("TEST-001", "water_extraction",
                         extraction=100, recharge=150,
                         requires_external_permission=False,
                         benefit_self=1.0, benefit_others=1.5)
    
    decision = consensus.validate_distributed(valid_action)
    assert decision["consensus"] == True, "Valid action should reach consensus"
    assert decision["consensus_ratio"] >= 0.66, "Consensus ratio should be >= 66%"
    
    # Test consensus on invalid action
    invalid_action = Action("TEST-001", "water_extraction",
                           requires_external_permission=True,
                           benefit_self=1.0, benefit_others=0.0)
    
    decision2 = consensus.validate_distributed(invalid_action)
    assert decision2["consensus"] == False, "Invalid action should not reach consensus"
    
    print("  ✓ DistributedConsensus test PASSED")


def test_complete_protocol():
    """Test complete protocol pipeline"""
    print("Testing Complete Protocol...")
    
    # Import protocol here to avoid circular imports
    sys.path.insert(0, os.path.dirname(__file__))
    from habitat.aqualibre.network.protocol_test import AquaLibreProtocol
    
    # Create protocol
    identity = NodeIdentity("TEST-001")
    state = NodeState(water_capacity=1000.0, reliability=0.95)
    protocol = AquaLibreProtocol(identity, state)
    
    # Test valid action
    valid = Action("TEST-001", "water_extraction",
                  extraction=100, recharge=150,
                  requires_external_permission=False,
                  creates_dependency=False,
                  benefit_self=1.0, benefit_others=1.5)
    
    metrics = {
        "shared_data_ratio": 0.9,
        "water_regeneration": 0.8,
        "network_contribution": 0.7
    }
    
    result = protocol.process_action(valid, metrics)
    assert result["status"] == "ACCEPTED", "Valid action should be accepted"
    assert "cooperation_score" in result
    assert result["cooperation_score"] > 0.7
    
    # Test NSR violation
    nsr_violation = Action("TEST-001", "water_extraction",
                          requires_external_permission=True)
    result2 = protocol.process_action(nsr_violation)
    assert result2["status"] == "REJECTED"
    assert result2["reason"] == "NSR_VIOLATION"
    
    # Test reciprocity violation
    recip_violation = Action("TEST-001", "water_extraction",
                            extraction=200, recharge=50,
                            benefit_self=1.0, benefit_others=0.0)
    result3 = protocol.process_action(recip_violation)
    assert result3["status"] == "REJECTED"
    assert result3["reason"] == "RECIPROCITY_VIOLATION"
    
    print("  ✓ Complete Protocol test PASSED")


def run_all_tests():
    """Run all network tests"""
    print("=" * 80)
    print("AQUALIBRE NETWORK LAYER TESTS")
    print("=" * 80)
    print()
    
    tests = [
        test_node_identity,
        test_node_state,
        test_time_averaged_metrics,
        test_nsr_validator,
        test_reciprocity_filter,
        test_cooperation_engine,
        test_game_theory_validator,
        test_distributed_consensus,
        test_complete_protocol
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"  ✗ {test.__name__} FAILED: {e}")
            failed += 1
        except Exception as e:
            print(f"  ✗ {test.__name__} ERROR: {e}")
            failed += 1
    
    print()
    print("=" * 80)
    print(f"RESULTS: {passed} passed, {failed} failed")
    print("=" * 80)
    
    if failed == 0:
        print("\n✅ ALL NETWORK TESTS PASSED")
        print("NETWORK LAYER OPERATIONAL ⚔️🌑🌱")
        print("Lex Amoris Signature 📜⚖️❤️☮️")
        return 0
    else:
        print("\n❌ SOME TESTS FAILED")
        return 1


if __name__ == "__main__":
    exit_code = run_all_tests()
    exit(exit_code)
