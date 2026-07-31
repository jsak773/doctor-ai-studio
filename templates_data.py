# Self-Contained HTML Dashboard UI for 100% Vercel Serverless Compatibility

DASHBOARD_HTML_UI = """<!DOCTYPE html>
<html lang="gu">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ડૉક્ટર એઆઈ મેનેજમેન્ટ સ્ટુડિયો (Doctor AI Studio)</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        body { background-color: #f0f2f5; font-family: 'Segoe UI', system-ui, -apple-system, sans-serif; }
        .sidebar { background: #1e293b; color: white; min-height: 100vh; padding: 20px; }
        .sidebar-brand { font-size: 1.3rem; font-weight: bold; color: #38bdf8; margin-bottom: 25px; display: block; text-decoration: none; }
        .nav-link-custom { color: #94a3b8; padding: 12px 16px; border-radius: 8px; margin-bottom: 8px; font-weight: 500; display: block; text-decoration: none; transition: 0.2s; }
        .nav-link-custom:hover, .nav-link-custom.active { background: #0f172a; color: #38bdf8; }
        .card-custom { border-radius: 12px; border: none; box-shadow: 0 4px 15px rgba(0,0,0,0.05); background: white; }
        .status-badge { font-size: 0.85rem; padding: 6px 14px; border-radius: 20px; font-weight: 600; }
        .qr-box { border: 2px dashed #0284c7; border-radius: 12px; padding: 20px; text-align: center; background: #f8fafc; }
        .qr-img { max-width: 220px; height: auto; border-radius: 8px; }
        .chat-bubble-agent { background: #e0f2fe; color: #0369a1; padding: 12px 16px; border-radius: 12px; margin-bottom: 10px; max-width: 80%; }
        .chat-bubble-user { background: #f1f5f9; color: #334155; padding: 12px 16px; border-radius: 12px; margin-bottom: 10px; max-width: 80%; margin-left: auto; text-align: right; }
        .lang-select-sidebar { background: #0f172a; color: #38bdf8; border: 1px solid #334155; border-radius: 6px; padding: 6px 10px; font-weight: 600; font-size: 0.9rem; }
    </style>
</head>
<body>

<div class="container-fluid">
    <div class="row">

        <!-- Sidebar Navigation -->
        <div class="col-md-3 col-lg-2 sidebar">
            <a href="#" class="sidebar-brand">
                <i class="fa-solid fa-user-doctor me-2"></i> Doctor AI Studio
            </a>

            <!-- Sidebar Language Control Selector -->
            <div class="mb-4">
                <label class="form-label small text-muted text-uppercase fw-bold m-0 mb-1"><i class="fa-solid fa-language me-1"></i> <span data-i18n="lang_label">Language / ભાષા</span></label>
                <select id="lang_toggle" class="form-select lang-select-sidebar" onchange="changeLanguage(this.value)">
                    <option value="gu">ગુજરાતી (Gujarati)</option>
                    <option value="en">English (US)</option>
                </select>
            </div>

            <div class="nav flex-column nav-pills" id="v-pills-tab" role="tablist">
                <a class="nav-link-custom active" id="tab-appts" data-bs-toggle="pill" href="#pane-appts">
                    <i class="fa-solid fa-calendar-check me-2"></i> <span data-i18n="tab_appointments">એપોઇન્ટમેન્ટ્સ</span>
                </a>
                <a class="nav-link-custom" id="tab-wa-bot" data-bs-toggle="pill" href="#pane-wa-bot">
                    <i class="fa-brands fa-whatsapp text-success me-2"></i> <span data-i18n="tab_wa_bot">વોટ્સએપ ચેટબોટ</span>
                </a>
                <a class="nav-link-custom" id="tab-voice" data-bs-toggle="pill" href="#pane-voice">
                    <i class="fa-solid fa-microphone text-warning me-2"></i> <span data-i18n="tab_voice">એઆઈ વોઈસ એજન્ટ</span>
                </a>
                <a class="nav-link-custom" id="tab-whatsapp" data-bs-toggle="pill" href="#pane-whatsapp">
                    <i class="fa-brands fa-whatsapp text-success me-2"></i> <span data-i18n="tab_wa_qr">વોટ્સએપ ક્યુઆર</span>
                </a>
                <a class="nav-link-custom" id="tab-patients" data-bs-toggle="pill" href="#pane-patients">
                    <i class="fa-solid fa-users me-2"></i> <span data-i18n="tab_patients">દર્દીઓની હિસ્ટ્રી</span>
                </a>
                <a class="nav-link-custom" id="tab-hr" data-bs-toggle="pill" href="#pane-hr">
                    <i class="fa-solid fa-hospital-user me-2"></i> <span data-i18n="tab_hr">ક્લિનિક HR સ્ટાફ</span>
                </a>
                <a class="nav-link-custom" id="tab-settings" data-bs-toggle="pill" href="#pane-settings">
                    <i class="fa-solid fa-gear me-2"></i> <span data-i18n="tab_settings">પ્રોફાઇલ & સેટિંગ્સ</span>
                </a>
            </div>
        </div>

        <!-- Main Workspace -->
        <div class="col-md-9 col-lg-10 p-4">

            <!-- Top Header Bar -->
            <div class="d-flex justify-content-between align-items-center mb-4 bg-white p-3 rounded-3 shadow-sm">
                <div>
                    <h4 class="fw-bold m-0 text-dark" id="header-doctor-name">Dr. A. J. Sakhrelia Clinic</h4>
                    <small class="text-muted" id="header-clinic-name">Arogya Healthcare Center</small>
                </div>
                <div class="d-flex align-items-center gap-2">
                    <span class="badge bg-primary status-badge"><i class="fa-solid fa-phone me-1"></i> Doctor: +91 9099555744</span>
                    <span id="wa-status-badge" class="badge bg-warning status-badge"><i class="fa-solid fa-spinner fa-spin me-1"></i> WhatsApp Syncing</span>
                    <span class="badge bg-success status-badge"><i class="fa-solid fa-cloud-arrow-up me-1"></i> Vercel Live</span>
                </div>
            </div>

            <div class="tab-content" id="v-pills-tabContent">

                <!-- TAB 1: Appointments -->
                <div class="tab-pane fade show active" id="pane-appts">
                    <div class="row g-4 mb-4">
                        <div class="col-lg-7">
                            <div class="card card-custom p-4">
                                <h5 class="fw-bold mb-3"><i class="fa-solid fa-plus-circle text-primary me-2"></i> <span data-i18n="new_appt_title">નવી એપોઇન્ટમેન્ટ શિડ્યુલ કરો</span></h5>
                                <form id="booking-form" onsubmit="handleBooking(event)" class="row g-3">
                                    <div class="col-md-6">
                                        <label class="form-label fw-semibold" data-i18n="lbl_patient_name">દર્દીનું પૂરું નામ</label>
                                        <input type="text" id="patient_name" class="form-control" required placeholder="Ramesh Patel">
                                    </div>
                                    <div class="col-md-6">
                                        <label class="form-label fw-semibold" data-i18n="lbl_mobile">મોબાઇલ નંબર</label>
                                        <input type="text" id="patient_phone" class="form-control" required placeholder="+919876543210">
                                    </div>
                                    <div class="col-md-6">
                                        <label class="form-label fw-semibold" data-i18n="lbl_date">તારીખ</label>
                                        <input type="date" id="appointment_date" class="form-control" required>
                                    </div>
                                    <div class="col-md-6">
                                        <label class="form-label fw-semibold" data-i18n="lbl_slot">કલાક સ્લોટ</label>
                                        <select id="time_slot" class="form-select" required>
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
                                        <button type="submit" class="btn btn-primary fw-bold px-4 py-2">
                                            <i class="fa-solid fa-check-circle me-1"></i> <span data-i18n="btn_confirm_slot">સ્લોટ કન્ફર્મ કરો અને વોટ્સએપ મોકલો</span>
                                        </button>
                                    </div>
                                </form>
                            </div>
                        </div>

                        <div class="col-lg-5">
                            <div class="card card-custom p-4">
                                <h5 class="fw-bold mb-3"><i class="fa-solid fa-bolt text-warning me-2"></i> <span data-i18n="quick_actions_title">કવિક એક્શન્સ & ઓટોમેશન</span></h5>
                                <p class="text-muted small" data-i18n="quick_actions_desc">એક ક્લિકથી દર્દીઓને અડધી કલાક પહેલાનો રિમાઇન્ડર અને ડૉક્ટરને આજના દર્દીઓનું લિસ્ટ મોકલો.</p>
                                <button onclick="trigger30MinReminders()" class="btn btn-warning fw-bold text-dark w-100 py-2 mb-3">
                                    <i class="fa-solid fa-clock-rotate-left me-2"></i> <span data-i18n="btn_reminder_30m">30-મિનિટ દર્દી રિમાઇન્ડર મોકલો</span>
                                </button>
                                <button onclick="sendDoctorDailySummary()" class="btn btn-info fw-bold text-white w-100 py-2">
                                    <i class="fa-solid fa-paper-plane me-2"></i> <span data-i18n="btn_doctor_report">ડૉક્ટરને ડેઇલી રિપોર્ટ મોકલો</span> (+91 9099555744)
                                </button>
                            </div>
                        </div>
                    </div>

                    <!-- Appointments Table -->
                    <div class="card card-custom p-4">
                        <h5 class="fw-bold mb-3"><i class="fa-solid fa-list-check me-2"></i> <span data-i18n="all_appts_title">બધા જ એપોઇન્ટમેન્ટ્સ સ્લોટ્સ</span></h5>
                        <div class="table-responsive">
                            <table class="table table-hover align-middle">
                                <thead class="table-light">
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
                            <div class="card card-custom p-4">
                                <h5 class="fw-bold mb-3 text-success"><i class="fa-brands fa-whatsapp me-2"></i> <span data-i18n="wa_bot_console_title">વોટ્સએપ એઆઈ ચેટબોટ કન્સોલ</span></h5>
                                <p class="text-muted small" data-i18n="wa_bot_desc">કોઈ પણ દર્દી WhatsApp પર <strong>"Hi"</strong> અથવા <strong>"નમસ્તે"</strong> મોકલશે, એટલે AI ઓટોમેટીક જવાબ આપશે અને બુકિંગ કરશે:</p>

                                <div id="wa-chat-box" style="height: 320px; overflow-y: auto;" class="p-3 border rounded mb-3 bg-light">
                                    <div class="chat-bubble-agent">
                                        <i class="fa-brands fa-whatsapp me-1 text-success"></i> <strong>WhatsApp AI Bot:</strong> 👋 નમસ્તે! ડૉ. A. J. Sakhrelia ના ક્લિનિકમાં તમારું સ્વાગત છે. એપોઇન્ટમેન્ટ બુક કરવા માટે તમારું નામ જણાવશો?
                                    </div>
                                </div>

                                <div class="input-group">
                                    <input type="text" id="wa_user_input" class="form-control" placeholder="'Hi', 'રમેશ પટેલ' અથવા '10 AM'...">
                                    <button onclick="sendWaSimMessage()" class="btn btn-success fw-bold">
                                        <i class="fa-solid fa-paper-plane me-1"></i> <span data-i18n="btn_send">મોકલો</span>
                                    </button>
                                </div>
                            </div>
                        </div>

                        <div class="col-lg-5">
                            <div class="card card-custom p-4">
                                <h5 class="fw-bold mb-3"><i class="fa-solid fa-circle-info text-primary me-2"></i> <span data-i18n="how_wa_bot_works_title">WhatsApp ચેટબોટ કેવી રીતે કામ કરે છે?</span></h5>
                                <ol class="text-muted small">
                                    <li class="mb-2">દર્દી WhatsApp પર <strong>"Hi"</strong> અથવા <strong>"નમસ્તે"</strong> મોકલે છે.</li>
                                    <li class="mb-2">AI ચેટબોટ ઓટોમેટીક ડેટાબેઝમાંથી ઓપન સ્લોટ્સ ચેક કરીને ચેટમાં લિસ્ટ મોકલે છે.</li>
                                    <li class="mb-2">દર્દી સ્લોટ પસંદ કરે એટલે બુકિંગ થઈ જાય છે.</li>
                                    <li class="mb-2">ડૉક્ટર સાહેબના નંબર <code>+91 9099555744</code> પર અને દર્દીને કન્ફર્મેશન મેસેજ મોકલે છે.</li>
                                </ol>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- TAB 3: Voice Agent -->
                <div class="tab-pane fade" id="pane-voice">
                    <div class="row g-4 mb-4">
                        <div class="col-lg-6">
                            <div class="card card-custom p-4">
                                <h5 class="fw-bold mb-3 text-primary"><i class="fa-solid fa-microphone me-2"></i> <span data-i18n="voice_sim_title">ફ્રી માઇક્રોફોન ગુજરાતી કોલર (Voice Test)</span></h5>
                                <p class="text-muted small" data-i18n="voice_sim_desc">બ્રાઉઝર માઇક્રોફોન દ્વારા ગુજરાતીમાં AI એજન્ટ સાથે ફ્રી કોલિંગ ટેસ્ટ કરો:</p>
                                
                                <div id="voice-chat-box" style="height: 250px; overflow-y: auto;" class="p-3 border rounded mb-3 bg-light">
                                    <div class="chat-bubble-agent">
                                        <i class="fa-solid fa-headset me-1"></i> <strong>AI એજન્ટ:</strong> નમસ્તે! ડૉ. A. J. Sakhrelia ના ક્લિનિકમાં તમારું સ્વાગત છે. કૃપા કરીને તમારું પૂરું નામ જણાવશો?
                                    </div>
                                </div>

                                <div class="d-flex gap-2">
                                    <input type="text" id="sim_user_transcript" class="form-control" placeholder="ગુજરાતીમાં બોલો/લખો...">
                                    <button onclick="sendVoiceSimTurn()" class="btn btn-primary fw-bold">
                                        <i class="fa-solid fa-paper-plane me-1"></i> <span data-i18n="btn_speak">બોલો/મોકલો</span>
                                    </button>
                                </div>
                            </div>
                        </div>

                        <div class="col-lg-6">
                            <div class="card card-custom p-4">
                                <h5 class="fw-bold mb-3 text-dark"><i class="fa-solid fa-phone me-2"></i> <span data-i18n="voice_config_title">ટેલિફોની વેરિફિકેશન</span></h5>
                                <ul class="list-group mb-3 small">
                                    <li class="list-group-item d-flex justify-content-between">
                                        <span>ડૉક્ટર મોબાઇલ નંબર:</span>
                                        <strong class="text-primary">+91 9099555744</strong>
                                    </li>
                                    <li class="list-group-item d-flex justify-content-between">
                                        <span>વોઈસ લેંગ્વેજ:</span>
                                        <strong class="text-success">Gujarati (gu-IN) & English</strong>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>

                    <!-- Call Logs -->
                    <div class="card card-custom p-4">
                        <h5 class="fw-bold mb-3"><i class="fa-solid fa-phone-volume me-2"></i> <span data-i18n="call_logs_title">લાઈવ કોલ લોગ્સ</span></h5>
                        <div class="table-responsive">
                            <table class="table table-striped align-middle">
                                <thead class="table-light">
                                    <tr>
                                        <th>કોલર નંબર</th>
                                        <th>ઓડિયો બોલેલ</th>
                                        <th>AI જવાબ</th>
                                        <th>સ્ટેટસ</th>
                                    </tr>
                                </thead>
                                <tbody id="voice-logs-body">
                                    <!-- Dynamic -->
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>

                <!-- TAB 4: WhatsApp QR -->
                <div class="tab-pane fade" id="pane-whatsapp">
                    <div class="card card-custom p-4 mb-4">
                        <h5 class="fw-bold mb-3"><i class="fa-brands fa-whatsapp text-success me-2"></i> વોટ્સએપ ક્યુઆર કોડ કનેક્શન</h5>
                        <div class="row align-items-center">
                            <div class="col-md-5">
                                <div class="qr-box">
                                    <div id="qr-container">
                                        <i class="fa-solid fa-spinner fa-spin fa-2x text-primary"></i>
                                        <p class="mt-2 text-muted">ક્યુઆર કોડ લોડ થઈ રહ્યો છે...</p>
                                    </div>
                                    <button onclick="refreshQR()" class="btn btn-outline-primary btn-sm w-100 mt-3">
                                        <i class="fa-solid fa-rotate-right me-1"></i> રિફ્રેશ QR કોડ
                                    </button>
                                </div>
                            </div>
                            <div class="col-md-7">
                                <h6><strong>વોટ્સએપ કનેક્ટ કરવાની રીત:</strong></h6>
                                <ol class="text-muted">
                                    <li>મોબાઈલમાં <strong>WhatsApp</strong> ખોલો.</li>
                                    <li>Settings > <strong>Linked Devices</strong> માં જાઓ.</li>
                                    <li><strong>Link a Device</strong> પર ટેપ કરીને QR કોડ સ્કેન કરો.</li>
                                </ol>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- TAB 5: Patients Directory -->
                <div class="tab-pane fade" id="pane-patients">
                    <div class="card card-custom p-4">
                        <h5 class="fw-bold mb-3"><i class="fa-solid fa-users me-2"></i> <span data-i18n="patients_title">દર્દીઓની હિસ્ટ્રી અને ડિરેક્ટરી</span></h5>
                        <div class="table-responsive">
                            <table class="table table-bordered table-hover align-middle">
                                <thead class="table-light">
                                    <tr>
                                        <th data-i18n="th_patient_name">દર્દીનું નામ</th>
                                        <th data-i18n="th_phone">મોબાઈલ નંબર</th>
                                        <th>કુલ મુલાકાત</th>
                                        <th>છેલ્લી મુલાકાત</th>
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
                    <div class="card card-custom p-4">
                        <h5 class="fw-bold mb-3"><i class="fa-solid fa-hospital-user me-2"></i> <span data-i18n="hr_title">ક્લિનિક સ્ટાફ અને HR હેલ્પર</span></h5>
                        <div class="table-responsive">
                            <table class="table table-striped align-middle">
                                <thead class="table-light">
                                    <tr>
                                        <th>નામ</th>
                                        <th>હોદ્દો</th>
                                        <th>મોબાઈલ નંબર</th>
                                        <th>શિફ્ટ સમય</th>
                                        <th>સ્ટેટસ</th>
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
                    <div class="card card-custom p-4">
                        <h5 class="fw-bold mb-3"><i class="fa-solid fa-gear text-secondary me-2"></i> <span data-i18n="settings_title">ડૉક્ટર પ્રોફાઇલ અને ક્લિનિક સેટિંગ્સ</span></h5>
                        <form id="settings-form" onsubmit="saveSettings(event)" class="row g-3">
                            <div class="col-md-6">
                                <label class="form-label fw-semibold">ડૉક્ટર સાહેબનું નામ</label>
                                <input type="text" id="setting_doctor_name" class="form-control" required>
                            </div>
                            <div class="col-md-6">
                                <label class="form-label fw-semibold">ડૉક્ટરનો વોટ્સએપ નંબર</label>
                                <input type="text" id="setting_doctor_phone" class="form-control" required value="+919099555744">
                            </div>
                            <div class="col-md-6">
                                <label class="form-label fw-semibold">દવાખાનાનું નામ</label>
                                <input type="text" id="setting_clinic_name" class="form-control" required>
                            </div>
                            <div class="col-md-6">
                                <label class="form-label fw-semibold">ડેશબોર્ડ ભાષા (Dashboard Language)</label>
                                <select id="setting_dashboard_language" class="form-select" onchange="changeLanguage(this.value)">
                                    <option value="gu">ગુજરાતી (Gujarati)</option>
                                    <option value="en">English (US)</option>
                                </select>
                            </div>
                            <div class="col-12">
                                <label class="form-label fw-semibold">ક્લિનિકનું લોકેશન / ગૂગલ મેપ્સ લિંક</label>
                                <input type="text" id="setting_clinic_location" class="form-control" required>
                            </div>
                            <div class="col-12 mt-3">
                                <button type="submit" class="btn btn-success fw-bold px-4">
                                    <i class="fa-solid fa-floppy-disk me-1"></i> સેવ કરો (Save Settings)
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

    const i18nDict = {
        gu: {
            lang_label: "ભાષા (Language)",
            tab_appointments: "એપોઇન્ટમેન્ટ્સ",
            tab_wa_bot: "વોટ્સએપ ચેટબોટ",
            tab_voice: "એઆઈ વોઈસ એજન્ટ",
            tab_wa_qr: "વોટ્સએપ ક્યુઆર",
            tab_patients: "દર્દીઓની હિસ્ટ્રી",
            tab_hr: "ક્લિનિક HR સ્ટાફ",
            tab_settings: "પ્રોફાઇલ & સેટિંગ્સ",
            new_appt_title: "નવી એપોઇન્ટમેન્ટ શિડ્યુલ કરો",
            lbl_patient_name: "દર્દીનું પૂરું નામ",
            lbl_mobile: "મોબાઇલ નંબર",
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
            btn_send: "મોકલો",
            how_wa_bot_works_title: "WhatsApp ચેટબોટ કેવી રીતે કામ કરે છે?",
            voice_sim_title: "ફ્રી માઇક્રોફોન ગુજરાતી કોલર (Voice Test)",
            voice_sim_desc: "બ્રાઉઝર માઇક્રોફોન દ્વારા ગુજરાતીમાં AI એજન્ટ સાથે ફ્રી કોલિંગ ટેસ્ટ કરો:",
            btn_speak: "બોલો/મોકલો",
            voice_config_title: "ટેલિફોની વેરિફિકેશન",
            call_logs_title: "લાઈવ કોલ લોગ્સ",
            patients_title: "દર્દીઓની હિસ્ટ્રી અને ડિરેક્ટરી",
            hr_title: "ક્લિનિક સ્ટાફ અને HR હેલ્પર",
            settings_title: "ડૉક્ટર પ્રોફાઇલ અને ક્લિનિક સેટિંગ્સ"
        },
        en: {
            lang_label: "Language / ભાષા",
            tab_appointments: "Appointments",
            tab_wa_bot: "WhatsApp Chatbot",
            tab_voice: "AI Voice Agent",
            tab_wa_qr: "WhatsApp QR Sync",
            tab_patients: "Patient History",
            tab_hr: "Clinic HR Staff",
            tab_settings: "Profile & Settings",
            new_appt_title: "Schedule New Appointment",
            lbl_patient_name: "Patient Full Name",
            lbl_mobile: "Mobile Number",
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
            wa_bot_console_title: "Interactive WhatsApp AI Chatbot",
            wa_bot_desc: "When a patient sends 'Hi' or 'Hello' on WhatsApp, AI automatically replies, shows slots, and completes booking:",
            btn_send: "Send",
            how_wa_bot_works_title: "How WhatsApp AI Chatbot Works",
            voice_sim_title: "Free Microphone Gujarati Voice Caller",
            voice_sim_desc: "Test Gujarati voice calling for free directly using your browser microphone:",
            btn_speak: "Speak / Send",
            voice_config_title: "Telephony Verification",
            call_logs_title: "Live Voice Call Logs",
            patients_title: "Patient Registry & Visit History",
            hr_title: "Clinic Staff & HR Roster",
            settings_title: "Doctor Profile & Clinic Settings"
        }
    };

    function changeLanguage(lang) {
        document.getElementById('lang_toggle').value = lang;
        document.getElementById('setting_dashboard_language').value = lang;
        const dict = i18nDict[lang] || i18nDict['gu'];
        
        document.querySelectorAll('[data-i18n]').forEach(el => {
            const key = el.getAttribute('data-i18n');
            if (dict[key]) {
                el.innerText = dict[key];
            }
        });
        localStorage.setItem('doc_dashboard_lang', lang);
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
        data.logs.forEach(l => {
            tbody.innerHTML += `
                <tr>
                    <td><code>${l.caller_phone}</code></td>
                    <td>${l.transcript}</td>
                    <td><small class="text-primary">${l.agent_response}</small></td>
                    <td><span class="badge bg-success">${l.status}</span></td>
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

            if (data.status === 'AUTHENTICATED') {
                container.innerHTML = `<i class="fa-solid fa-circle-check text-success fa-4x"></i><h6 class="mt-3 text-success fw-bold">WhatsApp Connected!</h6>`;
                badge.className = 'badge bg-success status-badge';
                badge.innerHTML = `<i class="fa-solid fa-circle-check me-1"></i> WhatsApp Connected`;
            } else if (data.qr_data_url) {
                container.innerHTML = `<img src="${data.qr_data_url}" class="qr-img" alt="Scan QR">`;
                badge.className = 'badge bg-primary status-badge';
                badge.innerHTML = `<i class="fa-solid fa-qrcode me-1"></i> Scan QR Code`;
            } else {
                container.innerHTML = `<i class="fa-solid fa-qrcode fa-3x text-secondary"></i><p class="mt-2 text-muted">Generating QR...</p>`;
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
        data.appointments.forEach(a => {
            tbody.innerHTML += `
                <tr>
                    <td><code>${a.appointment_id}</code></td>
                    <td class="fw-bold">${a.patient_name}</td>
                    <td>${a.patient_phone}</td>
                    <td>${a.appointment_date}</td>
                    <td><span class="badge bg-primary">${a.time_slot}</span></td>
                    <td><span class="badge bg-success">${a.status}</span></td>
                </tr>
            `;
        });
    }

    async function loadPatients() {
        const res = await fetch('/api/patients');
        const data = await res.json();
        const tbody = document.getElementById('patients-table-body');
        tbody.innerHTML = '';
        data.patients.forEach(p => {
            tbody.innerHTML += `
                <tr>
                    <td class="fw-bold">${p.name}</td>
                    <td>${p.phone}</td>
                    <td><span class="badge bg-info text-dark">${p.total_visits} Visits</span></td>
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
        data.staff.forEach(s => {
            tbody.innerHTML += `
                <tr>
                    <td class="fw-bold">${s.name}</td>
                    <td><span class="badge bg-secondary">${s.role}</span></td>
                    <td>${s.phone}</td>
                    <td>${s.shift_timing}</td>
                    <td><span class="badge bg-success">Active</span></td>
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
