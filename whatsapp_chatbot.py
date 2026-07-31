import sqlite3
import datetime
import logging
from typing import Dict, Any, Tuple
from database import DB_PATH, get_settings
from schedule_engine import ScheduleEngine

logger = logging.getLogger("WhatsAppChatbot")

class WhatsAppChatbot:
    def __init__(self, schedule_engine: ScheduleEngine):
        self.schedule_engine = schedule_engine
        self.chat_sessions: Dict[str, Dict[str, Any]] = {}

    def process_incoming_message(self, sender_phone: str, message_text: str) -> str:
        text = message_text.strip()
        text_lower = text.lower()
        
        session = self.chat_sessions.get(sender_phone, {"step": "GREETING", "patient_name": None})
        step = session.get("step")

        settings = get_settings()
        doctor_name = settings.get("doctor_name", "Dr. A. J. Sakhrelia")
        doctor_phone = settings.get("doctor_phone", "+919099555744")

        # Restart trigger
        if text_lower in ["hi", "hello", "hey", "નમસ્તે", "start", "restart", "0"]:
            self.chat_sessions[sender_phone] = {"step": "COLLECT_NAME", "patient_name": None}
            return (
                f"👋 *નમસ્તે! ડૉ. {doctor_name} ના ક્લિનિકમાં તમારું સ્વાગત છે.*\n\n"
                f"હું એઆઈ એસિસ્ટન્ટ છું. એપોઇન્ટમેન્ટ બુક કરવા માટે કૃપા કરીને તમારું પૂરું નામ જણાવશો?"
            )

        if step == "COLLECT_NAME":
            session["patient_name"] = text
            session["step"] = "COLLECT_SLOT"
            self.chat_sessions[sender_phone] = session

            today = datetime.date.today()
            days_ahead = 0 - today.weekday()
            if days_ahead <= 0: days_ahead += 7
            next_mon = (today + datetime.timedelta(days=days_ahead)).strftime("%Y-%m-%d")
            session["date"] = next_mon

            return (
                f"આભાર {text} જી! 🙏\n\n"
                f"📅 *આવતા સોમવાર ({next_mon}) ના રોજ આ સ્લોટ્સ ઉપલબ્ધ છે:*\n"
                f"1️⃣ 09:00 AM\n"
                f"2️⃣ 10:00 AM\n"
                f"3️⃣ 11:00 AM\n"
                f"4️⃣ 02:00 PM\n"
                f"5️⃣ 04:00 PM\n\n"
                f"કૃપા કરીને તમારો પસંદગીનો સમય (દા.ત. 10 AM) લખીને મોકલો."
            )

        elif step == "COLLECT_SLOT":
            selected_slot = "10:00 AM"
            for slot in ["09:00 AM", "10:00 AM", "11:00 AM", "12:00 PM", "02:00 PM", "03:00 PM", "04:00 PM", "05:00 PM"]:
                if slot.lower().replace(" ", "") in text_lower.replace(" ", ""):
                    selected_slot = slot
                    break

            patient_name = session.get("patient_name", "પ્રિય દર્દી")
            date_str = session.get("date", datetime.date.today().strftime("%Y-%m-%d"))

            # Book in SQLite & Send Doctor Alert automatically
            booking_res = self.schedule_engine.book_appointment(
                patient_name=patient_name,
                patient_phone=sender_phone,
                date_str=date_str,
                time_slot=selected_slot
            )

            # Reset Chat Session
            self.chat_sessions.pop(sender_phone, None)

            return (
                f"✅ *એપોઇન્ટમેન્ટ કન્ફર્મ થઈ ગઈ છે!*\n\n"
                f"👤 દર્દી: {patient_name}\n"
                f"👨‍⚕️ ડૉક્ટર: Dr. {doctor_name}\n"
                f"📅 તારીખ: {date_str}\n"
                f"⏰ સમય: {selected_slot}\n"
                f"🆔 એપોઇન્ટમેન્ટ નંબર: {booking_res['appointment_id']}\n\n"
                f"📍 *ક્લિનિક લોકેશન:* https://maps.google.com/?q=21.1702,72.8311 (Surat, Gujarat)\n\n"
                f"આભાર! સમયસર પહોંચવા વિનંતી."
            )

        # Default fallback
        return f"નમસ્તે! એપોઇન્ટમેન્ટ બુક કરવા માટે 'Hi' અથવા 'નમસ્તે' મોકલો."

if __name__ == "__main__":
    from schedule_engine import ScheduleEngine
    engine = ScheduleEngine()
    bot = WhatsAppChatbot(engine)
    print("Bot Greeting:", bot.process_incoming_message("+919876543210", "Hi"))
    print("Bot Name:", bot.process_incoming_message("+919876543210", "Aashit Sakhrelia"))
    print("Bot Slot:", bot.process_incoming_message("+919876543210", "10 AM"))
