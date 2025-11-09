#Library Management System

This is a Library Management System built using FastAPI and SQLAlchemy to manage books, users, and borrowing records efficiently.

##Tech Stack
- **FastAPI** — Web Framework
- **SQLAlchemy** — ORM for database operations
- **MySQL** — Database
- **Uvicorn** — ASGI server
- **Python** — Core programming language

##Installation Steps

### 1. Clone the repository
git clone https://github.com/your-username/LIBRARY_MANAGEMENT.git
cd LIBRARY_MANAGEMENT

Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate  # On Mac/Linux

Install dependencies
pip install -r requirements.txt

Setup environment variables
DATABASE_URL=mysql+pymysql://username:password@localhost/library_db

Run the application
uvicorn app.main:app --reload

#Project Structure

LIBRARY_MANAGEMENT/
│
├── app/
│   ├── main.py
│   ├── books.py
│   ├── users.py
│   ├── routers/
│   ├── schema/
│   ├── lib/
│   ├── models/
│   └── __pycache__/
│
├── .env
├── requirements.txt
└── README.md

Features
Add, update, and delete books
Manage users
Connect with a MySQL database
FastAPI endpoints for easy integration

#https://github.com/Bhavana-02052002/LIBRARY_MANAGEMENT



