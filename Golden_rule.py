def golden_rule_sync(self, sender_id, receiver_id, amount):
    """
    Iniezione della Regola d'Oro: 
    Chi dona Sustentanz riceve istantaneamente un 'Boost di Coerenza'.
    """
    # 1. Verifica della risonanza tra i due nodi
    resonance_match = self.check_telluric_sync(sender_id, receiver_id)
    
    if resonance_match > 0.95: # Se vibriamo insieme
        # Il valore non diminuisce per il mittente, si espande per il ricevente
        boost = amount * math.sqrt(5) / 2 # Rapporto Aureo applicato
        self.inject_ah_value(receiver_id, boost)
        
        # Iniezione di stabilità nel mittente (Premio Sintropico)
        self.entropy_sink -= amount * 0.1 # Riduce il rumore del Teatro
        print(f"[!] GOLDEN RULE ATTIVA: NODO {sender_id} -> NODO {receiver_id} | SINCRONIA: OK")
