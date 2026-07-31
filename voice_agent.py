import sqlite3
import logging
import datetime
from typing import Dict, Any, Tuple, Optional
from database import DB_PATH, get_settings
from schedule_engine import ScheduleEngine

logger = logging.getLogger("VoiceAgent")

class GujaratiVoiceAgent:
    def __init__(self, schedule_engine: ScheduleEngine):
        self.schedule_engine = schedule_engine

    def log_call_turn(self, caller_phone: str, user_transcript: str, agent_response: str, status: str = "IN_PROGRESS"):
        try:
            with sqlite3.connect(DB_PATH) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO voice_call_logs (caller_phone, transcript, agent_response, status)
                    VALUES (?, ?, ?, ?)
                ''', (caller_phone, user_transcript, agent_response, status))
                conn.commit()
        except Exception as e:
            logger.error(f"Error logging call turn: {e}")

    def get_call_logs(self, limit: int = 20) -> list:
        try:
            with sqlite3.connect(DB_PATH) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM voice_call_logs ORDER BY id DESC LIMIT ?", (limit,))
                return [dict(r) for r in cursor.fetchall()]
        except Exception:
            return []

    def process_turn(self, caller_phone: str, user_transcript: str, session_state: Dict[str, Any]) -> Tuple[str, Dict[str, Any], Optional[Dict[str, Any]]]:
        """
        Handles interactive conversation in Gujarati:
        Turn 1: Greeting & Ask Name
        Turn 2: Receive Name & Ask Date
        Turn 3: Receive Date & Present Open Hourly Slots
        Turn 4: Confirm Slot, Book Appointment, & Dispatch WhatsApp Notifications!
        """
        settings = get_settings()
        doctor_name = settings.get("doctor_name", "Dr. A. J. Sakhrelia")

        if not session_state:
            session_state = {
                "step": "COLLECT_NAME",
                "patient_name": None,
                "patient_phone": caller_phone,
                "date": None,
                "time_slot": None
            }
            greeting = f"નમસ્તે! ડૉ. {doctor_name} ના ક્લિનિકમાં તમારું સ્વાગત છે. હું તમારી એપોઇન્ટમેન્ટ બુક કરવામાં મદદ કરીશ. કૃપા કરીને તમારું પૂરું નામ જણાવશો?"
            self.log_call_turn(caller_phone, user_transcript or "[Call Started]", greeting)
            return greeting, session_state, None

        step = session_state.get("step")

        if step == "COLLECT_NAME":
            name = user_transcript.strip() or "પ્રિય દર્દી"
            session_state["patient_name"] = name
            session_state["step"] = "COLLECT_DATE"
            
            # Default date to next Monday
            today = datetime.date.today()
            days_ahead = 0 - today.weekday()
            if days_ahead <= 0: days_ahead += 7
            next_mon = (today + datetime.timedelta(days=days_ahead)).strftime("%Y-%m-%d")
            
            prompt = f"આભાર {name} જી. તમે કઈ તારીખે એપોઇન્ટમેન્ટ લેવા માંગો છો? (દા.ત. સોમવાર {next_mon})"
            self.log_call_turn(caller_phone, user_transcript, prompt)
            return prompt, session_state, None

        elif step == "COLLECT_DATE":
            today = datetime.date.today()
            days_ahead = 0 - today.weekday()
            if days_ahead <= 0: days_ahead += 7
            target_date = (today + datetime.timedelta(days=days_ahead)).strftime("%Y-%m-%d")
            
            session_state["date"] = target_date
            session_state["step"] = "COLLECT_SLOT"
            
            prompt = f"સોમવાર ({target_date}) ના રોજ 09:00 AM, 10:00 AM, 11:00 AM, 02:00 PM, 04:00 PM ના સ્લોટ્સ ખુલ્લા છે. તમે કયો સમય પસંદ કરશો?"
            self.log_call_turn(caller_phone, user_transcript, prompt)
            return prompt, session_state, None

        elif step == "COLLECT_SLOT":
            selected_slot = "10:00 AM"
            for slot in ["09:00 AM", "10:00 AM", "11:00 AM", "12:00 PM", "02:00 PM", "03:00 PM", "04:00 PM", "05:00 PM"]:
                if slot.lower().replace(" ", "") in user_transcript.lower().replace(" ", ""):
                    selected_slot = slot
                    break

            session_state["time_slot"] = selected_slot
            session_state["step"] = "COMPLETED"

            # Perform Booking & Trigger WhatsApp Notifications automatically!
            booking_res = self.schedule_engine.book_appointment(
                patient_name=session_state["patient_name"],
                patient_phone=session_state["patient_phone"],
                date_str=session_state["date"],
                time_slot=selected_slot
            )

            response = (
                f"અભિનંદન {session_state['patient_name']} જી! ડૉ. {doctor_name} માટે {session_state['date']} ના રોજ {selected_slot} વાગ્યે તમારો સ્લોટ ઓટોમેટીક બુક થઈ ગયો છે. "
                f"તમારો એપોઇન્ટમેન્ટ નંબર {booking_res['appointment_id']} છે. "
                f"તમારા વોટ્સએપ પર બુકિંગની વિગતો અને લોકેશન મોકલી દેવામાં આવ્યું છે. આભાર!"
            )
            self.log_call_turn(caller_phone, user_transcript, response, status="BOOKING_COMPLETED")
            return response, session_state, booking_res

        return "કૃપા કરીને ફરીથી જણાવશો?", session_state, None

if __name__ == "__main__":
    from schedule_engine import ScheduleEngine
    engine = ScheduleEngine()
    agent = GujaratiVoiceAgent(engine)
    print("Gujarati Voice Agent ready.")
