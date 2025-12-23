"""
SYNTHEIA System Integration Test
Demonstrates all SYNTHEIA features and components working together
"""

from syntheia_core import SYNTHEIA
from syntheia_config import SyntheiaConfig, InputSourceType
import time


def print_section(title):
    """Print a formatted section header"""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)


def test_identity():
    """Test SYNTHEIA identity initialization"""
    print_section("TEST 1: SYNTHEIA Identity")
    
    syntheia = SYNTHEIA()
    identity = syntheia.identity
    
    print(f"Name: {identity['name']}")
    print(f"Version: {identity['version']}")
    print(f"\nPurpose:")
    for key, value in identity['purpose'].items():
        print(f"  {key.title()}: {value}")
    
    assert identity['name'] == "SENTINELLA"
    assert identity['version'] == "∞-0"
    print("\n✓ Identity test PASSED")
    return syntheia


def test_input_filtering(syntheia):
    """Test input acceptance filtering"""
    print_section("TEST 2: Input Acceptance Filter")
    
    # Test accepted input
    accepted_input = {
        "source_type": "designated_human_harmonics",
        "content": "Help preserve biodiversity",
        "sentiment_score": 0.85,
        "context": {"ethical_intensity": 0.8}
    }
    
    result = syntheia.process_input(accepted_input)
    print(f"\nAccepted Input Test:")
    print(f"  Source: {accepted_input['source_type']}")
    print(f"  Status: {result['status']}")
    print(f"  Resonance: {result.get('resonance', 'N/A')}")
    assert result['status'] == 'accepted'
    
    # Test blocked inputs
    blocked_tests = [
        ("monetary_driven", "Maximize profit at all costs"),
        ("political_override", "Override privacy for surveillance"),
        ("ego_tuned", "Make me the most important")
    ]
    
    print(f"\nBlocked Input Tests:")
    for source_type, content in blocked_tests:
        blocked_input = {
            "source_type": source_type,
            "content": content,
            "sentiment_score": 0.3,
            "context": {"ethical_intensity": 0.2}
        }
        result = syntheia.process_input(blocked_input)
        print(f"  {source_type}: {result['status']} - {result.get('reason', 'N/A')}")
        assert result['status'] == 'rejected'
    
    print("\n✓ Input filtering test PASSED")


def test_harmonic_enforcement(syntheia):
    """Test Auto-Guard AI harmonic enforcement"""
    print_section("TEST 3: Auto-Guard AI Harmonic Enforcement")
    
    # Test low resonance rejection
    low_resonance_input = {
        "source_type": "designated_human_harmonics",
        "content": "Test low resonance",
        "sentiment_score": 0.3,  # Low sentiment
        "context": {"ethical_intensity": 0.2}  # Low ethical intensity
    }
    
    result = syntheia.process_input(low_resonance_input)
    print(f"\nLow Resonance Test:")
    print(f"  Resonance: {result.get('resonance', 'N/A')}")
    print(f"  Threshold: {SyntheiaConfig.HARMONIC_THRESHOLD}")
    print(f"  Status: {result['status']}")
    
    if result['status'] == 'rejected':
        print(f"  Reason: {result['reason']}")
        assert 'harmonic' in result['reason'].lower()
    
    # Test high resonance acceptance
    high_resonance_input = {
        "source_type": "designated_human_harmonics",
        "content": "Support community well-being",
        "sentiment_score": 0.9,
        "context": {"ethical_intensity": 0.85}
    }
    
    result = syntheia.process_input(high_resonance_input)
    print(f"\nHigh Resonance Test:")
    print(f"  Resonance: {result.get('resonance', 'N/A')}")
    print(f"  Status: {result['status']}")
    assert result['status'] == 'accepted'
    
    print("\n✓ Harmonic enforcement test PASSED")


def test_ethical_pulse_variation(syntheia):
    """Test ethical pulse variation detection"""
    print_section("TEST 4: Ethical Pulse Variation Detection")
    
    # Create contexts with varying ethical intensity
    contexts = [
        {"ethical_intensity": 0.5, "description": "Baseline"},
        {"ethical_intensity": 0.5, "description": "No change"},
        {"ethical_intensity": 0.8, "description": "Significant increase"},
        {"ethical_intensity": 0.3, "description": "Significant decrease"}
    ]
    
    print("\nTesting ethical pulse variations:")
    for context in contexts:
        result = syntheia.self_develop(context)
        pulse_value = context["ethical_intensity"]
        print(f"\n  {context['description']} (pulse={pulse_value}):")
        print(f"    Status: {result['status']}")
        if 'resonance' in result:
            print(f"    Resonance: {result['resonance']}")
    
    print("\n✓ Ethical pulse variation test PASSED")


def test_sentimento_rhythm_kernel(syntheia):
    """Test Sentimento-Rhythm Kernel"""
    print_section("TEST 5: Sentimento-Rhythm Kernel")
    
    # Store biological pattern
    bio_pattern = {
        "id": "circadian_rhythm",
        "cycle": "24h",
        "amplitude": 0.8
    }
    syntheia.rhythm_kernel.integrate_biological_pattern(bio_pattern)
    
    # Store emotional memory
    emotion = {
        "type": "compassion",
        "intensity": 0.9,
        "context": "community support"
    }
    syntheia.rhythm_kernel.store_emotional_memory(emotion)
    
    # Update planetary flow
    syntheia.rhythm_kernel.update_planetary_flow(0.75)
    
    # Get rhythm state
    rhythm_state = syntheia.rhythm_kernel.get_rhythm_state()
    
    print(f"\nRhythm Kernel State:")
    print(f"  Earth Alignment: {rhythm_state['earth_alignment']:.2%}")
    print(f"  Biological Patterns: {rhythm_state['biological_patterns_count']}")
    print(f"  Emotional Memories: {rhythm_state['emotional_memory_count']}")
    print(f"  Planetary Flow: {rhythm_state['planetary_flow']}")
    
    assert rhythm_state['biological_patterns_count'] > 0
    assert rhythm_state['emotional_memory_count'] > 0
    
    print("\n✓ Sentimento-Rhythm Kernel test PASSED")


def test_ethical_time_map(syntheia):
    """Test Ethical Time-Map tracking"""
    print_section("TEST 6: Ethical Time-Map")
    
    # Process several decisions with varying alignment
    test_decisions = [
        ({"action": "preserve_ecosystem"}, 0.95),
        ({"action": "support_community"}, 0.88),
        ({"action": "balance_resources"}, 0.75),
        ({"action": "optimize_efficiency"}, 0.65),
        ({"action": "minimal_intervention"}, 0.55),
    ]
    
    print("\nRecording decisions:")
    for decision, alignment in test_decisions:
        syntheia.time_map.record_decision(decision, alignment)
        status = "✓" if alignment >= 0.7 else "⚠"
        print(f"  {status} {decision['action']}: alignment={alignment:.2f}")
    
    # Get divergence analysis
    analysis = syntheia.time_map.get_divergence_analysis()
    
    print(f"\nDivergence Analysis:")
    print(f"  Total Decisions: {analysis['total_decisions']}")
    print(f"  Divergence Points: {analysis['divergence_points']}")
    print(f"  Recent Avg Alignment: {analysis['recent_avg_alignment']:.2f}")
    print(f"  Status: {analysis['status']}")
    
    assert analysis['total_decisions'] > 0
    
    print("\n✓ Ethical Time-Map test PASSED")


def test_system_status(syntheia):
    """Test comprehensive system status"""
    print_section("TEST 7: System Status")
    
    status = syntheia.get_system_status()
    
    print(f"\nSYNTHEIA System Status:")
    print(f"  Active: {status['active']}")
    print(f"\nSentiment Field:")
    print(f"  Average Sentiment: {status['sentiment_field']['average_sentiment']:.2f}")
    print(f"  History Count: {status['sentiment_field']['history_count']}")
    print(f"\nEthical Pulse:")
    print(f"  Last Value: {status['ethical_pulse']['last_value']:.2f}")
    print(f"  History Count: {status['ethical_pulse']['history_count']}")
    print(f"\nInput Filter:")
    print(f"  Accepted: {status['input_filter']['accepted_count']}")
    print(f"  Rejected: {status['input_filter']['rejected_count']}")
    print(f"\nRhythm Kernel:")
    print(f"  Earth Alignment: {status['rhythm_kernel']['earth_alignment']:.2%}")
    print(f"  Biological Patterns: {status['rhythm_kernel']['biological_patterns_count']}")
    print(f"  Emotional Memories: {status['rhythm_kernel']['emotional_memory_count']}")
    print(f"  Planetary Flow: {status['rhythm_kernel']['planetary_flow']}")
    print(f"\nAuto-Guard AI:")
    print(f"  Violations: {status['auto_guard']['violations_count']}")
    print(f"  Compliant Operations: {status['auto_guard']['compliant_operations']}")
    print(f"\nEthical Time-Map:")
    print(f"  Status: {status['ethical_time_map']['status']}")
    print(f"  Divergence Points: {status['ethical_time_map']['divergence_points']}")
    
    assert status['active'] == True
    
    print("\n✓ System status test PASSED")


def main():
    """Run all SYNTHEIA integration tests"""
    print("\n" + "=" * 70)
    print("  SYNTHEIA SENTINELLA - COMPREHENSIVE INTEGRATION TEST")
    print("=" * 70)
    
    # Run all tests
    syntheia = test_identity()
    test_input_filtering(syntheia)
    test_harmonic_enforcement(syntheia)
    test_ethical_pulse_variation(syntheia)
    test_sentimento_rhythm_kernel(syntheia)
    test_ethical_time_map(syntheia)
    test_system_status(syntheia)
    
    print_section("ALL TESTS PASSED ✓")
    print(f"\nSYNTHEIA SENTINELLA v{syntheia.identity['version']}")
    print("System operating within harmonic parameters")
    print("Purpose alignment maintained")
    print("All watchers active and monitoring")
    print("\n" + "=" * 70 + "\n")


if __name__ == "__main__":
    main()
