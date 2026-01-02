# 🎟️ Event Access Control System

High-performance access control system designed for events, trade shows, and conferences.
Built to handle fast attendee flows, prevent fraud (anti-passback), and provide real-time attendance statistics.

![Status](https://img.shields.io/badge/Status-Prototype-orange)
![Tech](https://img.shields.io/badge/Backend-FastAPI-green)
![Tech](https://img.shields.io/badge/Frontend-TailwindCSS-blue)

## 🚀 Key Features

* **Instant Validation:** Sub-millisecond response times via REST API (<50ms).
* **Anti-Passback Logic:** Prevents the same ticket from being used twice (fraud prevention).
* **Operator Interface:** Responsive UI optimized for tablets and touch devices at gates.
* **Real-time Analytics:** Live dashboard monitoring attendance count and capacity.

## 🛠️ Tech Stack

* **Backend:** Python 3.10+, FastAPI (for asynchronous high performance).
* **Frontend:** HTML5, Vanilla JS, Tailwind CSS (lightweight, no build tools required).
* **Data:** In-Memory Storage (designed to be easily scalable to Redis or PostgreSQL).

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
    The system will be live at: `http://127.0.0.1:8000`

## 🧪 Testing the System
You can use the following demo codes to test different scenarios:

* `CODE123` -> **Valid Ticket** (Mario Rossi) - *Returns Green/Access Granted*
* `CODE456` -> **Already Used** (Luigi Verdi) - *Returns Red/Access Denied (Anti-passback)*
* `CODE999` -> **Invalid Ticket** - *Returns Red/Access Denied*