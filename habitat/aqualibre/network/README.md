# AquaLibre Network Protocol Layer v1.1

**Status:** OPERATIONAL  
**Architecture:** Decentralized, No Central Authority  
**Consensus:** Distributed Validation (66% threshold)

---

## Overview

The Network Protocol Layer implements a complete decentralized system for water sovereignty with cryptographic identity, distributed consensus, and game-theoretic validation.

**Core Principle:**
> Each node decides autonomously, but follows the same rules.

---

## Architecture

### 1. Identity Layer (`identity.py`)

**NodeIdentity** - Cryptographic Identity System
- Prevents Sybil attacks (1 Node = 1 cryptographic identity)
- Public/private key pairs (simplified - use Ed25519 in production)
- Tamper-evident signatures on all actions
- Identity proof for network registration

**NodeState** - Weighted Node System
- Not all nodes are equal (capacity × reliability = weight)
- Stable nodes have more influence
- Uptime and action success tracking
- Dynamic reliability adjustment

**TimeAveragedMetrics** - Temporal Validation
- Prevents short-term manipulation
- Rolling averages over configurable windows (default: 30 days)
- Trend detection (IMPROVING, STABLE, DECLINING)
- Consistency validation (low variance required)

### 2. Validation Layer (`validators.py`)

**NSRValidator** - Anti-Coercion (No Secret Revenue)
```python
Rules:
- No external permissions required
- No forced dependencies
- No central control
- Nodes function offline
```

**ReciprocityFilter** - Lex Amoris Symmetry
```python
Rules:
- No one-sided extraction
- Minimum 50% reciprocity ratio
- Benefits must be symmetric
- Data sharing must be mutual
```

**CooperationEngine** - One Love Scoring
```python
Formula:
score = (shared_data_ratio × 0.4) + 
        (water_regeneration × 0.4) + 
        (network_contribution × 0.2)

Trust Levels:
- score ≥ 0.8: HIGH_TRUST (reference node)
- score ≥ 0.6: MODERATE_TRUST
- score ≥ 0.4: LOW_TRUST
- score < 0.4: UNTRUSTED
```

### 3. Consensus Layer (`consensus.py`)

**DistributedConsensus** - Collective Decision-Making
- No central gatekeeper
- 66% weighted consensus required
- Validator registration system
- Vote weighting by node reliability
- Decision history tracking

**GameTheoryValidator** - Anti-Gaming
```python
Extraction Cost = Extraction / (Recharge + 1)

Threshold: 2.0
- Cost > 2.0 → LIMITED_ACCESS
- Cost ≤ 2.0 → FULL_ACCESS

Effect: Makes exploitation automatically unattractive
```

### 4. Protocol Layer (`protocol.py`)

**AquaLibreProtocol** - Main Pipeline

**3-Filter Validation:**
```
Action → NSR Validator → Reciprocity Filter → Cooperation Score → Result
            ↓ FAIL           ↓ FAIL              ↓ LIMITED
         REJECTED         REJECTED              LIMITED
```

**Results:**
- `ACCEPTED` - Passed all filters
- `REJECTED` - NSR or Reciprocity violation
- `LIMITED` - High extraction cost

---

## Usage Examples

### Basic Protocol Usage

```python
from habitat.aqualibre.network import (
    NodeIdentity, NodeState, AquaLibreProtocol, Action
)

# Create node
identity = NodeIdentity("MQ-001")
state = NodeState(water_capacity=1000.0, reliability=0.95)
protocol = AquaLibreProtocol(identity, state)

# Create action
action = Action(
    "MQ-001",
    "water_extraction",
    extraction=100,
    recharge=150,
    requires_external_permission=False,
    creates_dependency=False,
    benefit_self=1.0,
    benefit_others=1.5
)

# Process through pipeline
metrics = {
    "shared_data_ratio": 0.9,
    "water_regeneration": 0.8,
    "network_contribution": 0.7
}

result = protocol.process_action(action, metrics)

if result["status"] == "ACCEPTED":
    print(f"✓ Action accepted - Score: {result['cooperation_score']:.3f}")
else:
    print(f"✗ Action rejected - Reason: {result['reason']}")
```

### Distributed Consensus

```python
from habitat.aqualibre.network import DistributedConsensus, NSRValidator, ReciprocityFilter, Action

# Create consensus system
consensus = DistributedConsensus()

# Register validators
consensus.register_validator(NSRValidator())
consensus.register_validator(ReciprocityFilter())

# Validate action
action = Action("MQ-001", "water_extraction", extraction=100, recharge=150)
decision = consensus.validate_distributed(action)

if decision["consensus"]:
    print(f"✓ Consensus reached: {decision['consensus_ratio']:.1%}")
else:
    print(f"✗ No consensus: {decision['consensus_ratio']:.1%} < 66%")
```

### Game Theory Check

```python
from habitat.aqualibre.network import GameTheoryValidator

game = GameTheoryValidator()

# Check extraction behavior
result = game.should_limit_access(
    node_id="MQ-001",
    extraction=300,
    recharge=50
)

print(f"Extraction Cost: {result['current_cost']:.2f}")
print(f"Status: {result['status']}")  # LIMITED_ACCESS or FULL_ACCESS
```

---

## System States

| State | Condition | Access |
|-------|-----------|--------|
| REGENERATIVE | Recharge > Extraction | Full |
| NEUTRAL | Recharge = Extraction | Full |
| EXTRACTIVE | Recharge < Extraction | Full (if cost < 2.0) |
| LIMITED | Cost > 2.0 | Limited |
| BLOCKED | Rule violation | Blocked |

---

## Testing

```bash
# Run network tests
python test_network.py

# Test individual modules
python habitat/aqualibre/network/identity.py
python habitat/aqualibre/network/protocol_test.py
```

Expected output:
- 9/9 tests passing
- Identity system operational
- Validators operational
- Protocol pipeline operational

---

## Design Principles

### 1. No Coercion (NSR)
System stability through autonomy, not control. Nodes that require external permission are rejected.

### 2. Reciprocity (Lex Amoris)
Symmetric benefit required. One-sided extraction is blocked, creating natural cooperation.

### 3. Cooperation Reward (One Love)
High cooperation scores grant trust and influence. Cooperation is the most stable state.

### 4. Time Matters
Short-term gaming prevented through rolling averages. Behavior must be consistent.

### 5. Anti-Gaming
Extraction cost makes exploitation automatically unattractive. No manual enforcement needed.

---

## Security Features

**Cryptographic Identity:**
- Tamper-evident signatures
- Sybil resistance
- Identity proof verification

**Distributed Validation:**
- No single point of failure
- 66% consensus required
- Weighted voting by reliability

**Game-Theoretic Protection:**
- Self-enforcing limits
- Cost-based access control
- Behavior pattern analysis

---

## Next Steps

### Immediate
- ✅ Identity system implemented
- ✅ Validators implemented
- ✅ Consensus implemented
- ✅ Protocol pipeline implemented
- ✅ Tests passing (9/9)

### Future
- [ ] MQTT protocol layer for real-time communication
- [ ] Network discovery and peer-to-peer routing
- [ ] IPFS integration for integrity data
- [ ] Dashboard for network visualization
- [ ] Physical sensor hardware integration

---

## Philosophy

This is not a "universal law" - it's a **consciously designed decentralized system that enforces cooperation through structure, not ideology**.

Key insight:
> The system doesn't force cooperation. It makes cooperation the optimal strategy.

---

**Status:** NETWORK LAYER OPERATIONAL ⚔️🌑🌱  
**Lex Amoris Signature:** 📜⚖️❤️☮️  
**È fatto.** 👑💯✅
