const express = require('express');
const QRCode = require('qrcode');
const http = require('http');
const fs = require('fs');
const path = require('path');
const { Client, LocalAuth } = require('whatsapp-web.js');

const app = express();
app.use(express.json());

let currentQR = null;
let connectionStatus = 'INITIALIZING';
let client = null;

const SESSION_DIR = path.join(__dirname, 'whatsapp_auth_session');

function initWhatsAppClient() {
    connectionStatus = 'INITIALIZING';
    currentQR = null;

    client = new Client({
        authStrategy: new LocalAuth({ dataPath: SESSION_DIR }),
        puppeteer: {
            args: ['--no-sandbox', '--disable-setuid-sandbox']
        }
    });

    client.on('qr', (qr) => {
        connectionStatus = 'QR_READY';
        QRCode.toDataURL(qr, (err, url) => {
            if (!err) {
                currentQR = url;
                console.log('[WhatsApp Service] New QR Code generated.');
            }
        });
    });

    client.on('ready', () => {
        connectionStatus = 'AUTHENTICATED';
        currentQR = null;
        console.log('[WhatsApp Service] WhatsApp connected successfully!');
    });

    client.on('disconnected', (reason) => {
        connectionStatus = 'DISCONNECTED';
        currentQR = null;
        console.log('[WhatsApp Service] Disconnected:', reason);
    });

    client.on('message', async (msg) => {
        try {
            const senderPhone = msg.from.replace('@c.us', '');
            const messageBody = msg.body || '';

            const postData = JSON.stringify({
                sender_phone: senderPhone,
                message_text: messageBody
            });

            const req = http.request({
                hostname: 'localhost',
                port: 8080,
                path: '/api/whatsapp/inbound',
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Content-Length': Buffer.byteLength(postData)
                }
            }, (res) => {
                let data = '';
                res.on('data', (chunk) => data += chunk);
                res.on('end', async () => {
                    try {
                        const replyObj = JSON.parse(data);
                        if (replyObj.reply_text) {
                            await client.sendMessage(msg.from, replyObj.reply_text);
                        }
                    } catch (e) {
                        console.error('Error parsing backend reply:', e.message);
                    }
                });
            });

            req.on('error', (e) => console.error('Error contacting backend chatbot:', e.message));
            req.write(postData);
            req.end();

        } catch (err) {
            console.error('Error handling inbound message:', err.message);
        }
    });

    client.initialize().catch(err => {
        console.log('[WhatsApp Service] Initialization Note:', err.message);
    });
}

// Initial Client Launch
initWhatsAppClient();

app.get('/qr', (req, res) => {
    res.json({
        status: connectionStatus,
        qr_data_url: currentQR
    });
});

app.post('/disconnect', async (req, res) => {
    console.log('[WhatsApp Service] Disconnecting WhatsApp session requested...');
    try {
        if (client) {
            await client.logout().catch(() => {});
            await client.destroy().catch(() => {});
        }
        connectionStatus = 'DISCONNECTED';
        currentQR = null;

        // Clean up session directory if exists
        if (fs.existsSync(SESSION_DIR)) {
            fs.rmSync(SESSION_DIR, { recursive: true, force: true });
        }

        // Re-initialize client for fresh QR code
        setTimeout(() => {
            initWhatsAppClient();
        }, 1000);

        return res.json({ success: true, message: 'WhatsApp session disconnected. Scanning new QR code required.' });
    } catch (err) {
        console.error('Disconnect Error:', err.message);
        return res.status(500).json({ error: err.message });
    }
});

app.post('/send-message', async (req, res) => {
    const { number, message } = req.body;
    if (!number || !message) {
        return res.status(400).json({ error: 'Number and message required' });
    }

    const formattedNumber = number.replace(/[^0-9]/g, '') + '@c.us';

    try {
        if (connectionStatus === 'AUTHENTICATED') {
            await client.sendMessage(formattedNumber, message);
            return res.json({ success: true, message: 'Dispatched via WhatsApp QR.' });
        } else {
            console.log(`[Simulated WhatsApp Message to ${number}]:\n${message}`);
            return res.json({ success: true, simulated: true, message: 'Session pending QR scan. Logged.' });
        }
    } catch (err) {
        console.error('WhatsApp Error:', err.message);
        return res.status(500).json({ error: err.message });
    }
});

const PORT = 5000;
app.listen(PORT, () => {
    console.log(`WhatsApp QR Service running on http://localhost:${PORT}`);
});
