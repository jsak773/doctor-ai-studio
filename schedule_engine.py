import sqlite3
import datetime
import requests
import logging
from typing import List, Dict, Any, Optional
from database import DB_PATH, get_settings

logger = logging.getLogger("ScheduleEngine")

class ScheduleEngine:
    def __init__(self, whatsapp_bridge_url: str = "http://localhost:5000"):
        self.whatsapp_bridge_url = whatsapp_bridge_url

    def send_whatsapp_msg(self, phone: str, message: str) -> bool:
        """
        Dispatches WhatsApp message:
        1. Logs to SQLite `whatsapp_outbox` table so messages are visible on Vercel/Cloud.
        2. Tries sending via Node.js QR bridge if running on Localhost.
        """
        # Step 1: Save to outbox DB so user can see all WhatsApp messages sent on Vercel live!
        try:
            with sqlite3.connect(DB_PATH) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS whatsapp_outbox (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        recipient_phone TEXT,
                        message_body TEXT,
                        status TEXT DEFAULT 'SENT',
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                ''')
                cursor.execute('''
                    INSERT INTO whatsapp_outbox (recipient_phone, message_body)
                    VALUES (?, ?)
                ''', (phone, message))
                conn.commit()
        except Exception as e:
            logger.error(f"Error saving to WhatsApp outbox: {e}")

        # Step 2: Try local Node.js bridge if available
        try:
            resp = requests.post(
                f"{self.whatsapp_bridge_url}/send-message",
                json={"number": phone, "message": message},
                timeout=2
            )
            return resp.status_code == 200
        except Exception:
            logger.info(f"[Pure Python WhatsApp Log for {phone}]:\n{message}")
            return True

    @staticmethod
    def get_hourly_slots() -> List[str]:
        return ["09:00 AM", "10:00 AM", "11:00 AM", "12:00 PM", "02:00 PM", "03:00 PM", "04:00 PM", "05:00 PM"]

    def book_appointment(self, patient_name: str, patient_phone: str, date_str: str, time_slot: str) -> Dict[str, Any]:
        settings = get_settings()
        doctor_name = settings.get("doctor_name", "Dr. A. J. Sakhrelia")
        doctor_phone = settings.get("doctor_phone", "+919099555744")
        clinic_name = settings.get("clinic_name", "Arogya Healthcare Center")
        clinic_loc = settings.get("clinic_location", "Surat, Gujarat")

        apt_id = f"APT-{date_str.replace('-', '')}-{time_slot.replace(':', '').replace(' ', '')}"

        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT OR REPLACE INTO appointments (appointment_id, doctor_name, patient_name, patient_phone, appointment_date, time_slot, status)
                VALUES (?, ?, ?, ?, ?, ?, 'BOOKED')
            ''', (apt_id, doctor_name, patient_name, patient_phone, date_str, time_slot))
            
            cursor.execute('''
                INSERT INTO patients (name, phone, last_visit) VALUES (?, ?, ?)
                ON CONFLICT(phone) DO UPDATE SET total_visits = total_visits + 1, last_visit = ?
            ''', (patient_name, patient_phone, date_str, date_str))
            
            conn.commit()

        # WhatsApp Message to Doctor (+91 9099555744)
        doc_msg = (
            f"🩺 *નવું એપોઇન્ટમેન્ટ બુક થયું છે*\n\n"
            f"👤 દર્દીનું નામ: {patient_name}\n"
            f"📞 ફોન નંબર: {patient_phone}\n"
            f"📅 તારીખ: {date_str}\n"
            f"⏰ સમય: {time_slot}\n"
            f"🆔 એપોઇન્ટમેન્ટ ID: {apt_id}"
        )
        self.send_whatsapp_msg(doctor_phone, doc_msg)

        # WhatsApp Message to Client
        patient_msg = (
            f"✅ *એપોઇન્ટમેન્ટ બુકિંગ કન્ફર્મેશન*\n\n"
            f"નમસ્તે {patient_name},\n"
            f"\"You have booked a slot for {doctor_name} at {time_slot} on {date_str}.\"\n\n"
            f"🏥 દવાખાનું/ક્લિનિક: {clinic_name}\n"
            f"📍 લોકેશન: {clinic_loc}\n"
            f"🆔 એપોઇન્ટમેન્ટ નંબર: {apt_id}\n"
            f"📞 તમારો મોબાઈલ નંબર: {patient_phone}"
        )
        self.send_whatsapp_msg(patient_phone, patient_msg)

        return {
            "appointment_id": apt_id,
            "patient_name": patient_name,
            "patient_phone": patient_phone,
            "date": date_str,
            "time_slot": time_slot,
            "status": "BOOKED"
        }

    def trigger_30min_reminders(self):
        today_str = datetime.datetime.now().strftime("%Y-%m-%d")

        with sqlite3.connect(DB_PATH) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute('''
                SELECT * FROM appointments 
                WHERE appointment_date = ? AND reminder_sent = 0 AND status = 'BOOKED'
            ''', (today_str,))
            appts = cursor.fetchall()

            for appt in appts:
                reminder_msg = (
                    f"⏰ *એપોઇન્ટમેન્ટ રિમાઇન્ડર (30 Min Reminder)*\n\n"
                    f"નમસ્તે {appt['patient_name']} જી,\n"
                    f"તમારો {appt['doctor_name']} સાથેનો એપોઇન્ટમેન્ટ સ્લોટ અડધી કલાકમાં ({appt['time_slot']}) છે. "
                    f"કૃપા કરીને સમયસર પહોંચવા વિનંતી.\n\n"
                    f"🆔 એપોઇન્ટમેન્ટ નંબર: {appt['appointment_id']}"
                )
                self.send_whatsapp_msg(appt['patient_phone'], reminder_msg)
                cursor.execute('UPDATE appointments SET reminder_sent = 1 WHERE id = ?', (appt['id'],))
            conn.commit()

    def send_daily_doctor_summary(self):
        settings = get_settings()
        doctor_name = settings.get("doctor_name", "Dr. A. J. Sakhrelia")
        doctor_phone = settings.get("doctor_phone", "+919099555744")
        today_str = datetime.date.today().strftime("%Y-%m-%d")

        with sqlite3.connect(DB_PATH) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM appointments WHERE appointment_date = ? AND status != "CANCELLED"', (today_str,))
            today_appts = cursor.fetchall()

        if not today_appts:
            summary = f"👨‍⚕️ {doctor_name}, આજે ({today_str}) માટે કોઈ એપોઇન્ટમેન્ટ શિડ્યુલ થયેલ નથી."
        else:
            list_text = "\n".join([f"• {a['time_slot']} - {a['patient_name']} ({a['patient_phone']})" for a in today_appts])
            summary = (
                f"📋 *આજના દર્દીઓનું લિસ્ટ ({today_str})*\n\n"
                f"{list_text}\n\n"
                f"કૃપા કરીને કોઈ ફેરફાર હોય તો ડેશબોર્ડમાંથી અપડેટ કરશો."
            )

        self.send_whatsapp_msg(doctor_phone, summary)

if __name__ == "__main__":
    engine = ScheduleEngine()
    print("Schedule Engine initialized.")
