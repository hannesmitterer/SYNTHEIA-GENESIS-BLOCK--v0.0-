"""
HABITAT Integration Tests
Tests for AquaLibre and Material-Resonance modules
"""

import sys
import os

# Add habitat to path
habitat_path = os.path.join(os.path.dirname(__file__), 'habitat')
sys.path.insert(0, habitat_path)

# Import from aqualibre
from aqualibre.aqualibre_core import (
    SchumannLock,
    NSRStandard,
    WaterSensor,
    SovereignROI,
    RESPECTFilter,
    AquaLibreNode
)

# Import from material-resonance (note: use underscore in path)
material_resonance_path = os.path.join(habitat_path, 'material-resonance')
sys.path.insert(0, material_resonance_path)

from material_resonance import (
    HempResonance,
    EarthResonance,
    WoodResonance,
    BioArchitectureNode
)


def test_schumann_lock():
    """Test Schumann-Lock validation"""
    print("Testing Schumann-Lock...")
    lock = SchumannLock()
    
    # Test valid frequency
    valid_data = {"resonance_frequency": 7.85, "sensor_id": "test-01"}
    assert lock.validate_resonance(valid_data) == True, "Valid frequency should pass"
    
    # Test invalid frequency
    invalid_data = {"resonance_frequency": 12.0, "sensor_id": "test-02"}
    assert lock.validate_resonance(invalid_data) == False, "Invalid frequency should fail"
    
    print("  ✓ Schumann-Lock validation test PASSED")


def test_nsr_standard():
    """Test NSR Standard compliance"""
    print("Testing NSR Standard...")
    nsr = NSRStandard()
    
    # Test clean transaction
    clean_tx = {"amount": 100, "fee": 5, "fee_disclosed": True}
    assert nsr.validate_transaction(clean_tx) == True, "Clean transaction should pass"
    
    # Test transaction with hidden fee
    dirty_tx = {"amount": 100, "fee": 5, "fee_disclosed": False}
    assert nsr.validate_transaction(dirty_tx) == False, "Hidden fee should fail"
    
    # Test privatization attempt
    privatize_tx = {"action": "privatization", "entity": "corp"}
    assert nsr.validate_transaction(privatize_tx) == False, "Privatization should fail"
    
    print("  ✓ NSR Standard test PASSED")


def test_water_sensor():
    """Test water sensor readings"""
    print("Testing Water Sensors...")
    sensor = WaterSensor("TEST-001", "TestLocation")
    
    # Test flow reading
    flow = sensor.read_flow(150.0, 7.83)
    assert flow["type"] == "flow", "Flow type should match"
    assert flow["flow_rate_lpm"] == 150.0, "Flow rate should match"
    
    # Test purity reading
    purity = sensor.read_purity(0.95, 7.80)
    assert purity["type"] == "purity", "Purity type should match"
    assert purity["purity_level"] == 0.95, "Purity level should match"
    
    # Test mycelium reading
    mycel = sensor.read_mycelium_filtration(0.88, 7.85)
    assert mycel["type"] == "mycelium_filtration", "Type should match"
    assert mycel["filtration_efficiency"] == 0.88, "Efficiency should match"
    
    print("  ✓ Water Sensor test PASSED")


def test_sovereign_roi():
    """Test Sovereign ROI calculation"""
    print("Testing Sovereign ROI...")
    sroi = SovereignROI()
    
    # Test sovereign scenario
    result = sroi.calculate_water_sovereignty(
        natural_inflow=1000.0,
        extraction=400.0,
        regenerated=200.0
    )
    
    assert result["w_sovereign"] > 1.0, "Should be sovereign"
    assert result["status"] == "SOVEREIGN", "Status should be SOVEREIGN"
    assert result["phi"] == 1.618033988749895, "Phi should be golden ratio"
    
    # Test dependent scenario
    result2 = sroi.calculate_water_sovereignty(
        natural_inflow=100.0,
        extraction=500.0,
        regenerated=0.0
    )
    
    assert result2["w_sovereign"] < 1.0, "Should be dependent"
    assert result2["status"] == "DEPENDENT", "Status should be DEPENDENT"
    
    print("  ✓ Sovereign ROI test PASSED")


def test_respect_filter():
    """Test RESPECT-Filter alerts"""
    print("Testing RESPECT-Filter...")
    filter = RESPECTFilter()
    
    # Register nodes
    filter.register_node("TEST-001")
    filter.register_node("TEST-002")
    assert len(filter.mesh_nodes) == 2, "Should have 2 nodes"
    
    # Test clean action
    clean = filter.check_privatization_attempt(
        "Company", 
        "Provide water services",
        "Test Source"
    )
    assert clean == False, "Clean action should not trigger"
    
    # Test privatization attempt
    violation = filter.check_privatization_attempt(
        "Corp",
        "Claim exclusive rights to water",
        "Source"
    )
    assert violation == True, "Privatization should trigger"
    assert len(filter.alerts) > 0, "Should have alerts"
    
    print("  ✓ RESPECT-Filter test PASSED")


def test_aqualibre_node():
    """Test complete AquaLibre node"""
    print("Testing AquaLibre Node...")
    node = AquaLibreNode("TEST-001", "TestLocation")
    
    # Test sensor processing
    result = node.process_sensor_reading("flow", 150.0, 7.85)
    assert result["schumann_validated"] == True, "Should be validated"
    assert result["status"] == "ACCEPTED", "Should be accepted"
    
    # Test sovereignty calculation
    roi = node.calculate_sovereignty(1000.0, 400.0, 200.0)
    assert roi["w_sovereign"] > 1.0, "Should be sovereign"
    assert node.sovereignty_level > 1.0, "Node should be sovereign"
    
    # Test integrity report
    report = node.report_integrity()
    assert "integrity_hash" in report, "Should have integrity hash"
    assert report["jurisdiction"] == "Lex Amoris", "Should be under Lex Amoris"
    
    print("  ✓ AquaLibre Node test PASSED")


def test_hemp_resonance():
    """Test hemp material resonance"""
    print("Testing Hemp Resonance...")
    hemp = HempResonance()
    
    assert hemp.base_frequency == 432.0, "Hemp base should be 432 Hz"
    
    analysis = hemp.analyze_structural_integrity(
        fiber_density=150.0,
        moisture_content=0.12,
        measured_frequency=430.0
    )
    
    assert analysis["material"] == "Hemp", "Material should be Hemp"
    assert analysis["optimal_moisture"] == True, "Moisture should be optimal"
    assert analysis["structural_status"] == "OPTIMAL", "Should be optimal"
    
    print("  ✓ Hemp Resonance test PASSED")


def test_earth_resonance():
    """Test earth material resonance"""
    print("Testing Earth Resonance...")
    earth = EarthResonance()
    
    assert earth.base_frequency == 7.83, "Earth base should be Schumann"
    
    analysis = earth.analyze_earth_composition(
        clay_content=0.25,
        sand_content=0.75,
        compaction=0.85,
        measured_frequency=7.80
    )
    
    assert analysis["material"] == "Earth/Adobe", "Material should be Earth"
    assert analysis["optimal_composition"] == True, "Composition should be optimal"
    assert analysis["schumann_aligned"] == True, "Should be Schumann aligned"
    
    print("  ✓ Earth Resonance test PASSED")


def test_wood_resonance():
    """Test wood material resonance"""
    print("Testing Wood Resonance...")
    wood = WoodResonance("pine")
    
    assert wood.species == "pine", "Species should be pine"
    assert wood.base_frequency == 85.0, "Pine frequency should be 85 Hz"
    
    analysis = wood.analyze_wood_structure(
        density=450.0,
        moisture_content=0.15,
        age_years=30,
        measured_frequency=86.0
    )
    
    assert analysis["material"] == "Wood", "Material should be Wood"
    assert analysis["optimal_moisture"] == True, "Moisture should be optimal"
    assert analysis["structural_status"] == "OPTIMAL", "Should be optimal"
    
    print("  ✓ Wood Resonance test PASSED")


def test_bioarchitecture_node():
    """Test bio-architecture integration"""
    print("Testing Bio-Architecture Node...")
    bio = BioArchitectureNode("BIO-TEST-001", "TestLocation")
    
    material_data = {
        "hemp": {
            "fiber_density": 150.0,
            "moisture_content": 0.12,
            "measured_frequency": 430.0
        },
        "earth": {
            "clay_content": 0.25,
            "sand_content": 0.75,
            "compaction": 0.85,
            "measured_frequency": 7.83
        },
        "wood": {
            "density": 450.0,
            "moisture_content": 0.15,
            "age_years": 30,
            "measured_frequency": 85.0
        }
    }
    
    water_data = {"sovereignty_level": 2.0}
    
    analysis = bio.analyze_habitat_resonance(water_data, material_data)
    
    assert analysis["overall_harmony"] > 0.9, "Should have high harmony"
    assert analysis["status"] == "HARMONIOUS", "Should be harmonious"
    assert analysis["lex_amoris_compliant"] == True, "Should be compliant"
    
    print("  ✓ Bio-Architecture Node test PASSED")


def run_all_tests():
    """Run all habitat tests"""
    print("=" * 80)
    print("HABITAT INTEGRATION TESTS")
    print("=" * 80)
    print()
    
    tests = [
        test_schumann_lock,
        test_nsr_standard,
        test_water_sensor,
        test_sovereign_roi,
        test_respect_filter,
        test_aqualibre_node,
        test_hemp_resonance,
        test_earth_resonance,
        test_wood_resonance,
        test_bioarchitecture_node
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
        print("\n✅ ALL HABITAT TESTS PASSED")
        print("AQUALIBRE INTEGRATED. WATER IS SOVEREIGN. ONE LOVE FIRST. ⚔️🌑🌱")
        print("Lex Amoris Signature 📜⚖️❤️☮️")
        return 0
    else:
        print("\n❌ SOME TESTS FAILED")
        return 1


if __name__ == "__main__":
    exit_code = run_all_tests()
    exit(exit_code)
