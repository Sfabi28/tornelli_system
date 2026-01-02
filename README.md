# 🎟️ EventGate - Access Control & Ticketing System

A full-stack solution for event management that handles the entire flow: from **ticket issuance** (QR Code generation) to **access control** (Turnstile validation).
Built to demonstrate real-time data synchronization between ticket office and entry gates.

![Status](https://img.shields.io/badge/Status-MVP-green)
![Tech](https://img.shields.io/badge/Backend-FastAPI-green)
![Tech](https://img.shields.io/badge/Frontend-TailwindCSS-blue)
![Module](https://img.shields.io/badge/Module-QRCode-lightgrey)

## 🚀 Key Features

### 🎫 Ticketing Office
* **Instant Issuance:** Generate valid tickets instantly via web interface.
* **QR Code Engine:** Server-side dynamic QR generation (in-memory streaming, no disk I/O).
* **Auto-Sync:** Newly created tickets are immediately valid at the turnstiles.

### 🛑 Access Control
* **Instant Validation:** Sub-millisecond response times via REST API (<50ms).
* **Anti-Passback Logic:** Prevents the same ticket from being used twice (fraud prevention).
* **Real-time Analytics:** Live dashboard monitoring attendance count vs total capacity.

## 🛠️ Tech Stack

* **Backend:** Python 3.10+, FastAPI, Pydantic, Python-QRCode (Pillow).
* **Frontend:** HTML5, Vanilla JS, Tailwind CSS.
* **Data:** In-Memory Storage (simulating a shared database).

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
    Open `biglietteria.html` in your browser.
    * Enter a name (e.g., `VIP-GUEST`) and click **Generate**.
    * A QR Code will appear.

2.  **Open the Turnstile:**
    Open `index.html` in your browser.
    * Enter the code you just created (`VIP-GUEST`).
    * You will see **ACCESS GRANTED**.
    * Try entering it again to test the **Anti-Passback** (Access Denied).

---
*Developed as a Proof of Concept for event management workflows.*