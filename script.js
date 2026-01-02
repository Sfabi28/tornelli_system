
const inputCampo = document.getElementById('ticketInput');
const bottone = document.getElementById('checkBtn');
const boxRisultato = document.getElementById('resultBox');
const titoloRisultato = document.getElementById('resultTitle');
const messaggioRisultato = document.getElementById('resultMessage');

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

    } catch (errore) {
        console.error("Errore di connessione:", errore);
        alert("Impossibile contattare il server! Controlla se main.py è aperto.");
    }

    inputCampo.value = "";
    inputCampo.focus();
}


function mostraRisultato(dati) {

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

    boxRisultato.classList.remove('hidden');
}

bottone.addEventListener('click', verificaBiglietto);

inputCampo.addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        verificaBiglietto();
    }
});