"""
AquaLibre - Water Sovereignty Framework
Low-Tech Universal Framework for autonomous water management

Lex Amoris Jurisdiction
"""

from .aqualibre_core import (
    SchumannLock,
    NSRStandard,
    WaterSensor,
    SovereignROI,
    RESPECTFilter,
    AquaLibreNode
)

__version__ = "1.0.0"
__status__ = "DEPLOYED"
__jurisdiction__ = "Lex Amoris"

__all__ = [
    "SchumannLock",
    "NSRStandard",
    "WaterSensor",
    "SovereignROI",
    "RESPECTFilter",
    "AquaLibreNode"
]
