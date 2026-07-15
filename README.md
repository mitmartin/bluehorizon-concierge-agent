# Horizon Helper — pre-built fallback (tested reference)

> **This branch is the safety net for Demo 2.** `main` is the empty greenfield scaffold you build live. If the live build runs into trouble, `git checkout prebuilt/horizon-helper` and you have a **working, tested** app.

**Horizon Helper** is a small chat web app: a guest describes their port, interests, and budget, and an **Azure AI Foundry agent** recommends 2–3 shore excursions from a curated list. Built with FastAPI + `azure-ai-agents` + a static UI. Verified working end-to-end against a real Foundry project on 2026-07-15.

## Run it locally (proven — this is the primary fallback)
```powershell
# 1) Python deps
python -m venv .venv; .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

# 2) Point at the Foundry project + model (Entra auth via your az login)
az login                      # if not already
$env:AI_FOUNDRY_PROJECT_ENDPOINT = "https://emailagent-mcaps-aifoundry.services.ai.azure.com/api/projects/project-mcaps"
$env:AI_FOUNDRY_MODEL_DEPLOYMENT = "gpt-4o-mini"

# 3) Run
uvicorn app.main:app --host 127.0.0.1 --port 8000
# open http://127.0.0.1:8000  ->  try: "Cozumel, snorkeling, 2 kids, ~$150pp"
```

## What's inside
- `app/main.py` — FastAPI: serves the UI, `GET /health`, `POST /api/chat`.
- `app/agent.py` — the Foundry agent wiring (`AgentsClient`, `DefaultAzureCredential`, one agent + one thread).
- `app/excursions.py` — the ~12-item excursion catalog + the agent's grounding instructions.
- `static/index.html`, `static/app.js` — the chat UI.
- `requirements.txt` — **pinned** versions known to work (`azure-ai-agents==1.1.0`).

## Deploy to Azure (optional)
`azd up` builds and deploys the container. For the agent to work in the cloud, the Container App's managed identity needs the **Azure AI User** role on the Foundry account, plus the two `AI_FOUNDRY_*` env vars set on the app. (Locally you don't need this — your `az login` covers auth.)

## Prerequisites
- An Azure AI Foundry project with a `gpt-4o-mini` deployment (we use the existing `emailagent-mcaps-aifoundry / project-mcaps`).
- Signed in via `az login` (no API keys — MCAPS uses Entra).
