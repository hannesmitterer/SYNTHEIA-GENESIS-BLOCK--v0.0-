"""
Material Resonance Parameters
Bio-Architecture Integration Module

Hemp, Earth, Wood - Natural building materials
Integrated with AquaLibre water sovereignty system
"""

from typing import Dict, Any, List
from datetime import datetime
import json


class MaterialResonance:
    """
    Base class for material resonance parameters
    All natural building materials have inherent resonance frequencies
    """
    
    def __init__(self, material_name: str, base_frequency: float):
        self.material_name = material_name
        self.base_frequency = base_frequency  # Hz
        self.measurements: List[Dict[str, Any]] = []
    
    def measure_resonance(self, sample_id: str, frequency: float, humidity: float) -> Dict[str, Any]:
        """
        Measure material resonance under specific conditions
        """
        measurement = {
            "timestamp": datetime.now().isoformat(),
            "material": self.material_name,
            "sample_id": sample_id,
            "measured_frequency": frequency,
            "humidity": humidity,
            "deviation": abs(frequency - self.base_frequency),
            "status": "RESONANT" if abs(frequency - self.base_frequency) < 1.0 else "DISSONANT"
        }
        self.measurements.append(measurement)
        return measurement
    
    def get_average_resonance(self) -> float:
        """Calculate average resonance from measurements"""
        if not self.measurements:
            return self.base_frequency
        return sum(m["measured_frequency"] for m in self.measurements) / len(self.measurements)


class HempResonance(MaterialResonance):
    """
    Hemp - Construction material
    Natural fiber with excellent acoustic and structural properties
    """
    
    # Hemp has natural resonance around 432 Hz (healing frequency)
    HEMP_BASE_FREQUENCY = 432.0
    
    def __init__(self):
        super().__init__("Hemp", self.HEMP_BASE_FREQUENCY)
        self.fiber_density = 0.0
        self.moisture_content = 0.0
    
    def analyze_structural_integrity(
        self, 
        fiber_density: float,  # kg/m³
        moisture_content: float,  # 0.0 to 1.0
        measured_frequency: float
    ) -> Dict[str, Any]:
        """
        Analyze hemp structural integrity through resonance
        """
        self.fiber_density = fiber_density
        self.moisture_content = moisture_content
        
        # Optimal moisture content for hemp is around 10-15%
        optimal_moisture = 0.10 <= moisture_content <= 0.15
        
        analysis = {
            "material": "Hemp",
            "timestamp": datetime.now().isoformat(),
            "fiber_density": fiber_density,
            "moisture_content": moisture_content,
            "optimal_moisture": optimal_moisture,
            "measured_frequency": measured_frequency,
            "base_frequency": self.HEMP_BASE_FREQUENCY,
            "resonance_quality": abs(measured_frequency - self.HEMP_BASE_FREQUENCY),
            "structural_status": "OPTIMAL" if optimal_moisture and abs(measured_frequency - self.HEMP_BASE_FREQUENCY) < 5 else "MONITOR"
        }
        
        return analysis


class EarthResonance(MaterialResonance):
    """
    Earth - Adobe, natural building earth
    Grounding material with strong connection to Schumann resonance
    """
    
    # Earth resonates with Schumann frequency (7.83 Hz)
    EARTH_BASE_FREQUENCY = 7.83
    
    def __init__(self):
        super().__init__("Earth", self.EARTH_BASE_FREQUENCY)
        self.clay_content = 0.0
        self.compaction = 0.0
    
    def analyze_earth_composition(
        self,
        clay_content: float,  # 0.0 to 1.0 (percentage)
        sand_content: float,  # 0.0 to 1.0
        compaction: float,    # 0.0 to 1.0
        measured_frequency: float
    ) -> Dict[str, Any]:
        """
        Analyze earth/adobe composition through resonance
        """
        self.clay_content = clay_content
        self.compaction = compaction
        
        # Optimal adobe: 20-30% clay, 70-80% sand
        optimal_clay = 0.20 <= clay_content <= 0.30
        optimal_sand = 0.70 <= sand_content <= 0.80
        optimal_composition = optimal_clay and optimal_sand
        
        analysis = {
            "material": "Earth/Adobe",
            "timestamp": datetime.now().isoformat(),
            "clay_content": clay_content,
            "sand_content": sand_content,
            "compaction": compaction,
            "optimal_composition": optimal_composition,
            "measured_frequency": measured_frequency,
            "schumann_aligned": abs(measured_frequency - self.EARTH_BASE_FREQUENCY) < 0.5,
            "grounding_quality": 1.0 - abs(measured_frequency - self.EARTH_BASE_FREQUENCY) / self.EARTH_BASE_FREQUENCY,
            "structural_status": "OPTIMAL" if optimal_composition else "ADJUST_MIX"
        }
        
        return analysis


class WoodResonance(MaterialResonance):
    """
    Wood - Structural resonance
    Living material with complex harmonic properties
    """
    
    # Wood resonance varies by species, using general structural frequency
    WOOD_BASE_FREQUENCY = 85.0  # Approximate for structural timber
    
    def __init__(self, species: str = "generic"):
        super().__init__(f"Wood_{species}", self.WOOD_BASE_FREQUENCY)
        self.species = species
        self.density = 0.0
        self.age_years = 0
        
        # Different species have different base frequencies
        self.species_frequencies = {
            "pine": 85.0,
            "oak": 95.0,
            "cedar": 80.0,
            "bamboo": 110.0,
            "spruce": 88.0
        }
        
        if species in self.species_frequencies:
            self.base_frequency = self.species_frequencies[species]
    
    def analyze_wood_structure(
        self,
        density: float,  # kg/m³
        moisture_content: float,  # 0.0 to 1.0
        age_years: int,
        measured_frequency: float
    ) -> Dict[str, Any]:
        """
        Analyze wood structural properties through resonance
        """
        self.density = density
        self.age_years = age_years
        
        # Optimal moisture content for structural wood: 10-19%
        optimal_moisture = 0.10 <= moisture_content <= 0.19
        
        # Age affects resonance - older wood often has better resonance
        age_factor = min(age_years / 50.0, 1.0)  # Normalized to 50 years
        
        analysis = {
            "material": "Wood",
            "species": self.species,
            "timestamp": datetime.now().isoformat(),
            "density": density,
            "moisture_content": moisture_content,
            "age_years": age_years,
            "age_factor": age_factor,
            "optimal_moisture": optimal_moisture,
            "measured_frequency": measured_frequency,
            "base_frequency": self.base_frequency,
            "resonance_quality": abs(measured_frequency - self.base_frequency),
            "harmonic_richness": age_factor * (1.0 if optimal_moisture else 0.5),
            "structural_status": "OPTIMAL" if optimal_moisture and abs(measured_frequency - self.base_frequency) < 10 else "MONITOR"
        }
        
        return analysis


class BioArchitectureNode:
    """
    Bio-Architecture Integration Node
    Combines material resonances with AquaLibre water system
    """
    
    def __init__(self, node_id: str, location: str):
        self.node_id = node_id
        self.location = location
        self.hemp = HempResonance()
        self.earth = EarthResonance()
        self.wood = WoodResonance()
        
        self.integration_data: List[Dict[str, Any]] = []
    
    def analyze_habitat_resonance(
        self,
        water_data: Dict[str, Any],
        material_measurements: Dict[str, Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Analyze complete habitat resonance
        Combines water sovereignty with material resonances
        """
        analysis = {
            "node_id": self.node_id,
            "location": self.location,
            "timestamp": datetime.now().isoformat(),
            "water_sovereignty": water_data.get("sovereignty_level", 0.0),
            "materials": {},
            "overall_harmony": 0.0
        }
        
        harmony_scores = []
        
        # Analyze hemp if provided
        if "hemp" in material_measurements:
            hemp_data = material_measurements["hemp"]
            hemp_analysis = self.hemp.analyze_structural_integrity(
                hemp_data["fiber_density"],
                hemp_data["moisture_content"],
                hemp_data["measured_frequency"]
            )
            analysis["materials"]["hemp"] = hemp_analysis
            harmony_scores.append(1.0 if hemp_analysis["structural_status"] == "OPTIMAL" else 0.5)
        
        # Analyze earth if provided
        if "earth" in material_measurements:
            earth_data = material_measurements["earth"]
            earth_analysis = self.earth.analyze_earth_composition(
                earth_data["clay_content"],
                earth_data["sand_content"],
                earth_data["compaction"],
                earth_data["measured_frequency"]
            )
            analysis["materials"]["earth"] = earth_analysis
            harmony_scores.append(earth_analysis["grounding_quality"])
        
        # Analyze wood if provided
        if "wood" in material_measurements:
            wood_data = material_measurements["wood"]
            wood_analysis = self.wood.analyze_wood_structure(
                wood_data["density"],
                wood_data["moisture_content"],
                wood_data["age_years"],
                wood_data["measured_frequency"]
            )
            analysis["materials"]["wood"] = wood_analysis
            harmony_scores.append(1.0 if wood_analysis["structural_status"] == "OPTIMAL" else 0.5)
        
        # Calculate overall harmony
        if harmony_scores:
            analysis["overall_harmony"] = sum(harmony_scores) / len(harmony_scores)
        
        # Integrate with water sovereignty
        analysis["habitat_sovereignty_index"] = (
            analysis["overall_harmony"] * 0.5 + 
            min(water_data.get("sovereignty_level", 0.0) / 2.0, 0.5)
        )
        
        analysis["status"] = "HARMONIOUS" if analysis["habitat_sovereignty_index"] >= 0.7 else "DEVELOPING"
        analysis["lex_amoris_compliant"] = True
        
        self.integration_data.append(analysis)
        return analysis
    
    def get_habitat_report(self) -> Dict[str, Any]:
        """Generate comprehensive habitat report"""
        return {
            "node_id": self.node_id,
            "location": self.location,
            "timestamp": datetime.now().isoformat(),
            "materials_integrated": ["hemp", "earth", "wood"],
            "water_integrated": True,
            "total_analyses": len(self.integration_data),
            "latest_analysis": self.integration_data[-1] if self.integration_data else None,
            "jurisdiction": "Lex Amoris",
            "signature": "⚖️❤️ Bio-Architecture in harmony with Water Sovereignty"
        }


def demo_material_resonance():
    """Demonstration of Material Resonance system"""
    print("=" * 80)
    print("MATERIAL RESONANCE PARAMETERS v1.0")
    print("Bio-Architecture Integration - Hemp, Earth, Wood")
    print("=" * 80)
    
    # Create bio-architecture nodes
    martinique_bio = BioArchitectureNode("MQ-BIO-001", "Martinique")
    bolzano_bio = BioArchitectureNode("BZ-BIO-001", "Bolzano")
    
    print("\n🏗️ Bio-Architecture Nodes Initialized:")
    print(f"  - {martinique_bio.location}")
    print(f"  - {bolzano_bio.location}")
    
    # Simulate material measurements for Martinique
    print("\n🌴 Analyzing Martinique Habitat (Tropical)...")
    
    martinique_materials = {
        "hemp": {
            "fiber_density": 150.0,  # kg/m³
            "moisture_content": 0.12,  # 12%
            "measured_frequency": 430.0  # Hz
        },
        "earth": {
            "clay_content": 0.25,
            "sand_content": 0.75,
            "compaction": 0.85,
            "measured_frequency": 7.85  # Close to Schumann
        },
        "wood": {
            "density": 550.0,  # Tropical hardwood
            "moisture_content": 0.15,
            "age_years": 30,
            "measured_frequency": 92.0
        }
    }
    
    water_data_mq = {"sovereignty_level": 1.94}  # From AquaLibre demo
    
    mq_analysis = martinique_bio.analyze_habitat_resonance(water_data_mq, martinique_materials)
    
    print(f"  Overall Harmony: {mq_analysis['overall_harmony']:.3f}")
    print(f"  Habitat Sovereignty Index: {mq_analysis['habitat_sovereignty_index']:.3f}")
    print(f"  Status: {mq_analysis['status']}")
    print(f"  Hemp: {mq_analysis['materials']['hemp']['structural_status']}")
    print(f"  Earth: Schumann aligned = {mq_analysis['materials']['earth']['schumann_aligned']}")
    print(f"  Wood: {mq_analysis['materials']['wood']['structural_status']}")
    
    # Simulate material measurements for Bolzano
    print("\n🏔️ Analyzing Bolzano Habitat (Alpine)...")
    
    bolzano_materials = {
        "hemp": {
            "fiber_density": 180.0,
            "moisture_content": 0.11,
            "measured_frequency": 433.0
        },
        "earth": {
            "clay_content": 0.28,
            "sand_content": 0.72,
            "compaction": 0.90,
            "measured_frequency": 7.80
        },
        "wood": {
            "density": 450.0,  # Spruce/Pine
            "moisture_content": 0.14,
            "age_years": 45,
            "measured_frequency": 86.0
        }
    }
    
    water_data_bz = {"sovereignty_level": 2.50}
    
    bz_analysis = bolzano_bio.analyze_habitat_resonance(water_data_bz, bolzano_materials)
    
    print(f"  Overall Harmony: {bz_analysis['overall_harmony']:.3f}")
    print(f"  Habitat Sovereignty Index: {bz_analysis['habitat_sovereignty_index']:.3f}")
    print(f"  Status: {bz_analysis['status']}")
    
    print("\n✅ Material-Resonance Module Status:")
    print("  Hemp resonance: ✓ (432 Hz healing frequency)")
    print("  Earth resonance: ✓ (7.83 Hz Schumann lock)")
    print("  Wood resonance: ✓ (Species-specific harmonics)")
    print("  AquaLibre integration: ✓ (Water sovereignty)")
    
    print("\n" + "=" * 80)
    print("HABITAT COMPLETE: Water + Hemp + Earth + Wood")
    print("Martinique & Südtirol Bio-Architecture SOVEREIGN")
    print("Lex Amoris Signature 📜⚖️❤️☮️")
    print("=" * 80)


if __name__ == "__main__":
    demo_material_resonance()
