# PharmaQMS AI Copilot

> AI-powered Pharmaceutical Quality Management System — complaint intake, classification, root cause analysis, CAPA, and regulatory compliance.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![CI](https://github.com/karthik-ak-Git/Aivoa-Qa/actions/workflows/ci.yml/badge.svg)](https://github.com/karthik-ak-Git/Aivoa-Qa/actions/workflows/ci.yml)

---

## Architecture

```
┌─────────────────────┐      ┌──────────────────────────┐
│   Frontend (React)  │─────▶│   Backend (FastAPI)       │
│   Port 5173         │      │   Port 8000               │
│                     │      │                           │
│  - Complaint Form   │      │  - Writer Agent (Groq)    │
│  - Copilot Chat     │      │  - RAG + ChromaDB         │
│  - Form Preview     │      │  - Supabase / PostgreSQL  │
└─────────────────────┘      └──────────────────────────┘
                                      │
                                      ▼
                             ┌──────────────────────┐
                             │   Knowledge Base      │
                             │   (75+ pharma docs)   │
                             └──────────────────────┘
```

---

## Prerequisites

- **Python 3.12+** — backend runtime
- **Node.js 20+** — frontend runtime
- **Docker & Docker Compose** — containerized run (recommended)
- **Groq API key** — LLM inference (get one at https://console.groq.com)
- **Supabase account** (optional) — persistence layer

---

## Quick Start (Docker — Recommended)

```bash
# 1. Clone
git clone https://github.com/karthik-ak-Git/Aivoa-Qa.git
cd Aivoa-Qa

# 2. Configure environment
cp backend/.env.example backend/.env
# Edit backend/.env — set at minimum GROQ_API_KEY and SUPABASE_* fields

# 3. Run
docker compose up --build
```

- Frontend: http://localhost:5173
- Backend API: http://localhost:8000
- API docs: http://localhost:8000/docs

---

## Manual Setup (Without Docker)

### Backend

```bash
cd backend

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate   # Windows
# source .venv/bin/activate   # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env — set GROQ_API_KEY (required) and Supabase credentials (optional)

# Run
python run.py
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at http://localhost:5173, proxying `/api` to the backend at http://localhost:8000.

---

## Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `GROQ_API_KEY` | **Yes** | — | Groq API key for LLM inference |
| `SUPABASE_URL` | No | — | Supabase project URL |
| `SUPABASE_ANON_KEY` | No | — | Supabase anonymous key |
| `SUPABASE_SERVICE_ROLE_KEY` | No | — | Supabase service role key |
| `SUPABASE_PROJECT_ID` | No | — | Supabase project ID |
| `DATABASE_URL` | No | — | Direct PostgreSQL connection string |
| `OPENROUTER_API_KEY` | No | — | Alternative LLM provider |
| `LOG_LEVEL` | No | `INFO` | Logging level |

Full list in `backend/.env.example`.

---

## Docker Images

### Build & Run

```bash
# Build and start all services
docker compose up --build

# Run in background
docker compose up --build -d

# View logs
docker compose logs -f

# Stop
docker compose down

# Stop and remove volumes (resets ChromaDB index)
docker compose down -v
```

### Individual Images

```bash
# Backend only
docker build -t pharmaqms-backend -f backend/Dockerfile .
docker run -p 8000:8000 --env-file backend/.env pharmaqms-backend

# Frontend only
docker build -t pharmaqms-frontend -f frontend/Dockerfile .
docker run -p 5173:80 pharmaqms-frontend
```

---

## CI/CD

This project uses GitHub Actions for continuous integration.

### Pipeline Stages

| Stage | Description |
|-------|-------------|
| `lint-backend` | Python linting via ruff |
| `lint-frontend` | ESLint on TypeScript/React |
| `build-frontend` | TypeScript compilation + Vite build |
| `docker-build` | Builds both Docker images with layer caching |

### Workflow file

`.github/workflows/ci.yml` — runs on push/PR to `main` and `develop`.

---

## What Is This?

A comprehensive pharmaceutical QMS application with an AI copilot that assists with:

- **Complaint Intake** — Parse natural-language descriptions into structured complaint forms
- **Classification** — Auto-classify by severity, category, and product type
- **Root Cause Analysis** — RAG-powered suggestions referencing 80+ root causes
- **CAPA Generation** — Propose corrective and preventive actions
- **Knowledge Base** — 75+ documents across 18 pharma QMS domains

### Knowledge Domains

| Domain | Coverage |
|--------|----------|
| Complaint Management | 14 categories, 120+ terms, 9 structured cases |
| Root Cause Analysis | 6M taxonomy, 80+ root causes |
| CAPA Management | Full lifecycle, 7-step process |
| Deviation Management | Classification, investigation framework |
| Investigations | Phase I/II, RCA methods, trend analysis |
| Regulatory Compliance | FDA 21 CFR, ICH Q7-Q12, EU GMP, WHO |
| FDA Enforcement | 11 recalls, 10 warning letters |
| Medicines | 100+ drugs across 10 therapeutic categories |
| Manufacturing | 7 stages, API + FDF, CPPs |
| Equipment | 25 types with maintenance schedules |
| Packaging | 14 types, defect taxonomy |
| Dosage Forms | 24 forms with stability profiles |
| Quality Control | Testing procedures, OOS/OOT |

**Total: 75+ documents, 18 domains, 228+ citations from 36 authoritative sources.**

---

## Folder Structure

```
Aivoa-Qa/
├── README.md
├── docker-compose.yml
├── .dockerignore
├── .github/workflows/ci.yml
│
├── backend/                      # FastAPI Python backend
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── run.py
│   ├── .env.example
│   └── app/
│       ├── main.py               # FastAPI entry point
│       ├── agents/               # Writer, Editor, OCR agents
│       ├── api/                  # REST endpoints
│       ├── core/                 # Config, logging
│       ├── database/             # DB models + connection
│       ├── graph/                # LangGraph workflow
│       ├── knowledge/            # Knowledge base loader
│       ├── retriever/            # ChromaDB vector store + retrieval
│       ├── services/             # Groq, Supabase, OpenRouter
│       └── schemas/              # Pydantic schemas
│
├── frontend/                     # React + Vite + Tailwind
│   ├── Dockerfile
│   ├── nginx.conf
│   ├── package.json
│   ├── vite.config.ts
│   └── src/
│       ├── App.tsx
│       ├── components/
│       │   ├── ComplaintForm.tsx
│       │   └── CopilotChat.tsx
│       ├── store/                # Redux Toolkit
│       └── services/             # API client
│
├── knowledge-base/               # 75+ pharma QMS documents
│   ├── knowledge_base_index.json
│   ├── complaint_categories/
│   ├── complaint_terms/
│   ├── complaint_examples/
│   ├── root_cause_library/
│   ├── CAPA/
│   ├── regulations/
│   ├── medicines/
│   ├── manufacturing/
│   └── ... (18 domains)
│
└── screenshots/
```

---

## License

MIT — see [LICENSE](./LICENSE).
