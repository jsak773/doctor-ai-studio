# 100% Comprehensive Multilingual i18n & Glassmorphism Dashboard UI

DASHBOARD_HTML_UI = """<!DOCTYPE html>
<html lang="gu">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Doctor AI Studio — Glassmorphism Dashboard</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        :root {
            --bg-gradient: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #0f172a 100%);
            --glass-bg: rgba(255, 255, 255, 0.07);
            --glass-border: 1px solid rgba(255, 255, 255, 0.15);
            --glass-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
            --text-primary: #f8fafc;
            --text-muted: #94a3b8;
            --accent-cyan: #38bdf8;
            --accent-emerald: #34d399;
            --accent-purple: #818cf8;
            --accent-amber: #fbbf24;
        }

        body {
            background: var(--bg-gradient);
            background-attachment: fixed;
            color: var(--text-primary);
            font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
            min-height: 100vh;
        }

        .glass-sidebar {
            background: rgba(15, 23, 42, 0.75);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border-right: var(--glass-border);
            min-height: 100vh;
            padding: 24px;
        }

        .sidebar-brand {
            font-size: 1.4rem;
            font-weight: 800;
            background: linear-gradient(90deg, #38bdf8, #818cf8);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-decoration: none;
            display: block;
            margin-bottom: 24px;
        }

        .glass-card {
            background: var(--glass-bg);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: var(--glass-border);
            box-shadow: var(--glass-shadow);
            border-radius: 16px;
            padding: 24px;
            margin-bottom: 24px;
            color: var(--text-primary);
        }

        .nav-link-glass {
            color: var(--text-muted);
            padding: 12px 18px;
            border-radius: 12px;
            margin-bottom: 8px;
            font-weight: 600;
            display: block;
            text-decoration: none;
            transition: all 0.3s ease;
            border: 1px solid transparent;
        }

        .nav-link-glass:hover, .nav-link-glass.active {
            background: rgba(56, 189, 248, 0.15);
            border: 1px solid rgba(56, 189, 248, 0.3);
            color: var(--accent-cyan);
            box-shadow: 0 4px 20px rgba(56, 189, 248, 0.2);
        }

        .form-control-glass, .form-select-glass {
            background: rgba(255, 255, 255, 0.05) !important;
            border: 1px solid rgba(255, 255, 255, 0.2) !important;
            color: #ffffff !important;
            border-radius: 10px !important;
            padding: 10px 14px !important;
        }

        .form-control-glass::placeholder { color: #64748b !important; }
        .form-select-glass option { background: #0f172a; color: #ffffff; }

        .btn-glass-primary {
            background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%);
            border: none;
            color: white;
            font-weight: 700;
            border-radius: 10px;
            padding: 10px 20px;
            box-shadow: 0 4px 15px rgba(2, 132, 199, 0.4);
            transition: 0.3s;
        }
        .btn-glass-primary:hover { opacity: 0.9; transform: translateY(-1px); }

        .btn-glass-danger {
            background: linear-gradient(135deg, #e11d48 0%, #be123c 100%);
            border: none;
            color: white;
            font-weight: 700;
            border-radius: 10px;
            padding: 10px 20px;
            box-shadow: 0 4px 15px rgba(225, 29, 72, 0.4);
        }

        .btn-glass-warning {
            background: linear-gradient(135deg, #d97706 0%, #b45309 100%);
            border: none;
            color: white;
            font-weight: 700;
            border-radius: 10px;
            padding: 10px 20px;
            box-shadow: 0 4px 15px rgba(217, 119, 6, 0.4);
        }

        .badge-glass-cyan { background: rgba(56, 189, 248, 0.2); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.4); }
        .badge-glass-emerald { background: rgba(52, 211, 153, 0.2); color: #34d399; border: 1px solid rgba(52, 211, 153, 0.4); }
        .badge-glass-amber { background: rgba(251, 191, 36, 0.2); color: #fbbf24; border: 1px solid rgba(251, 191, 36, 0.4); }
        .badge-glass-purple { background: rgba(129, 140, 248, 0.2); color: #818cf8; border: 1px solid rgba(129, 140, 248, 0.4); }

        .table-glass { color: var(--text-primary) !important; border-color: rgba(255, 255, 255, 0.1) !important; }
        .table-glass thead { background: rgba(255, 255, 255, 0.05); color: var(--accent-cyan); }
        .table-glass td, .table-glass th { border-color: rgba(255, 255, 255, 0.08) !important; padding: 12px; }

        .qr-box-glass {
            background: rgba(255, 255, 255, 0.03);
            border: 2px dashed rgba(56, 189, 248, 0.4);
            border-radius: 16px;
            padding: 24px;
            text-align: center;
        }

        .qr-img { max-width: 220px; height: auto; border-radius: 12px; }
        .chat-bubble-agent { background: rgba(56, 189, 248, 0.15); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.3); padding: 12px 16px; border-radius: 12px; margin-bottom: 10px; max-width: 80%; }
        .chat-bubble-user { background: rgba(255, 255, 255, 0.1); color: #f8fafc; border: 1px solid rgba(255, 255, 255, 0.15); padding: 12px 16px; border-radius: 12px; margin-bottom: 10px; max-width: 80%; margin-left: auto; text-align: right; }
    </style>
</head>
<body>

<div class="container-fluid">
    <div class="row">

        <!-- Sidebar Navigation -->
        <div class="col-md-3 col-lg-2 glass-sidebar">
            <a href="#" class="sidebar-brand">
                <i class="fa-solid fa-user-doctor me-2"></i> Doctor AI Studio
            </a>

            <!-- Sidebar Language Control Selector -->
            <div class="mb-4">
                <label class="form-label small text-muted text-uppercase fw-bold m-0 mb-1"><i class="fa-solid fa-language me-1"></i> <span data-i18n="lang_label">Language / ભાષા</span></label>
                <select id="lang_toggle" class="form-select form-select-glass fw-bold" onchange="changeLanguage(this.value)">
                    <option value="gu">ગુજરાતી (Gujarati)</option>
                    <option value="en">English (US)</option>
                </select>
            </div>

            <div class="nav flex-column nav-pills" role="tablist">
                <a class="nav-link-glass active" id="tab-appts" data-bs-toggle="pill" href="#pane-appts">
                    <i class="fa-solid fa-calendar-check me-2"></i> <span data-i18n="tab_appointments">એપોઇન્ટમેન્ટ્સ</span>
                </a>
                <a class="nav-link-glass" id="tab-wa-bot" data-bs-toggle="pill" href="#pane-wa-bot">
                    <i class="fa-brands fa-whatsapp text-success me-2"></i> <span data-i18n="tab_wa_bot">વોટ્સએપ ચેટબોટ</span>
                </a>
                <a class="nav-link-glass" id="tab-voice" data-bs-toggle="pill" href="#pane-voice">
                    <i class="fa-solid fa-microphone text-warning me-2"></i> <span data-i18n="tab_voice">એઆઈ વોઈસ એજન્ટ</span>
                </a>
                <a class="nav-link-glass" id="tab-whatsapp" data-bs-toggle="pill" href="#pane-whatsapp">
                    <i class="fa-brands fa-whatsapp text-success me-2"></i> <span data-i18n="tab_wa_qr">વોટ્સએપ કનેક્શન</span>
                </a>
                <a class="nav-link-glass" id="tab-patients" data-bs-toggle="pill" href="#pane-patients">
                    <i class="fa-solid fa-users me-2"></i> <span data-i18n="tab_patients">દર્દીઓની હિસ્ટ્રી</span>
                </a>
                <a class="nav-link-glass" id="tab-hr" data-bs-toggle="pill" href="#pane-hr">
                    <i class="fa-solid fa-hospital-user me-2"></i> <span data-i18n="tab_hr">ક્લિનિક HR સ્ટાફ</span>
                </a>
                <a class="nav-link-glass" id="tab-settings" data-bs-toggle="pill" href="#pane-settings">
                    <i class="fa-solid fa-gear me-2"></i> <span data-i18n="tab_settings">પ્રોફાઇલ & સેટિંગ્સ</span>
                </a>
            </div>
        </div>

        <!-- Main Workspace -->
        <div class="col-md-9 col-lg-10 p-4">

            <!-- Top Glass Header Bar -->
            <div class="glass-card d-flex justify-content-between align-items-center mb-4 py-3">
                <div>
                    <h4 class="fw-bold m-0" id="header-doctor-name">Dr. A. J. Sakhrelia Clinic</h4>
                    <small class="text-muted" id="header-clinic-name">Arogya Healthcare Center</small>
                </div>
                <div class="d-flex align-items-center gap-2">
                    <span class="badge badge-glass-cyan px-3 py-2 rounded-pill"><i class="fa-solid fa-phone me-1"></i> <span data-i18n="lbl_doctor">Doctor</span>: <strong id="header-doctor-phone">+91 9099555744</strong></span>
                    <span id="wa-status-badge" class="badge badge-glass-amber px-3 py-2 rounded-pill"><i class="fa-solid fa-spinner fa-spin me-1"></i> <span data-i18n="st_syncing">Syncing</span></span>
                    <span class="badge badge-glass-emerald px-3 py-2 rounded-pill"><i class="fa-solid fa-circle-check me-1"></i> <span data-i18n="st_active">Active</span></span>
                </div>
            </div>

            <div class="tab-content" id="v-pills-tabContent">

                <!-- TAB 1: Appointments -->
                <div class="tab-pane fade show active" id="pane-appts">
                    <div class="row g-4 mb-4">
                        <div class="col-lg-7">
                            <div class="glass-card">
                                <h5 class="fw-bold mb-3"><i class="fa-solid fa-plus-circle text-info me-2"></i> <span data-i18n="new_appt_title">નવી એપોઇન્ટમેન્ટ શિડ્યુલ કરો</span></h5>
                                <form id="booking-form" onsubmit="handleBooking(event)" class="row g-3">
                                    <div class="col-md-6">
                                        <label class="form-label fw-semibold" data-i18n="lbl_patient_name">દર્દીનું પૂરું નામ</label>
                                        <input type="text" id="patient_name" class="form-control form-control-glass" required data-i18n-ph="ph_patient_name" placeholder="Ramesh Patel">
                                    </div>
                                    <div class="col-md-6">
                                        <label class="form-label fw-semibold" data-i18n="lbl_mobile">મોબાઇલ નંબર</label>
                                        <input type="text" id="patient_phone" class="form-control form-control-glass" required data-i18n-ph="ph_mobile" placeholder="+919876543210">
                                    </div>
                                    <div class="col-md-6">
                                        <label class="form-label fw-semibold" data-i18n="lbl_date">તારીખ</label>
                                        <input type="date" id="appointment_date" class="form-control form-control-glass" required>
                                    </div>
                                    <div class="col-md-6">
                                        <label class="form-label fw-semibold" data-i18n="lbl_slot">કલાક સ્લોટ</label>
                                        <select id="time_slot" class="form-select form-select-glass" required>
                                            <option value="09:00 AM">09:00 AM</option>
                                            <option value="10:00 AM">10:00 AM</option>
                                            <option value="11:00 AM">11:00 AM</option>
                                            <option value="12:00 PM">12:00 PM</option>
                                            <option value="02:00 PM">02:00 PM</option>
                                            <option value="03:00 PM">03:00 PM</option>
                                            <option value="04:00 PM">04:00 PM</option>
                                            <option value="05:00 PM">05:00 PM</option>
                                        </select>
                                    </div>
                                    <div class="col-12 mt-3">
                                        <button type="submit" class="btn btn-glass-primary w-100">
                                            <i class="fa-solid fa-check-circle me-1"></i> <span data-i18n="btn_confirm_slot">સ્લોટ કન્ફર્મ કરો અને વોટ્સએપ મોકલો</span>
                                        </button>
                                    </div>
                                </form>
                            </div>
                        </div>

                        <div class="col-lg-5">
                            <div class="glass-card">
                                <h5 class="fw-bold mb-3"><i class="fa-solid fa-bolt text-warning me-2"></i> <span data-i18n="quick_actions_title">કવિક એક્શન્સ & ઓટોમેશન</span></h5>
                                <p class="text-muted small" data-i18n="quick_actions_desc">એક ક્લિકથી દર્દીઓને અડધી કલાક પહેલાનો રિમાઇન્ડર અને ડૉક્ટરને આજના દર્દીઓનું લિસ્ટ મોકલો.</p>
                                <button onclick="trigger30MinReminders()" class="btn btn-glass-warning w-100 mb-3">
                                    <i class="fa-solid fa-clock-rotate-left me-2"></i> <span data-i18n="btn_reminder_30m">30-મિનિટ દર્દી રિમાઇન્ડર મોકલો</span>
                                </button>
                                <button onclick="sendDoctorDailySummary()" class="btn btn-glass-primary w-100">
                                    <i class="fa-solid fa-paper-plane me-2"></i> <span data-i18n="btn_doctor_report">ડૉક્ટરને ડેઇલી રિપોર્ટ મોકલો</span>
                                </button>
                            </div>
                        </div>
                    </div>

                    <!-- Appointments Table -->
                    <div class="glass-card">
                        <h5 class="fw-bold mb-3"><i class="fa-solid fa-list-check me-2"></i> <span data-i18n="all_appts_title">બધા જ એપોઇન્ટમેન્ટ્સ સ્લોટ્સ</span></h5>
                        <div class="table-responsive">
                            <table class="table table-glass table-hover align-middle">
                                <thead>
                                    <tr>
                                        <th>ID</th>
                                        <th data-i18n="th_patient_name">દર્દીનું નામ</th>
                                        <th data-i18n="th_phone">ફોન નંબર</th>
                                        <th data-i18n="th_date">તારીખ</th>
                                        <th data-i18n="th_slot">સમય</th>
                                        <th data-i18n="th_status">સ્ટેટસ</th>
                                    </tr>
                                </thead>
                                <tbody id="appts-table-body">
                                    <!-- Dynamic -->
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>

                <!-- TAB 2: WhatsApp Chatbot -->
                <div class="tab-pane fade" id="pane-wa-bot">
                    <div class="row g-4">
                        <div class="col-lg-7">
                            <div class="glass-card">
                                <h5 class="fw-bold mb-3 text-success"><i class="fa-brands fa-whatsapp me-2"></i> <span data-i18n="wa_bot_console_title">વોટ્સએપ એઆઈ ચેટબોટ કન્સોલ</span></h5>
                                <p class="text-muted small" data-i18n="wa_bot_desc">કોઈ પણ દર્દી WhatsApp પર 'Hi' અથવા 'નમસ્તે' મોકલશે, એટલે AI ઓટોમેટીક જવાબ આપશે અને બુકિંગ કરશે:</p>

                                <div id="wa-chat-box" style="height: 320px; overflow-y: auto;" class="p-3 border border-secondary rounded mb-3 bg-dark">
                                    <div class="chat-bubble-agent" id="wa-initial-bubble">
                                        <i class="fa-brands fa-whatsapp me-1 text-success"></i> <strong>WhatsApp AI Bot:</strong> 👋 નમસ્તે! ડૉ. A. J. Sakhrelia ના ક્લિનિકમાં તમારું સ્વાગત છે. એપોઇન્ટમેન્ટ બુક કરવા માટે તમારું નામ જણાવશો?
                                    </div>
                                </div>

                                <div class="input-group">
                                    <input type="text" id="wa_user_input" class="form-control form-control-glass" data-i18n-ph="ph_wa_input" placeholder="'Hi', 'Ramesh Patel' or '10 AM'...">
                                    <button onclick="sendWaSimMessage()" class="btn btn-glass-primary">
                                        <i class="fa-solid fa-paper-plane me-1"></i> <span data-i18n="btn_send">મોકલો</span>
                                    </button>
                                </div>
                            </div>
                        </div>

                        <div class="col-lg-5">
                            <div class="glass-card">
                                <h5 class="fw-bold mb-3"><i class="fa-solid fa-circle-info text-info me-2"></i> <span data-i18n="how_wa_bot_works_title">WhatsApp ચેટબોટ કેવી રીતે કામ કરે છે?</span></h5>
                                <ol class="text-muted small">
                                    <li class="mb-2" data-i18n="wa_step1">દર્દી WhatsApp પર 'Hi' અથવા 'નમસ્તે' મોકલે છે.</li>
                                    <li class="mb-2" data-i18n="wa_step2">AI ચેટબોટ ઓટોમેટીક ડેટાબેઝમાંથી ઓપન સ્લોટ્સ ચેક કરીને ચેટમાં લિસ્ટ મોકલે છે.</li>
                                    <li class="mb-2" data-i18n="wa_step3">દર્દી સ્લોટ પસંદ કરે એટલે બુકિંગ થઈ જાય છે.</li>
                                    <li class="mb-2" data-i18n="wa_step4">ડૉક્ટર સાહેબના નંબર અને દર્દીને કન્ફર્મેશન મોકલે છે.</li>
                                </ol>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- TAB 3: Voice Agent -->
                <div class="tab-pane fade" id="pane-voice">
                    <div class="row g-4 mb-4">
                        <div class="col-lg-6">
                            <div class="glass-card">
                                <h5 class="fw-bold mb-3 text-info"><i class="fa-solid fa-microphone me-2"></i> <span data-i18n="voice_sim_title">ફ્રી માઇક્રોફોન ગુજરાતી કોલર</span></h5>
                                <p class="text-muted small" data-i18n="voice_sim_desc">બ્રાઉઝર માઇક્રોફોન દ્વારા ગુજરાતીમાં AI એજન્ટ સાથે ફ્રી કોલિંગ ટેસ્ટ કરો:</p>
                                
                                <div id="voice-chat-box" style="height: 250px; overflow-y: auto;" class="p-3 border border-secondary rounded mb-3 bg-dark">
                                    <div class="chat-bubble-agent" id="voice-initial-bubble">
                                        <i class="fa-solid fa-headset me-1"></i> <strong>AI Agent:</strong> નમસ્તે! ડૉ. A. J. Sakhrelia ના ક્લિનિકમાં તમારું સ્વાગત છે. કૃપા કરીને તમારું પૂરું નામ જણાવશો?
                                    </div>
                                </div>

                                <div class="d-flex gap-2">
                                    <input type="text" id="sim_user_transcript" class="form-control form-control-glass" data-i18n-ph="ph_voice_input" placeholder="Speak/type in Gujarati...">
                                    <button onclick="sendVoiceSimTurn()" class="btn btn-glass-primary">
                                        <i class="fa-solid fa-paper-plane me-1"></i> <span data-i18n="btn_speak">બોલો/મોકલો</span>
                                    </button>
                                </div>
                            </div>
                        </div>

                        <div class="col-lg-6">
                            <div class="glass-card">
                                <h5 class="fw-bold mb-3"><i class="fa-solid fa-phone me-2"></i> <span data-i18n="voice_config_title">ટેલિફોની વેરિફિકેશન</span></h5>
                                <ul class="list-group list-group-flush bg-transparent mb-3 small">
                                    <li class="list-group-item bg-transparent text-light d-flex justify-content-between">
                                        <span data-i18n="lbl_doc_mobile">ડૉક્ટર મોબાઇલ નંબર:</span>
                                        <strong class="text-info" id="voice-setting-phone">+91 9099555744</strong>
                                    </li>
                                    <li class="list-group-item bg-transparent text-light d-flex justify-content-between">
                                        <span data-i18n="lbl_voice_lang">વોઈસ ભાષા:</span>
                                        <strong class="text-success">Gujarati (gu-IN) & English</strong>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>

                    <!-- Call Logs -->
                    <div class="glass-card">
                        <h5 class="fw-bold mb-3"><i class="fa-solid fa-phone-volume me-2"></i> <span data-i18n="call_logs_title">લાઈવ કોલ લોગ્સ</span></h5>
                        <div class="table-responsive">
                            <table class="table table-glass align-middle">
                                <thead>
                                    <tr>
                                        <th data-i18n="th_caller">કોલર નંબર</th>
                                        <th data-i18n="th_transcript">ઓડિયો બોલેલ</th>
                                        <th data-i18n="th_agent_resp">AI જવાબ</th>
                                        <th data-i18n="th_status">સ્ટેટસ</th>
                                    </tr>
                                </thead>
                                <tbody id="voice-logs-body">
                                    <!-- Dynamic -->
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>

                <!-- TAB 4: WhatsApp Connection & Lifecycle Management -->
                <div class="tab-pane fade" id="pane-whatsapp">
                    <div class="row g-4 mb-4">
                        <div class="col-lg-6">
                            <div class="glass-card">
                                <h5 class="fw-bold mb-3 text-success"><i class="fa-brands fa-whatsapp me-2"></i> <span data-i18n="wa_qr_title">વોટ્સએપ ક્યુઆર કોડ કનેક્શન</span></h5>
                                <div class="qr-box-glass mb-3">
                                    <div id="qr-container">
                                        <i class="fa-solid fa-spinner fa-spin fa-2x text-info"></i>
                                        <p class="mt-2 text-muted" data-i18n="qr_loading">ક્યુઆર કોડ લોડ થઈ રહ્યો છે...</p>
                                    </div>
                                    <div class="d-flex gap-2 justify-content-center mt-3">
                                        <button onclick="refreshQR()" class="btn btn-glass-primary btn-sm">
                                            <i class="fa-solid fa-rotate-right me-1"></i> <span data-i18n="btn_refresh_qr">રિફ્રેશ QR</span>
                                        </button>
                                        <button onclick="disconnectWhatsApp()" class="btn btn-glass-danger btn-sm">
                                            <i class="fa-solid fa-power-off me-1"></i> <span data-i18n="btn_disconnect_wa">Disconnect WhatsApp</span>
                                        </button>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div class="col-lg-6">
                            <div class="glass-card">
                                <h5 class="fw-bold mb-3"><i class="fa-solid fa-mobile-screen-button text-info me-2"></i> <span data-i18n="change_phone_title">Change Doctor Phone Number</span></h5>
                                <p class="text-muted small" data-i18n="change_phone_desc">ડૉક્ટરનો નવો વોટ્સએપ નંબર સેટ કરો અને નવો QR કોડ સ્કેન કરો:</p>
                                <div class="mb-3">
                                    <label class="form-label fw-semibold" data-i18n="lbl_new_phone">નવો વોટ્સએપ નંબર (New Doctor Phone)</label>
                                    <input type="text" id="new_doctor_phone_input" class="form-control form-control-glass" value="+919099555744">
                                </div>
                                <button onclick="changeDoctorPhone()" class="btn btn-glass-primary w-100 mb-3">
                                    <i class="fa-solid fa-floppy-disk me-1"></i> <span data-i18n="btn_update_phone">નંબર બદલો & ડિસ્કનેક્ટ કરો</span>
                                </button>
                                
                                <div class="alert alert-info bg-transparent text-light border-secondary small m-0">
                                    <i class="fa-solid fa-circle-info me-1 text-info"></i> <strong data-i18n="qr_note_title">Note on QR Code Hosting:</strong>
                                    <span data-i18n="qr_note_desc">WhatsApp Web QR connection requires a long-running Node.js/Chromium process. On Localhost / Render / Docker it runs natively. On Vercel Serverless, simulated QR fallback handles API requests gracefully.</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- TAB 5: Patients Directory -->
                <div class="tab-pane fade" id="pane-patients">
                    <div class="glass-card">
                        <h5 class="fw-bold mb-3"><i class="fa-solid fa-users me-2"></i> <span data-i18n="patients_title">દર્દીઓની હિસ્ટ્રી અને ડિરેક્ટરી</span></h5>
                        <div class="table-responsive">
                            <table class="table table-glass align-middle">
                                <thead>
                                    <tr>
                                        <th data-i18n="th_patient_name">દર્દીનું નામ</th>
                                        <th data-i18n="th_phone">મોબાઈલ નંબર</th>
                                        <th data-i18n="th_total_visits">કુલ મુલાકાત</th>
                                        <th data-i18n="th_last_visit">છેલ્લી મુલાકાત</th>
                                    </tr>
                                </thead>
                                <tbody id="patients-table-body">
                                    <!-- Dynamic -->
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>

                <!-- TAB 6: Clinic HR Assistant -->
                <div class="tab-pane fade" id="pane-hr">
                    <div class="glass-card">
                        <h5 class="fw-bold mb-3"><i class="fa-solid fa-hospital-user me-2"></i> <span data-i18n="hr_title">ક્લિનિક સ્ટાફ અને HR હેલ્પર</span></h5>
                        <div class="table-responsive">
                            <table class="table table-glass align-middle">
                                <thead>
                                    <tr>
                                        <th data-i18n="th_staff_name">નામ</th>
                                        <th data-i18n="th_role">હોદ્દો</th>
                                        <th data-i18n="th_phone">મોબાઈલ નંબર</th>
                                        <th data-i18n="th_shift">શિફ્ટ સમય</th>
                                        <th data-i18n="th_status">સ્ટેટસ</th>
                                    </tr>
                                </thead>
                                <tbody id="hr-staff-body">
                                    <!-- Dynamic -->
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>

                <!-- TAB 7: Doctor Profile Settings -->
                <div class="tab-pane fade" id="pane-settings">
                    <div class="glass-card">
                        <h5 class="fw-bold mb-3"><i class="fa-solid fa-gear text-secondary me-2"></i> <span data-i18n="settings_title">ડૉક્ટર પ્રોફાઇલ અને ક્લિનિક સેટિંગ્સ</span></h5>
                        <form id="settings-form" onsubmit="saveSettings(event)" class="row g-3">
                            <div class="col-md-6">
                                <label class="form-label fw-semibold" data-i18n="lbl_doc_name_setting">ડૉક્ટર સાહેબનું નામ</label>
                                <input type="text" id="setting_doctor_name" class="form-control form-control-glass" required>
                            </div>
                            <div class="col-md-6">
                                <label class="form-label fw-semibold" data-i18n="lbl_doc_phone_setting">ડૉક્ટરનો વોટ્સએપ નંબર</label>
                                <input type="text" id="setting_doctor_phone" class="form-control form-control-glass" required value="+919099555744">
                            </div>
                            <div class="col-md-6">
                                <label class="form-label fw-semibold" data-i18n="lbl_clinic_name_setting">દવાખાનાનું નામ</label>
                                <input type="text" id="setting_clinic_name" class="form-control form-control-glass" required>
                            </div>
                            <div class="col-md-6">
                                <label class="form-label fw-semibold" data-i18n="lbl_lang_setting">ડેશબોર્ડ ભાષા (Language)</label>
                                <select id="setting_dashboard_language" class="form-select form-select-glass" onchange="changeLanguage(this.value)">
                                    <option value="gu">ગુજરાતી (Gujarati)</option>
                                    <option value="en">English (US)</option>
                                </select>
                            </div>
                            <div class="col-12">
                                <label class="form-label fw-semibold" data-i18n="lbl_clinic_loc_setting">ક્લિનિકનું લોકેશન / ગૂગલ મેપ્સ લિંક</label>
                                <input type="text" id="setting_clinic_location" class="form-control form-control-glass" required>
                            </div>
                            <div class="col-12 mt-3">
                                <button type="submit" class="btn btn-glass-primary">
                                    <i class="fa-solid fa-floppy-disk me-1"></i> <span data-i18n="btn_save_settings">સેવ કરો (Save Settings)</span>
                                </button>
                            </div>
                        </form>
                    </div>
                </div>

            </div>

        </div>
    </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
<script>
    document.getElementById('appointment_date').value = new Date().toISOString().split('T')[0];
    let simCallId = 'sim_call_' + Math.floor(Math.random() * 100000);
    let currentLang = 'gu';

    const i18nDict = {
        gu: {
            lang_label: "ભાષા (Language)",
            tab_appointments: "એપોઇન્ટમેન્ટ્સ",
            tab_wa_bot: "વોટ્સએપ ચેટબોટ",
            tab_voice: "એઆઈ વોઈસ એજન્ટ",
            tab_wa_qr: "વોટ્સએપ કનેક્શન",
            tab_patients: "દર્દીઓની હિસ્ટ્રી",
            tab_hr: "ક્લિનિક HR સ્ટાફ",
            tab_settings: "પ્રોફાઇલ & સેટિંગ્સ",
            lbl_doctor: "ડૉક્ટર",
            st_syncing: "સિંક થઈ રહ્યું છે",
            st_active: "સક્રિય છે",
            new_appt_title: "નવી એપોઇન્ટમેન્ટ શિડ્યુલ કરો",
            lbl_patient_name: "દર્દીનું પૂરું નામ",
            ph_patient_name: "રમેશ પટેલ",
            lbl_mobile: "મોબાઇલ નંબર",
            ph_mobile: "+919876543210",
            lbl_date: "તારીખ",
            lbl_slot: "કલાક સ્લોટ",
            btn_confirm_slot: "સ્લોટ કન્ફર્મ કરો અને વોટ્સએપ મોકલો",
            quick_actions_title: "કવિક એક્શન્સ & ઓટોમેશન",
            quick_actions_desc: "એક ક્લિકથી દર્દીઓને અડધી કલાક પહેલાનો રિમાઇન્ડર અને ડૉક્ટરને આજના દર્દીઓનું લિસ્ટ મોકલો.",
            btn_reminder_30m: "30-મિનિટ દર્દી રિમાઇન્ડર મોકલો",
            btn_doctor_report: "ડૉક્ટરને ડેઇલી રિપોર્ટ મોકલો",
            all_appts_title: "બધા જ એપોઇન્ટમેન્ટ્સ સ્લોટ્સ",
            th_patient_name: "દર્દીનું નામ",
            th_phone: "ફોન નંબર",
            th_date: "તારીખ",
            th_slot: "સમય",
            th_status: "સ્ટેટસ",
            wa_bot_console_title: "વોટ્સએપ એઆઈ ચેટબોટ કન્સોલ",
            wa_bot_desc: "કોઈ પણ દર્દી WhatsApp પર 'Hi' અથવા 'નમસ્તે' મોકલશે, એટલે AI ઓટોમેટીક જવાબ આપશે અને બુકિંગ કરશે:",
            ph_wa_input: "'Hi', 'રમેશ પટેલ' અથવા '10 AM' મોકલો...",
            btn_send: "મોકલો",
            how_wa_bot_works_title: "WhatsApp ચેટબોટ કેવી રીતે કામ કરે છે?",
            wa_step1: "દર્દી WhatsApp પર 'Hi' અથવા 'નમસ્તે' મોકલે છે.",
            wa_step2: "AI ચેટબોટ ઓટોમેટીક ડેટાબેઝમાંથી ઓપન સ્લોટ્સ ચેક કરીને ચેટમાં લિસ્ટ મોકલે છે.",
            wa_step3: "દર્દી સ્લોટ પસંદ કરે એટલે બુકિંગ થઈ જાય છે.",
            wa_step4: "ડૉક્ટર સાહેબના નંબર અને દર્દીને કન્ફર્મેશન મોકલે છે.",
            voice_sim_title: "ફ્રી માઇક્રોફોન ગુજરાતી કોલર",
            voice_sim_desc: "બ્રાઉઝર માઇક્રોફોન દ્વારા ગુજરાતીમાં AI એજન્ટ સાથે ફ્રી કોલિંગ ટેસ્ટ કરો:",
            ph_voice_input: "ગુજરાતીમાં બોલો/લખો...",
            btn_speak: "બોલો/મોકલો",
            voice_config_title: "ટેલિફોની વેરિફિકેશન",
            lbl_doc_mobile: "ડૉક્ટર મોબાઇલ નંબર:",
            lbl_voice_lang: "વોઈસ ભાષા:",
            call_logs_title: "લાઈવ કોલ લોગ્સ",
            th_caller: "કોલર નંબર",
            th_transcript: "ઓડિયો બોલેલ",
            th_agent_resp: "AI જવાબ",
            wa_qr_title: "વોટ્સએપ ક્યુઆર કોડ કનેક્શન",
            qr_loading: "ક્યુઆર કોડ લોડ થઈ રહ્યો છે...",
            btn_refresh_qr: "રિફ્રેશ QR",
            btn_disconnect_wa: "Disconnect WhatsApp",
            change_phone_title: "ડૉક્ટર મોબાઇલ નંબર બદલો",
            change_phone_desc: "ડૉક્ટરનો નવો વોટ્સએપ નંબર સેટ કરો અને નવો QR કોડ સ્કેન કરો:",
            lbl_new_phone: "નવો વોટ્સએપ નંબર (New Doctor Phone)",
            btn_update_phone: "નંબર બદલો & ડિસ્કનેક્ટ કરો",
            qr_note_title: "QR કોડ હોસ્ટિંગ વિગત:",
            qr_note_desc: "WhatsApp QR કનેક્શન લોકલહોસ્ટ / ડોકર / રેન્ડર પર ડાયરેક્ટ ચાલે છે. Vercel ક્લાઉડ પર ઓટો સિમ્યુલેટેડ QR સ્ટેટ મોડ સપોર્ટેડ છે.",
            patients_title: "દર્દીઓની હિસ્ટ્રી અને ડિરેક્ટરી",
            th_total_visits: "કુલ મુલાકાત",
            th_last_visit: "છેલ્લી મુલાકાત",
            hr_title: "ક્લિનિક સ્ટાફ અને HR હેલ્પર",
            th_staff_name: "નામ",
            th_role: "હોદ્દો",
            th_shift: "શિફ્ટ સમય",
            settings_title: "ડૉક્ટર પ્રોફાઇલ અને ક્લિનિક સેટિંગ્સ",
            lbl_doc_name_setting: "ડૉક્ટર સાહેબનું નામ",
            lbl_doc_phone_setting: "ડૉક્ટરનો વોટ્સએપ નંબર",
            lbl_clinic_name_setting: "દવાખાનાનું નામ",
            lbl_lang_setting: "ડેશબોર્ડ ભાષા (Language)",
            lbl_clinic_loc_setting: "ક્લિનિકનું લોકેશન / ગૂગલ મેપ્સ લિંક",
            btn_save_settings: "સેવ કરો (Save Settings)",
            wa_bubble_init: "👋 નમસ્તે! ડૉ. A. J. Sakhrelia ના ક્લિનિકમાં તમારું સ્વાગત છે. એપોઇન્ટમેન્ટ બુક કરવા માટે તમારું નામ જણાવશો?",
            voice_bubble_init: "નમસ્તે! ડૉ. A. J. Sakhrelia ના ક્લિનિકમાં તમારું સ્વાગત છે. કૃપા કરીને તમારું પૂરું નામ જણાવશો?",
            status_booked: "બુક થયેલ",
            status_active: "સક્રિય",
            visits_suffix: "મુલાકાત"
        },
        en: {
            lang_label: "Language / ભાષા",
            tab_appointments: "Appointments",
            tab_wa_bot: "WhatsApp Chatbot",
            tab_voice: "AI Voice Agent",
            tab_wa_qr: "WhatsApp Connection",
            tab_patients: "Patient History",
            tab_hr: "Clinic HR Staff",
            tab_settings: "Profile & Settings",
            lbl_doctor: "Doctor",
            st_syncing: "Syncing",
            st_active: "Active",
            new_appt_title: "Schedule New Appointment",
            lbl_patient_name: "Patient Full Name",
            ph_patient_name: "Ramesh Patel",
            lbl_mobile: "Mobile Number",
            ph_mobile: "+919876543210",
            lbl_date: "Date",
            lbl_slot: "Hourly Time Slot",
            btn_confirm_slot: "Confirm Slot & Send WhatsApp",
            quick_actions_title: "Quick Actions & Automation",
            quick_actions_desc: "Send 30-min advance reminders to patients and daily summaries to doctor in 1-click.",
            btn_reminder_30m: "Send 30-Min Patient Reminder",
            btn_doctor_report: "Send Daily Report to Doctor",
            all_appts_title: "All Appointment Slots",
            th_patient_name: "Patient Name",
            th_phone: "Phone Number",
            th_date: "Date",
            th_slot: "Time Slot",
            th_status: "Status",
            wa_bot_console_title: "Interactive WhatsApp AI Chatbot Console",
            wa_bot_desc: "When a patient sends 'Hi' or 'Hello' on WhatsApp, AI automatically replies, displays available slots, and completes booking:",
            ph_wa_input: "Type 'Hi', 'Ramesh Patel' or '10 AM'...",
            btn_send: "Send",
            how_wa_bot_works_title: "How WhatsApp AI Chatbot Works",
            wa_step1: "Patient sends 'Hi' or 'Hello' on WhatsApp.",
            wa_step2: "AI Chatbot queries open slots from the database and sends the list in chat.",
            wa_step3: "Patient selects preferred slot and booking is finalized.",
            wa_step4: "Sends instant confirmation to doctor and patient.",
            voice_sim_title: "Free Microphone Gujarati & English Voice Caller",
            voice_sim_desc: "Test voice calling for free directly using your browser microphone:",
            ph_voice_input: "Speak or type response...",
            btn_speak: "Speak / Send",
            voice_config_title: "Telephony Verification",
            lbl_doc_mobile: "Doctor Mobile Number:",
            lbl_voice_lang: "Voice Language:",
            call_logs_title: "Live Voice Call Logs",
            th_caller: "Caller Phone",
            th_transcript: "User Audio Transcript",
            th_agent_resp: "AI Agent Response",
            wa_qr_title: "WhatsApp Web Connection",
            qr_loading: "Loading QR Code...",
            btn_refresh_qr: "Refresh QR",
            btn_disconnect_wa: "Disconnect WhatsApp Session",
            change_phone_title: "Change Doctor Phone Number",
            change_phone_desc: "Update Doctor's WhatsApp number and scan a new QR code:",
            lbl_new_phone: "New Doctor WhatsApp Phone",
            btn_update_phone: "Update Phone & Disconnect Session",
            qr_note_title: "QR Code Hosting Note:",
            qr_note_desc: "WhatsApp QR connection runs natively on Localhost / Docker / Render. On Vercel Serverless, simulated QR fallback handles API requests gracefully.",
            patients_title: "Patient Registry & Visit History",
            th_total_visits: "Total Visits",
            th_last_visit: "Last Visit Date",
            hr_title: "Clinic Staff & HR Roster",
            th_staff_name: "Staff Name",
            th_role: "Role",
            th_shift: "Shift Timing",
            settings_title: "Doctor Profile & Clinic Settings",
            lbl_doc_name_setting: "Doctor Name",
            lbl_doc_phone_setting: "Doctor WhatsApp Phone",
            lbl_clinic_name_setting: "Clinic Name",
            lbl_lang_setting: "Dashboard Language",
            lbl_clinic_loc_setting: "Clinic Location / Google Maps Link",
            btn_save_settings: "Save Settings",
            wa_bubble_init: "👋 Welcome to Dr. A. J. Sakhrelia's Clinic! I am your AI Assistant. Please state your full name to book an appointment.",
            voice_bubble_init: "Welcome to Dr. A. J. Sakhrelia's Clinic! Please state your full name to schedule a slot.",
            status_booked: "BOOKED",
            status_active: "ACTIVE",
            visits_suffix: "Visits"
        }
    };

    function changeLanguage(lang) {
        currentLang = lang;
        document.getElementById('lang_toggle').value = lang;
        document.getElementById('setting_dashboard_language').value = lang;
        const dict = i18nDict[lang] || i18nDict['gu'];
        
        // 1. Update text content
        document.querySelectorAll('[data-i18n]').forEach(el => {
            const key = el.getAttribute('data-i18n');
            if (dict[key]) el.innerText = dict[key];
        });

        // 2. Update placeholders
        document.querySelectorAll('[data-i18n-ph]').forEach(el => {
            const key = el.getAttribute('data-i18n-ph');
            if (dict[key]) el.setAttribute('placeholder', dict[key]);
        });

        // 3. Update Chat Initial Bubbles
        const waInit = document.getElementById('wa-initial-bubble');
        if (waInit) waInit.innerHTML = `<i class="fa-brands fa-whatsapp me-1 text-success"></i> <strong>WhatsApp AI Bot:</strong> ${dict.wa_bubble_init}`;

        const voiceInit = document.getElementById('voice-initial-bubble');
        if (voiceInit) voiceInit.innerHTML = `<i class="fa-solid fa-headset me-1"></i> <strong>AI Agent:</strong> ${dict.voice_bubble_init}`;

        // 4. Re-render dynamic tables
        loadAppointments();
        loadPatients();
        loadHRStaff();

        localStorage.setItem('doc_dashboard_lang', lang);
    }

    async function disconnectWhatsApp() {
        if (!confirm('Are you sure you want to disconnect current WhatsApp session?')) return;
        const res = await fetch('/api/whatsapp/disconnect', {method: 'POST'});
        if (res.ok) {
            alert('WhatsApp session disconnected! Scan the new QR code.');
            fetchQRStatus();
        }
    }

    async function changeDoctorPhone() {
        const newPhone = document.getElementById('new_doctor_phone_input').value.trim();
        if (!newPhone) return alert('Please enter a valid phone number');

        const res = await fetch('/api/whatsapp/change-phone', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ new_phone: newPhone })
        });

        if (res.ok) {
            alert('Doctor phone number updated! Disconnecting session for new QR code scan.');
            loadSettings();
            fetchQRStatus();
        }
    }

    async function sendWaSimMessage() {
        const input = document.getElementById('wa_user_input');
        const text = input.value.trim();
        if (!text) return;

        const chatBox = document.getElementById('wa-chat-box');
        chatBox.innerHTML += `<div class="chat-bubble-user"><i class="fa-solid fa-user me-1"></i> <strong>User:</strong> ${text}</div>`;
        input.value = '';

        const res = await fetch('/api/whatsapp/inbound', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ sender_phone: '+919876543210', message_text: text })
        });

        const data = await res.json();
        if (res.ok) {
            chatBox.innerHTML += `<div class="chat-bubble-agent"><i class="fa-brands fa-whatsapp me-1 text-success"></i> <strong>WhatsApp AI Bot:</strong> ${data.reply_text.replace(/\n/g, '<br>')}</div>`;
            chatBox.scrollTop = chatBox.scrollHeight;
            loadAppointments();
            loadPatients();
        }
    }

    async function loadSettings() {
        const res = await fetch('/api/settings');
        const s = await res.json();
        document.getElementById('header-doctor-name').innerText = s.doctor_name || 'Dr. A. J. Sakhrelia';
        document.getElementById('header-clinic-name').innerText = s.clinic_name || 'Arogya Healthcare Center';
        document.getElementById('header-doctor-phone').innerText = s.doctor_phone || '+91 9099555744';
        document.getElementById('voice-setting-phone').innerText = s.doctor_phone || '+91 9099555744';
        document.getElementById('new_doctor_phone_input').value = s.doctor_phone || '+919099555744';
        
        document.getElementById('setting_doctor_name').value = s.doctor_name || '';
        document.getElementById('setting_doctor_phone').value = s.doctor_phone || '+919099555744';
        document.getElementById('setting_clinic_name').value = s.clinic_name || '';
        document.getElementById('setting_working_hours').value = s.working_hours || '';
        document.getElementById('setting_clinic_location').value = s.clinic_location || '';

        const lang = localStorage.getItem('doc_dashboard_lang') || s.dashboard_language || 'gu';
        changeLanguage(lang);
    }

    async function saveSettings(e) {
        e.preventDefault();
        const lang = document.getElementById('setting_dashboard_language').value;
        const payload = {
            doctor_name: document.getElementById('setting_doctor_name').value,
            doctor_phone: document.getElementById('setting_doctor_phone').value,
            clinic_name: document.getElementById('setting_clinic_name').value,
            working_hours: document.getElementById('setting_working_hours').value,
            clinic_location: document.getElementById('setting_clinic_location').value,
            dashboard_language: lang
        };
        const res = await fetch('/api/settings', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(payload)
        });
        if (res.ok) {
            alert('Settings Saved Successfully!');
            loadSettings();
        }
    }

    async function sendVoiceSimTurn() {
        const input = document.getElementById('sim_user_transcript');
        const text = input.value.trim();
        if (!text) return;

        const chatBox = document.getElementById('voice-chat-box');
        chatBox.innerHTML += `<div class="chat-bubble-user"><i class="fa-solid fa-user me-1"></i> <strong>User:</strong> ${text}</div>`;
        input.value = '';

        const res = await fetch('/api/voice/simulate-turn', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ call_id: simCallId, caller_phone: '+919876543210', user_transcript: text })
        });

        const data = await res.json();
        if (res.ok) {
            chatBox.innerHTML += `<div class="chat-bubble-agent"><i class="fa-solid fa-headset me-1"></i> <strong>AI Agent:</strong> ${data.agent_response_gujarati}</div>`;
            chatBox.scrollTop = chatBox.scrollHeight;
            if (data.booking_completed) {
                alert('Appointment Booked Successfully!');
                simCallId = 'sim_call_' + Math.floor(Math.random() * 100000);
                loadAppointments();
                loadPatients();
            }
            loadVoiceLogs();
        }
    }

    async function loadVoiceLogs() {
        const res = await fetch('/api/voice/logs');
        const data = await res.json();
        const tbody = document.getElementById('voice-logs-body');
        tbody.innerHTML = '';
        const dict = i18nDict[currentLang] || i18nDict['gu'];
        data.logs.forEach(l => {
            tbody.innerHTML += `
                <tr>
                    <td><code>${l.caller_phone}</code></td>
                    <td>${l.transcript}</td>
                    <td><small class="text-info">${l.agent_response}</small></td>
                    <td><span class="badge badge-glass-emerald">${l.status}</span></td>
                </tr>
            `;
        });
    }

    async function fetchQRStatus() {
        try {
            const res = await fetch('/api/qr');
            const data = await res.json();
            const container = document.getElementById('qr-container');
            const badge = document.getElementById('wa-status-badge');
            const dict = i18nDict[currentLang] || i18nDict['gu'];

            if (data.status === 'AUTHENTICATED') {
                container.innerHTML = `<i class="fa-solid fa-circle-check text-success fa-4x"></i><h6 class="mt-3 text-success fw-bold">WhatsApp Connected!</h6>`;
                badge.className = 'badge badge-glass-emerald px-3 py-2 rounded-pill';
                badge.innerHTML = `<i class="fa-solid fa-circle-check me-1"></i> Connected`;
            } else if (data.qr_data_url) {
                container.innerHTML = `<img src="${data.qr_data_url}" class="qr-img" alt="Scan QR">`;
                badge.className = 'badge badge-glass-cyan px-3 py-2 rounded-pill';
                badge.innerHTML = `<i class="fa-solid fa-qrcode me-1"></i> Scan QR Code`;
            } else {
                container.innerHTML = `<i class="fa-solid fa-qrcode fa-3x text-muted"></i><p class="mt-2 text-muted">${dict.qr_loading}</p>`;
                badge.className = 'badge badge-glass-amber px-3 py-2 rounded-pill';
                badge.innerHTML = `<i class="fa-solid fa-spinner fa-spin me-1"></i> ${dict.st_syncing}`;
            }
        } catch (err) { console.error(err); }
    }

    function refreshQR() { fetchQRStatus(); }

    async function handleBooking(e) {
        e.preventDefault();
        const payload = {
            patient_name: document.getElementById('patient_name').value,
            patient_phone: document.getElementById('patient_phone').value,
            appointment_date: document.getElementById('appointment_date').value,
            time_slot: document.getElementById('time_slot').value
        };
        const res = await fetch('/api/appointments/book', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(payload)
        });
        if (res.ok) {
            alert('Appointment Booked Successfully!');
            loadAppointments();
            loadPatients();
            document.getElementById('booking-form').reset();
        }
    }

    async function loadAppointments() {
        const res = await fetch('/api/appointments/list');
        const data = await res.json();
        const tbody = document.getElementById('appts-table-body');
        tbody.innerHTML = '';
        const dict = i18nDict[currentLang] || i18nDict['gu'];
        data.appointments.forEach(a => {
            tbody.innerHTML += `
                <tr>
                    <td><code>${a.appointment_id}</code></td>
                    <td class="fw-bold">${a.patient_name}</td>
                    <td>${a.patient_phone}</td>
                    <td>${a.appointment_date}</td>
                    <td><span class="badge badge-glass-cyan">${a.time_slot}</span></td>
                    <td><span class="badge badge-glass-emerald">${dict.status_booked}</span></td>
                </tr>
            `;
        });
    }

    async function loadPatients() {
        const res = await fetch('/api/patients');
        const data = await res.json();
        const tbody = document.getElementById('patients-table-body');
        tbody.innerHTML = '';
        const dict = i18nDict[currentLang] || i18nDict['gu'];
        data.patients.forEach(p => {
            tbody.innerHTML += `
                <tr>
                    <td class="fw-bold">${p.name}</td>
                    <td>${p.phone}</td>
                    <td><span class="badge badge-glass-amber">${p.total_visits} ${dict.visits_suffix}</span></td>
                    <td>${p.last_visit || '-'}</td>
                </tr>
            `;
        });
    }

    async function loadHRStaff() {
        const res = await fetch('/api/hr/staff');
        const data = await res.json();
        const tbody = document.getElementById('hr-staff-body');
        tbody.innerHTML = '';
        const dict = i18nDict[currentLang] || i18nDict['gu'];
        data.staff.forEach(s => {
            tbody.innerHTML += `
                <tr>
                    <td class="fw-bold">${s.name}</td>
                    <td><span class="badge badge-glass-purple">${s.role}</span></td>
                    <td>${s.phone}</td>
                    <td>${s.shift_timing}</td>
                    <td><span class="badge badge-glass-emerald">${dict.status_active}</span></td>
                </tr>
            `;
        });
    }

    async function trigger30MinReminders() {
        await fetch('/api/reminders/trigger-30min', {method: 'POST'});
        alert('30-Minute Reminders Dispatched!');
    }

    async function sendDoctorDailySummary() {
        await fetch('/api/notify-doctor-daily', {method: 'POST'});
        alert('Daily Report Sent to Doctor (+91 9099555744)!');
    }

    setInterval(fetchQRStatus, 3000);
    loadSettings();
    fetchQRStatus();
    loadAppointments();
    loadPatients();
    loadHRStaff();
    loadVoiceLogs();
</script>
</body>
</html>
"""
