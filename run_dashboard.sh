#!/bin/bash
echo "==================================================="
echo "  Doctor AI Studio & Booking Management System"
echo "==================================================="
echo ""

echo "[1/3] Installing Python & Node dependencies..."
pip install -r requirements.txt
npm install

echo "[2/3] Starting WhatsApp Web QR Service on Port 5000..."
node whatsapp_qr_service.js &

sleep 3

echo "[3/3] Starting Doctor AI Dashboard Server on Port 8080..."
echo ""
echo "Open your browser at: http://localhost:8080"
echo "==================================================="
python3 server.py
