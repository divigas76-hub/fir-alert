# FIR Alert - Versione iniziale
# Autore: divigas76-hub
# Descrizione: Script di esempio per avvisi e notifiche FIR

import time

def invia_notifica(messaggio):
    """Simula l'invio di una notifica FIR"""
    print(f"[FIR ALERT] {messaggio}")

if __name__ == "__main__":
    invia_notifica("Sistema FIR avviato correttamente.")
    while True:
        # Qui potrai aggiungere la logica di monitoraggio
        time.sleep(60)
        invia_notifica("Controllo completato: nessun evento rilevato.")
