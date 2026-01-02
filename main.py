from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from io import BytesIO
import qrcode
from fastapi.responses import StreamingResponse
import sqlite3

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def init_db():
    conn = sqlite3.connect("eventi.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            code TEXT PRIMARY KEY,
            name TEXT,
            checked_in INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

init_db()


class AccessResponse(BaseModel):
    result: str
    message: str
    user_name: Optional[str] = None

class StatsResponse(BaseModel):
    total: int
    checkedIn: int


@app.post("/check-access/{ticket_code}", response_model=AccessResponse)
def check_access(ticket_code: str):
    
    conn = sqlite3.connect("eventi.db")
    cursor = conn.cursor()

    res = cursor.execute("SELECT name, checked_in FROM tickets WHERE code = ?", (ticket_code,))
    data = res.fetchone()

    if data is None:
        conn.close()
        return AccessResponse(
            result="DENIED",
            message="CODICE NON TROVATO"
        )
    
    nome_ospite = data[0]
    stato_ingresso = data[1]

    if stato_ingresso == 1:
        conn.close()
        return AccessResponse(
            result="DENIED",
            message="BIGLIETTO GIÀ UTILIZZATO",
            user_name=nome_ospite
        )

    cursor.execute("UPDATE tickets SET checked_in = 1 WHERE code = ?", (ticket_code,))
    conn.commit()
    conn.close()

    return AccessResponse(
        result="OK",
        message="BENVENUTO",
        user_name=nome_ospite
    )


@app.get("/stats", response_model=StatsResponse)
def get_stats():
    conn = sqlite3.connect("eventi.db")
    cursor = conn.cursor()

    total = cursor.execute("SELECT COUNT(*) FROM tickets").fetchone()[0]

    entered_count = cursor.execute("SELECT COUNT(*) FROM tickets WHERE checked_in = 1").fetchone()[0]

    conn.close()

    return StatsResponse(
        total=total,
        checkedIn=entered_count
    )

@app.get("/generate-qr")
def generate_qr(qr_code: str):
    
    try:
        conn = sqlite3.connect("eventi.db")
        cursor = conn.cursor()
        
        cursor.execute("INSERT INTO tickets (code, name, checked_in) VALUES (?, ?, 0)", (qr_code, qr_code))
        
        conn.commit()
        conn.close()
    
    except sqlite3.IntegrityError:
        print(f"Attenzione: Il codice {qr_code} esisteva già nel database.")
    
    img = qrcode.make(qr_code)
    buffer = BytesIO()
    img.save(buffer)
    buffer.seek(0)

    return StreamingResponse(buffer, media_type="image/png")