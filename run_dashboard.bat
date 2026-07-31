@echo off
echo ===================================================
echo   Doctor AI Studio & Booking Management System
echo ===================================================
echo.

echo [1/3] Checking dependencies...
pip install -r requirements.txt
call npm install

echo [2/3] Starting WhatsApp Web QR Service on Port 5000...
start /b node whatsapp_qr_service.js

timeout /t 3 >nul

echo [3/3] Starting Doctor AI Dashboard Server on Port 8080...
echo.
echo Open your browser at: http://localhost:8080
echo ===================================================
python server.py
pause
