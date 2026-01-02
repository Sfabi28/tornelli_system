from fastapi import FastAPI #libreria per API
from pydantic import BaseModel #libreria per validazione dati
from fastapi.middleware.cors import CORSMiddleware #libreria per CORS
from typing import Optional #libreria per tipi opzionali (nome None)
from io import BytesIO #libreria per gestione byte stream
import qrcode #libreria per generazione QR code
from fastapi.responses import StreamingResponse #libreria per risposte in streaming

app = FastAPI() #creazione istanza FastAPI


app.add_middleware( #middleware per CORS permette di fare richieste da qualsiasi origine
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

database_tickets = { #simulazione database
    "CODE123": {"name": "Mario Rossi", "checked_in": False},
    "CODE456": {"name": "Luigi Verdi", "checked_in": True},
    "CODE789": {"name": "Anna Bianchi", "checked_in": False},
}

class AccessResponse(BaseModel): #modello di risposta, ogni return avra questi campi
    result: str
    message: str
    user_name: Optional[str] = None

class StatsResponse(BaseModel): #modello di risposta, ogni return avra questi campi
    total: int
    checkedIn: int

@app.post("/check-access/{ticket_code}", response_model=AccessResponse) #endpoint POST per controllo accesso

def check_access(ticket_code: str): #funzione che gestisce la richiesta di entrata
    
    guest = database_tickets.get(ticket_code) #ricerca codice nel "database"

    if not guest:
        return AccessResponse(
            result="DENIED",
            message="Invalid code"
        )

    if guest["checked_in"]:
        return AccessResponse(
            result="DENIED",
            message="TICKET ALREADY USED",
            user_name=guest["name"]
        )

    guest["checked_in"] = True
    
    return AccessResponse(
        result="OK",
        message="WELCOME",
        user_name=guest["name"]
    )

@app.get("/stats", response_model=StatsResponse)
def get_stats():

    total_tickets = len(database_tickets)

    entered_count = sum(1 for guest in database_tickets.values() if guest["checked_in"])
    
    return StatsResponse(
        total=total_tickets,
        checkedIn=entered_count
    )

@app.get("/generate-qr")
def generate_qr(qr_code: str):
    database_tickets[qr_code] = {"name": "Nuovo Ospite", "checked_in": False}

    img = qrcode.make(qr_code)

    buffer = BytesIO()
    img.save(buffer)

    buffer.seek(0)

    return StreamingResponse(buffer, media_type="image/png")
    
    
