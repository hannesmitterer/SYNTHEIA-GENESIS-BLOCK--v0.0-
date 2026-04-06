from vacuum_node.reputation import weight

def adjust_beta(node_id: str, ph: float, myzel: float, beta: float) -> float:
    ph_target = 6.5
    myzel_target = 0.85

    ph_err = ph_target - ph
    myzel_err = myzel_target - myzel

    # Basis‑Korrektur
    delta = 0.02 * ph_err + 0.03 * myzel_err

    # Reputation‑Weighting (w∈[0.1,1.0])
    w = weight(node_id)
    beta_new = beta + w * delta

    # Begrenzung auf sinnvolle Grenzen
    return max(0.05, min(beta_new, 0.5))
