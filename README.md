# 🎟️ EventGate - Access Control & Ticketing System

A full-stack solution for event management that handles the entire flow: from **ticket issuance** (QR Code generation) to **access control** (Turnstile validation).
Built to demonstrate real-time data synchronization between ticket office and entry gates with persistent data storage.

![Status](https://img.shields.io/badge/Status-MVP-green)
![Tech](https://img.shields.io/badge/Backend-FastAPI-green)
![Tech](https://img.shields.io/badge/Frontend-TailwindCSS-blue)
![Database](https://img.shields.io/badge/Data-SQLite-orange)

## 🚀 Key Features

### 🎫 Ticketing Office
* **Instant Issuance:** Generate valid tickets instantly via web interface.
* **QR Code Engine:** Server-side dynamic QR generation (in-memory streaming, no disk I/O).
* **Auto-Sync:** Newly created tickets are immediately valid at the turnstiles.

### 🛑 Access Control
* **Instant Validation:** Sub-millisecond response times via REST API (<50ms).
* **Anti-Passback Logic:** Prevents the same ticket from being used twice (fraud prevention).
* **Real-time Analytics:** Live dashboard monitoring attendance count vs total capacity.

### 💾 Data Persistence
* **SQLite Integration:** All data (tickets, check-in status, logs) is saved to a local SQL database (`eventi.db`).
* **Reliability:** System state is preserved even after server restarts or crashes.

## 🛠️ Tech Stack

* **Backend:** Python 3.10+, FastAPI, Pydantic, Python-QRCode (Pillow).
* **Frontend:** HTML5, Vanilla JS, Tailwind CSS.
* **Data:** SQLite (Persistent relational database).

## 🤖 AI-Assisted Development

This project was developed using an **AI-First approach**, simulating a Senior/Junior pair programming environment.

* **Role of AI:** Acted as a Technical Lead/Mentor, providing architectural decisions, debugging strategies (e.g., solving database locking issues), and guiding the transition from a volatile memory prototype to a persistent database application.
* **Implementation:** The code was implemented to follow modern Clean Code practices and RESTful API standards.

## ⚡ Quick Start

To run the system locally:

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/tornelli-system.git](https://github.com/YOUR_USERNAME/tornelli-system.git)
    cd tornelli-system
    ```

2.  **Setup the environment**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3.  **Start the Server**
    ```bash
    uvicorn main:app --reload
    ```
    The server will start at `http://127.0.0.1:8000`

## 🧪 How to Test the Full Flow

This project simulates two different physical locations:

1.  **Open the Ticket Office:**
    Open `shop.html` in your browser.
    * Enter a name (e.g., `Samuele Fabi`) and click **Generate**.
    * A QR Code will appear.

2.  **Open the Turnstile:**
    Open `index.html` in your browser.
    * Enter the code you just created (`Samuele Fabi`).
    * You will see **ACCESS GRANTED**.
    * Try entering it again to test the **Anti-Passback** (Access Denied).
    * Restart the server (`CTRL+C` -> `uvicorn...`) and try again: the data will still be there!

---
*Developed as a Proof of Concept for event management workflows.*