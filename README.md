🧭 CasePath — Intervention-Based Social Services Case System (v2)

CasePath is a full-stack decision-support platform for social workers that transforms intake data into structured intervention plans rather than static service recommendations.

This version introduces a major upgrade:

«Instead of matching people to services, the system designs corrective intervention strategies across multiple support layers.»

---

🧠 Core Philosophy

Traditional systems ask:

«“What service does this person fit into?”»

CasePath asks:

«“What combination of interventions is necessary to stabilize, support, and improve this situation?”»

This shifts the model from classification → action planning under complexity.

---

🚀 Key Upgrade in v2

From Service Matching → Intervention Design

The system now outputs three intervention layers:

🟥 1. Hands-on Corrective Interventions

High-intensity, immediate response actions.

Examples:

- Emergency shelter placement
- Crisis intervention teams
- Case worker home visits
- Medical or psychiatric stabilization coordination
- Legal aid activation

---

🟧 2. Structured Development Programs

Long-term improvement pathways.

Examples:

- Job training and placement programs
- Financial literacy coaching
- Substance recovery programs
- Education re-entry pathways
- Parenting support programs

---

🟨 3. Flexible Accommodation Pathways (NEW)

Adaptive support when no predefined program fits.

Examples:

- Temporary housing vouchers
- Unstructured cash assistance with oversight
- Custom case-worker designed support plans
- NGO/community matching
- Cross-agency coordination interventions

---

🧠 Decision Engine Overview

CasePath evaluates each case using a multi-factor intervention model:

Intervention Score =
  (Urgency × 0.4)
+ (Instability × 0.3)
+ (Skill Deficit × 0.2)
+ (System Fit Gap × 0.1)

---

📊 System Fit Gap (Critical Concept)

A new metric introduced in v2.

It measures:

«How poorly a case fits into predefined service categories.»

High system-fit gap means:

- multiple overlapping crises
- missing eligibility categories
- structural barriers
- rural / institutional mismatch
- undocumented complexity

This directly triggers flexible accommodation pathways.

---

🏗️ System Architecture

🔷 Frontend (React)

- Case intake wizard
- Intervention plan visualization
- Editable accommodation layer
- Case dashboard

🔶 Backend (FastAPI)

- Rule-based intervention engine
- Scoring system
- Case storage (MVP: in-memory)
- REST API endpoints

---

📁 Project Structure

casepath/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── routes.py
│   │   ├── engine.py
│   │   └── database.py
│   │
│   ├── requirements.txt
│   └── run.sh
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── api.js
│   │   ├── components/
│   │   │   ├── CaseWizard.jsx
│   │   │   ├── Dashboard.jsx
│   │   │   ├── InterventionView.jsx
│   │   │   └── StepQuestion.jsx
│   │
│   ├── index.html
│   ├── package.json
│   └── vite.config.js
│
└── README.md

---

⚙️ Installation

1. Clone Repository

git clone <repo-url>
cd casepath

---

2. Backend Setup

cd backend
pip install -r requirements.txt
bash run.sh

Backend runs at:

http://localhost:8000

---

3. Frontend Setup

cd frontend
npm install
npm run dev

Frontend runs at:

http://localhost:5173

---

🧭 Workflow

1. Intake Phase

Social worker enters:

- demographics
- housing status
- employment status
- mental health indicators

---

2. Intervention Scoring

System computes:

- urgency
- instability
- skill deficit
- system fit gap

---

3. Intervention Classification

Outputs one of:

🟥 HANDS-ON CRISIS RESPONSE

Immediate stabilization required

🟧 STRUCTURED DEVELOPMENT PATH

Program-based recovery and support

🟨 FLEXIBLE ACCOMMODATION REQUIRED

Non-standard, adaptive intervention required

---

4. Intervention Plan Output

Each case generates:

🟥 Immediate Actions

Crisis-level interventions

🟧 Development Pathways

Structured program assignments

🟨 Adaptive Support Layer

Custom, case-worker-defined solutions

---

🧠 Engine Logic Summary

if score > 0.75:
    return HANDS_ON_CRISIS

elif score > 0.45:
    return STRUCTURED_DEVELOPMENT

else:
    return FLEXIBLE_ACCOMMODATION

---

🖥️ Frontend Features

📌 Case Wizard

Step-by-step intake flow

📊 Dashboard

- Active cases
- Intervention categories
- workload overview

📄 Intervention View

- layered action plan
- editable accommodation section
- rationale transparency

---

🔌 API Endpoints

Create Case

POST /case

Get Case

GET /case/{case_id}

List Cases

GET /cases

---

🧠 Design Principles

✔ Intervention-first design

Focus on actions, not labels.

✔ Human-in-the-loop

Case workers retain full authority over decisions.

✔ Explainability

Every recommendation is traceable to input factors.

✔ Flexibility by design

System explicitly supports cases that do not fit standard programs.

---

🔥 Why This Version Matters

CasePath v2 introduces a critical capability:

«The system no longer fails when no service matches a case.»

Instead it:

- detects mismatch
- escalates to flexible intervention design
- enables custom support planning

This reflects real-world social service complexity.

---

🧬 Future Enhancements

🤖 AI Intervention Assistant

- suggests next steps dynamically
- fills missing intake information

---

📊 Funding Optimization Engine

- maps interventions to budget constraints
- forecasts system load

---

🧾 Audit + Compliance Layer

- full decision trace logs
- justification tracking per intervention

---

🧬 Bias Detection System

- identifies inconsistent classifications
- monitors demographic outcome distribution

---

🌐 Multi-Agency Coordination Graph

- shared intervention planning across institutions
- dependency tracking between agencies

---

⚠️ Limitations

- MVP uses simplified rule-based scoring
- No persistent database in base version
- Requires policy tuning for real-world deployment
- Not intended for automated eligibility denial

---

🧭 Final Philosophy

«CasePath is a structured reasoning system for human complexity—not a replacement for human judgment.»

---

📄 License

MIT (or organizational policy license)

---

✍️ Author

Designed as an intervention-focused case management framework for social services systems dealing with complex, non-linear human needs.
