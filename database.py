import sqlite3
import os
import tempfile
from typing import Dict, Any, List

# On Vercel/AWS Lambda, use /tmp (the only writable directory). On local, use script directory.
if os.getenv("VERCEL") or os.getenv("AWS_LAMBDA_FUNCTION_NAME"):
    DB_PATH = os.path.join(tempfile.gettempdir(), "doctor_studio.db")
else:
    DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "doctor_studio.db")

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        
        # 1. Doctor Settings Table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS doctor_settings (
                key TEXT PRIMARY KEY,
                value TEXT
            )
        ''')
        
        # Default Settings
        default_settings = {
            "doctor_name": "Dr. A. J. Sakhrelia",
            "doctor_phone": "+919099555744",
            "clinic_name": "Arogya Healthcare & Diagnostic Center",
            "clinic_location": "https://maps.google.com/?q=21.1702,72.8311 (Vesu Main Road, Surat, Gujarat)",
            "working_hours": "09:00 AM - 05:00 PM (Mon-Sat)",
            "dashboard_language": "en"
        }
        for k, v in default_settings.items():
            cursor.execute("INSERT OR IGNORE INTO doctor_settings (key, value) VALUES (?, ?)", (k, v))

        # 2. Appointments Table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS appointments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                appointment_id TEXT UNIQUE,
                doctor_name TEXT,
                patient_name TEXT,
                patient_phone TEXT,
                appointment_date TEXT,
                time_slot TEXT,
                status TEXT DEFAULT 'BOOKED',
                reminder_sent INTEGER DEFAULT 0,
                doctor_notified INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # 3. Patients Table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS patients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                phone TEXT UNIQUE,
                total_visits INTEGER DEFAULT 1,
                last_visit TEXT,
                notes TEXT
            )
        ''')

        # 4. Staff Table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS staff (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                role TEXT NOT NULL,
                phone TEXT,
                shift_timing TEXT,
                status TEXT DEFAULT 'ACTIVE'
            )
        ''')

        # 5. Voice Call Logs Table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS voice_call_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                caller_phone TEXT,
                transcript TEXT,
                agent_response TEXT,
                status TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # Seed Staff if empty
        cursor.execute("SELECT COUNT(*) FROM staff")
        if cursor.fetchone()[0] == 0:
            default_staff = [
                ("Priyanka Shah", "Head Receptionist & Billing", "+919800011111", "08:30 AM - 05:30 PM"),
                ("Vikram Parmar", "Clinic Assistant & Compounder", "+919800022222", "09:00 AM - 06:00 PM"),
                ("Neha Joshi", "Nursing Staff", "+919800033333", "08:00 AM - 04:00 PM")
            ]
            cursor.executemany("INSERT INTO staff (name, role, phone, shift_timing) VALUES (?, ?, ?, ?)", default_staff)

        conn.commit()

def get_settings() -> Dict[str, str]:
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT key, value FROM doctor_settings")
        return dict(cursor.fetchall())

def update_settings(settings_dict: Dict[str, str]):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        for k, v in settings_dict.items():
            cursor.execute("INSERT OR REPLACE INTO doctor_settings (key, value) VALUES (?, ?)", (k, v))
        conn.commit()

if __name__ == "__main__":
    init_db()
    print("Database initialized at DB_PATH:", DB_PATH)
