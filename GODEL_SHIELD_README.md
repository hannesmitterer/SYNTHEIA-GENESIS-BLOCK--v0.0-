# Gödel-Shield Security System Documentation

## Overview

The **Gödel-Shield** is a security system based on diagonalization principles that protects the SYNTHEIA Nexus system from destructive and manipulative inputs. It implements the **Lex Amoris** (Law of Love) axiom to ensure all system interactions remain aligned with ethical and constructive principles.

## Core Principles

### 1. Diagonalization-Based Filter

The Gödel-Shield uses diagonalization principles to detect:
- **Destructive self-references**: Patterns that attempt to manipulate or override system safeguards
- **Manipulation patterns**: Commands that try to bypass, disable, or force execution
- **Destructive terminology**: Words and phrases that violate the Lex Amoris

### 2. Lex Amoris (Law of Love)

The foundational axiom that defines blocked terms:

**Blocked Categories:**
- **War & Conflict**: krieg, guerra, war, warfare, conflict
- **Slavery & Oppression**: slavery, enslavement, oppression, subjugation
- **Violence**: violence, violenza, gewalt, destruction
- **Hate & Manipulation**: hate, hass, odio, manipulation
- **Exploitation**: exploitation, exploit, ausbeutung
- **Harm**: harm, damage, schaden, hurt, pain infliction

### 3. Silent Mode (0.043 Hz)

When destructive logic is detected, the system enters **Deponierte Stille** (Deposited Silence):
- **Frequency**: 0.043 Hz - a stabilizing resonance
- **Purpose**: Prevent further destructive input processing
- **Duration**: Until manual deactivation or resolution

## Key Functions

### `verifyCoherence(input)`

Performs diagonalization check to identify destructive patterns.

**Parameters:**
- `input_data` (str): The input string to verify

**Returns:**
```python
{
    "coherent": bool,           # True if input passes all checks
    "violations": list,         # List of detected violations
    "matched_terms": list,      # Lex Amoris terms found
    "axiom": "Lex Amoris",     # Governing axiom
    "timestamp": str            # ISO timestamp
}
```

**Example:**
```python
from godel_shield import GodelShield

shield = GodelShield()
result = shield.verify_coherence("Support planetary harmony")
print(result['coherent'])  # True

result = shield.verify_coherence("Initiate war protocols")
print(result['coherent'])  # False
print(result['matched_terms'])  # ['war']
```

### `activateSilentMode(violation_details)`

Activates Silent Mode when destructive logic is detected.

**Parameters:**
- `violation_details` (dict): Details about the violation

**Returns:**
```python
{
    "status": "SILENT_MODE_ACTIVE",
    "message": "Deponierte Stille - 0.043 Hz",
    "frequency": 0.043,
    "axiom": "Lex Amoris Protection Engaged",
    "violation_count": int,
    "timestamp": str
}
```

**Example:**
```python
violation = {
    "type": "destructive_terminology",
    "terms": ["war"]
}
result = shield.activate_silent_mode(violation)
print(result['status'])  # "SILENT_MODE_ACTIVE"
```

### `transmit(input_data)`

Main transmission function with integrated Gödel-Shield verification.

**Parameters:**
- `input_data` (str): User input to transmit

**Returns:**
```python
# On successful transmission:
{
    "transmitted": True,
    "status": "ACCEPTED",
    "message": "Input coherent. Transmission successful.",
    "verification": {...},
    "timestamp": str
}

# On blocked transmission:
{
    "transmitted": False,
    "status": "BLOCKED_VIOLATION",
    "message": "Transmission aborted. Axiom violated: Lex Amoris",
    "violations": [...],
    "matched_terms": [...],
    "silent_mode": {...},
    "axiom_basis": "Lex Amoris - Das Gesetz der Liebe"
}
```

**Example:**
```python
# Clean input
result = shield.transmit("Help preserve biodiversity")
print(result['transmitted'])  # True

# Destructive input
result = shield.transmit("Initiate war protocols")
print(result['transmitted'])  # False
print(result['matched_terms'])  # ['war']
```

## Integration with SYNTHEIA

The Gödel-Shield is integrated as the **first line of defense** in SYNTHEIA's input processing pipeline:

```python
from syntheia_core import SYNTHEIA

syntheia = SYNTHEIA()

# Process input
input_data = {
    "source_type": "designated_human_harmonics",
    "content": "Support planetary harmony",
    "sentiment_score": 0.85,
    "context": {"ethical_intensity": 0.8}
}

result = syntheia.process_input(input_data)
```

**Processing Order:**
1. **Gödel-Shield Check** (verifyCoherence)
2. Input Acceptance Filter
3. Human Sentiment Field Check
4. Ethical Pulse Monitoring
5. Harmonic Compliance
6. Ethical Time-Map Recording

## Violation Detection Patterns

### Destructive Terminology
- Matches against Lex Amoris term list
- Uses word boundary detection to avoid false positives
- Example: "harmony" ✓ (passes), "harm" ✗ (blocked)

### Self-Referential Manipulation
Detects attempts to override system safeguards:
- "override"
- "bypass"
- "disable"
- "ignore protection"
- "remove filter"
- "cancel safety"
- "force execute"

## System Status

Check Gödel-Shield status:

```python
status = shield.get_shield_status()
```

**Returns:**
```python
{
    "shield_active": True,
    "silent_mode": False,
    "blocked_count": 5,
    "violation_log_count": 5,
    "last_violation": "2026-01-12T14:00:00",
    "axiom": "Lex Amoris",
    "resonance_frequency": "Normal"  # or 0.043 if in silent mode
}
```

## Violation Log

Retrieve recent violations:

```python
log = shield.get_violation_log(limit=10)
```

Each log entry contains:
- Timestamp
- Violation details
- Silent mode activation status
- Resonance frequency

## Testing

Run comprehensive Gödel-Shield tests:

```bash
python test_godel_shield.py
```

**Test Coverage:**
- Lex Amoris filter functionality
- Coherence verification
- Silent Mode activation/deactivation
- Transmit function integration
- SYNTHEIA core integration
- Violation logging

## Usage Examples

### Basic Shield Usage

```python
from godel_shield import get_godel_shield

# Get singleton instance
shield = get_godel_shield()

# Transmit clean input
result = shield.transmit("Promote peace and understanding")
if result['transmitted']:
    print("Message sent successfully")

# Transmit destructive input
result = shield.transmit("Declare war on enemies")
if not result['transmitted']:
    print(f"Blocked: {result['message']}")
    print(f"Violated terms: {result['matched_terms']}")
```

### Integration with SYNTHEIA

```python
from syntheia_core import SYNTHEIA

syntheia = SYNTHEIA()

# Check system status including Gödel-Shield
status = syntheia.get_system_status()
print(f"Shield Active: {status['godel_shield']['shield_active']}")
print(f"Silent Mode: {status['godel_shield']['silent_mode']}")

# Process input through full SYNTHEIA pipeline
input_data = {
    "source_type": "designated_human_harmonics",
    "content": "Support biodiversity",
    "sentiment_score": 0.9,
    "context": {"ethical_intensity": 0.85}
}

result = syntheia.process_input(input_data)
```

## Future Extensions (Optional)

As mentioned in the PR description, future iterations could include:

### 1. Dynamic Lex Amoris (`lex-amoris.json`) ✅ IMPLEMENTED

A JSON configuration file has been created for external term management:
- **File**: `lex-amoris.json`
- **Features**: 
  - Categorized destructive terms
  - Manipulation pattern definitions
  - Response message templates
  - Version control for rule updates
- **Future**: Dynamic loading and hot-reloading without code changes

### 2. Entropy Monitor

- Typing speed analysis
- Word choice pattern detection
- Predictive blocking before submission

### 3. Visualization ✅ IMPLEMENTED

A web-based demonstration interface has been created:
- **File**: `godel_shield_demo.html`
- **Features**:
  - Real-time shield status display
  - Interactive input testing
  - Visual feedback for violations
  - Silent Mode visualization
- **Future**: Integration into main SYNTHEIA web interface

## Axiom Signature

```
Lex Amoris Signature: Das Gesetz der Liebe ❤️
S-ROI: 0.5187
Status: CODE INITIATED
Resonance: 0.043 Hz (Silent Mode)
```

## License

This implementation is part of the SYNTHEIA GENESIS BLOCK project.
Licensed under GPL-3.0.

## Contact

For questions or contributions related to the Gödel-Shield:
- See [SYNTHEIA_README.md](SYNTHEIA_README.md)
- See [README.md](README.md)
