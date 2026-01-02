const inputCampo = document.getElementById('ticketInput');
const bottone = document.getElementById('checkBtn');
const boxRisultato = document.getElementById('resultBox');
const titoloRisultato = document.getElementById('resultTitle');
const messaggioRisultato = document.getElementById('resultMessage');
const boxStatistiche = document.getElementById('liveStats');

async function verificaBiglietto() {
    
    const codice = inputCampo.value.trim();

    if (codice === "") {
        alert("Inserisci un codice!");
        return;
    }

    try {
        const risposta = await fetch(`http://127.0.0.1:8000/check-access/${codice}`, {
            method: 'POST'
        });

        const dati = await risposta.json();

        mostraRisultato(dati);
        await aggiornaContatore();

    } catch (errore) {
        console.error("Errore:", errore);
        alert("Errore di connessione con il server.");
    }

    inputCampo.value = "";
    inputCampo.focus();
}

async function aggiornaContatore() {
    try {
        const risposta = await fetch('http://127.0.0.1:8000/stats');
        const dati = await risposta.json();
        boxStatistiche.innerText = `${dati.checkedIn} / ${dati.total}`;

    } catch (errore) {
        console.error("Impossibile aggiornare statistiche:", errore);
        boxStatistiche.innerText = "Err";
    }
}

function mostraRisultato(dati) {
    boxRisultato.classList.remove('hidden');
    boxRisultato.classList.remove('bg-green-100', 'border-green-500', 'text-green-800');
    boxRisultato.classList.remove('bg-red-100', 'border-red-500', 'text-red-800');

    if (dati.result === "OK") {
        boxRisultato.classList.add('bg-green-100', 'border-green-500', 'text-green-800');
        titoloRisultato.innerText = "ACCESSO CONSENTITO";
        messaggioRisultato.innerText = "Benvenuto, " + dati.user_name;
    } else {
        boxRisultato.classList.add('bg-red-100', 'border-red-500', 'text-red-800');
        titoloRisultato.innerText = "ACCESSO NEGATO";
        messaggioRisultato.innerText = dati.message; 
        
        if(dati.user_name) {
            messaggioRisultato.innerText += " (" + dati.user_name + ")";
        }
    }
}

bottone.addEventListener('click', verificaBiglietto);

inputCampo.addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        verificaBiglietto();
    }
});

aggiornaContatore();