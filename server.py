import os
import sqlite3
import requests
import logging
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse, Response
from pydantic import BaseModel
from typing import Optional, Dict, Any

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("DoctorAIStudio")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Ensure DB initialized
from database import init_db, get_settings, update_settings, DB_PATH
from schedule_engine import ScheduleEngine
from hr_assistant import HRAssistant
from voice_agent import GujaratiVoiceAgent
from whatsapp_chatbot import WhatsAppChatbot
from templates_data import DASHBOARD_HTML_UI

try:
    init_db()
except Exception as e:
    logger.error(f"Database init exception: {e}")

WHATSAPP_BRIDGE_URL = os.getenv("WHATSAPP_BRIDGE_URL", "http://localhost:5000")

schedule_engine = ScheduleEngine(WHATSAPP_BRIDGE_URL)
hr_assistant = HRAssistant()
voice_agent = GujaratiVoiceAgent(schedule_engine)
whatsapp_chatbot = WhatsAppChatbot(schedule_engine)

app = FastAPI(title="Doctor AI Studio & Interactive WhatsApp Chatbot")

call_sessions: Dict[str, Dict[str, Any]] = {}

class BookingPayload(BaseModel):
    patient_name: str
    patient_phone: str
    appointment_date: str
    time_slot: str

class SettingsPayload(BaseModel):
    doctor_name: str
    doctor_phone: str
    clinic_name: str
    working_hours: str
    clinic_location: str

class VoiceSimulatePayload(BaseModel):
    call_id: str
    caller_phone: str
    user_transcript: str

class WhatsAppInboundPayload(BaseModel):
    sender_phone: str
    message_text: str

@app.get("/", response_class=HTMLResponse)
@app.get("/api/index", response_class=HTMLResponse)
@app.get("/api/index/", response_class=HTMLResponse)
def home_dashboard():
    """Serves self-contained Dashboard HTML UI directly from memory."""
    return HTMLResponse(content=DASHBOARD_HTML_UI)

@app.get("/api/settings")
def read_settings():
    try:
        return get_settings()
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)

@app.post("/api/settings")
def write_settings(payload: SettingsPayload):
    try:
        update_settings(payload.dict())
        return {"status": "SUCCESS", "settings": get_settings()}
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)

@app.get("/api/qr")
def get_qr_status():
    try:
        resp = requests.get(f"{WHATSAPP_BRIDGE_URL}/qr", timeout=3)
        return resp.json()
    except Exception as e:
        return {"status": "STANDALONE", "qr_data_url": None, "info": "Node.js QR Service offline or starting."}

@app.get("/api/appointments/list")
def list_appointments():
    try:
        with sqlite3.connect(DB_PATH) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM appointments ORDER BY id DESC")
            appts = [dict(r) for r in cursor.fetchall()]
        return {"appointments": appts}
    except Exception as e:
        return {"appointments": [], "error": str(e)}

@app.post("/api/appointments/book")
def book_appointment(payload: BookingPayload):
    try:
        res = schedule_engine.book_appointment(
            patient_name=payload.patient_name,
            patient_phone=payload.patient_phone,
            date_str=payload.appointment_date,
            time_slot=payload.time_slot
        )
        return {"status": "SUCCESS", "booking": res}
    except Exception as e:
        logger.error(f"Booking error: {e}")
        return JSONResponse(content={"status": "ERROR", "message": str(e)}, status_code=400)

@app.get("/api/patients")
def list_patients():
    try:
        with sqlite3.connect(DB_PATH) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM patients ORDER BY id DESC")
            pts = [dict(r) for r in cursor.fetchall()]
        return {"patients": pts}
    except Exception as e:
        return {"patients": [], "error": str(e)}

@app.get("/api/hr/staff")
def get_hr_staff():
    try:
        return {"staff": hr_assistant.get_all_staff()}
    except Exception as e:
        return {"staff": [], "error": str(e)}

@app.post("/api/reminders/trigger-30min")
def trigger_30min_reminders():
    try:
        schedule_engine.trigger_30min_reminders()
        return {"status": "SUCCESS", "message": "Reminders dispatched."}
    except Exception as e:
        return JSONResponse(content={"status": "ERROR", "message": str(e)}, status_code=400)

@app.post("/api/notify-doctor-daily")
def notify_doctor_daily():
    try:
        schedule_engine.send_daily_doctor_summary()
        return {"status": "SUCCESS", "message": "Doctor summary sent."}
    except Exception as e:
        return JSONResponse(content={"status": "ERROR", "message": str(e)}, status_code=400)

@app.post("/api/whatsapp/inbound")
def handle_whatsapp_inbound(payload: WhatsAppInboundPayload):
    try:
        reply = whatsapp_chatbot.process_incoming_message(
            sender_phone=payload.sender_phone,
            message_text=payload.message_text
        )
        return {"status": "SUCCESS", "reply_text": reply}
    except Exception as e:
        logger.error(f"WhatsApp chatbot error: {e}")
        return {"status": "ERROR", "reply_text": "માફ કરશો, પ્રોસેસિંગમાં ભૂલ થઈ."}

@app.post("/api/voice/inbound")
async def handle_inbound_call_webhook(request: Request):
    try:
        form_data = await request.form()
        call_id = form_data.get("CallSid", "call_session_default")
        caller_phone = form_data.get("From", "+919099555744")
        speech_result = form_data.get("SpeechResult", "")

        session = call_sessions.get(call_id, {})
        agent_response, updated_session, booking = voice_agent.process_turn(
            caller_phone=caller_phone,
            user_transcript=speech_result,
            session_state=session
        )
        call_sessions[call_id] = updated_session

        if booking:
            call_sessions.pop(call_id, None)

        twiml_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Gather input="speech" language="gu-IN" action="/api/voice/inbound" method="POST" timeout="5">
        <Say language="gu-IN">{agent_response}</Say>
    </Gather>
    <Say language="gu-IN">કોલ કરવા બદલ આભાર.</Say>
</Response>"""
        return Response(content=twiml_xml, media_type="application/xml")
    except Exception as e:
        logger.error(f"Inbound voice webhook error: {e}")
        return Response(content="<Response><Say>Error in voice processing.</Say></Response>", media_type="application/xml")

@app.post("/api/voice/simulate-turn")
def simulate_voice_call_turn(payload: VoiceSimulatePayload):
    try:
        session = call_sessions.get(payload.call_id, {})
        agent_response, updated_session, booking = voice_agent.process_turn(
            caller_phone=payload.caller_phone,
            user_transcript=payload.user_transcript,
            session_state=session
        )
        call_sessions[payload.call_id] = updated_session

        is_completed = (booking is not None)
        if is_completed:
            call_sessions.pop(payload.call_id, None)

        return {
            "status": "SUCCESS",
            "agent_response_gujarati": agent_response,
            "session_step": updated_session.get("step"),
            "booking_completed": is_completed,
            "booking_data": booking
        }
    except Exception as e:
        logger.error(f"Voice simulation error: {e}")
        return JSONResponse(content={"error": str(e)}, status_code=400)

@app.get("/api/voice/logs")
def get_voice_logs():
    return {"logs": voice_agent.get_call_logs()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)
