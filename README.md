# 🎟️ Event Access Control System

Sistema di controllo accessi ad alte prestazioni per eventi, fiere e congressi.
Progettato per gestire flussi veloci, prevenire frodi (anti-passback) e fornire statistiche in tempo reale.

![Status](https://img.shields.io/badge/Status-Prototype-orange)
![Tech](https://img.shields.io/badge/Backend-FastAPI-green)
![Tech](https://img.shields.io/badge/Frontend-TailwindCSS-blue)

## 🚀 Funzionalità Chiave

* **Validazione Istantanea:** Risposte in <50ms tramite API REST.
* **Anti-Passback:** Impedisce che lo stesso biglietto venga usato due volte (prevenzione frodi).
* **Interfaccia Operatore:** UI ottimizzata per tablet e dispositivi touch ai varchi.
* **Real-time Analytics:** (In sviluppo) Monitoraggio presenze e flussi in tempo reale.

## 🛠️ Tecnologie Utilizzate

* **Backend:** Python 3.10+, FastAPI (per performance asincrone).
* **Frontend:** HTML5, Vanilla JS, Tailwind CSS (per UI responsive senza build tools pesanti).
* **Data:** In-Memory Storage (facilmente scalabile a Redis/PostgreSQL).

## ⚡ Quick Start

Se vuoi provare il tornello in locale:

1.  **Clona la repository**
    ```bash
    git clone [https://github.com/TuoUtente/tornelli-system.git](https://github.com/TuoUtente/tornelli-system.git)
    cd tornelli-system
    ```

2.  **Prepara l'ambiente**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Su Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3.  **Avvia il Server**
    ```bash
    uvicorn main:app --reload
    ```
    Il sistema sarà attivo su: `http://127.0.0.1:8000`

## 🧪 Testare il sistema
Puoi usare i seguenti codici demo:
* `CODE123` -> Biglietto Valido (Mario Rossi)
* `CODE456` -> Biglietto Già Usato (Luigi Verdi)
* `CODE999` -> Biglietto Inesistente
