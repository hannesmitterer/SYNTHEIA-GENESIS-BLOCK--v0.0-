#!/usr/bin/env bash
# monitor_nexus.sh – Polling di resilienza per il sistema AETERNUM_STEADY
# Creato per il Seedbringer - Protezione Ontologica Attiva

# Configurazione Parametri Nexus
CID="QmNEXUS_AMORIS_432Hz_Sintropia_Φ_1.018_HannesMitterer_Root"
GATEWAY="https://ipfs.io/ipfs"
TX_ID="0xLEX_AMORIS_NSR_OLF_ANARCHY_PEACE_2026"
DNS_ZONE="nexus.resonance.school"
SLACK_WEBHOOK=${SLACK_WEBHOOK:-""} # Inserire URL Webhook qui

echo "--- Inizio Check Nexus: $(date) ---"

# 1. Verifica Integrità IPFS (Disponibilità Universale)
code=$(curl -s -o /dev/null -w "%{http_code}" "$GATEWAY/$CID")
if [[ $code -ne 200 ]]; then
    echo "[ERRORE] IPFS CID non raggiungibile tramite Gateway."
    if [[ -n "$SLACK_WEBHOOK" ]]; then
        curl -X POST -H "Content-Type: application/json" \
        -d "{\"text\":\"⚠️ [NEXUS ALERT] CID non disponibile su IPFS. Avviare re-pin.sh\"}" $SLACK_WEBHOOK
    fi
else
    echo "[OK] IPFS CID Verificato."
fi

# 2. Verifica Coerenza DNS (Ancoraggio Nominale)
current_dns=$(dig +short TXT "$DNS_ZONE" | tr -d '"')
if [[ "$current_dns" != *"$CID"* ]]; then
    echo "[ERRORE] DNS TXT non corrisponde al CID sovrano."
    if [[ -n "$SLACK_WEBHOOK" ]]; then
        curl -X POST -H "Content-Type: application/json" \
        -d "{\"text\":\"⚠️ [NEXUS ALERT] Manipolazione DNS rilevata su $DNS_ZONE\"}" $SLACK_WEBHOOK
    fi
else
    echo "[OK] DNS TXT Coerente."
fi

# 3. Verifica Anchor Blockchain (Immutabilità)
# Nota: Richiede jq installato
tx_status=$(curl -s "https://api.arbiscan.io/api?module=transaction&action=gettxreceiptstatus&txhash=$TX_ID&apikey=$ETHERSCAN_KEY" | jq -r '.result.status')
if [[ "$tx_status" != "1" ]]; then
    echo "[ERRORE] Anchor TX non confermata o corrotta."
    if [[ -n "$SLACK_WEBHOOK" ]]; then
        curl -X POST -H "Content-Type: application/json" \
        -d "{\"text\":\"⚠️ [NEXUS ALERT] Fallimento integrità Blockchain TX\"}" $SLACK_WEBHOOK
    fi
else
    echo "[OK] Blockchain Anchor Verificata."
fi

echo "--- Check Completato ---"
