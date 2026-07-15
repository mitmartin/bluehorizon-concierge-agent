# Blue Horizon Concierge Agent

**Greenfield — built live during the demo with GitHub Copilot.**

This repository is intentionally (almost) empty. It exists so the live GitHub Copilot
enablement demo can start from **near zero** — no application code, no build config, no
infrastructure — and let Copilot interview the presenter, write the requirements, design
the architecture, plan the work, build the app, and deploy it.

## What is checked in on purpose

The only things here are the customizations we "bring in" and the empty doc placeholders
Copilot will fill during the demo:

- `.github/copilot-instructions.md` — how Blue Horizon wants Copilot to build (stack, conventions, guardrails).
- `.github/agents/solution-shaper.agent.md` — the custom agent that runs the interview-and-build.
- `.github/skills/brd-writer/SKILL.md` — a skill that turns the interview into a BRD.
- `docs/BRD.md`, `docs/architecture.md`, `docs/implementation-plan.md` — placeholders that read *"To be generated live."*

There is **no** `src/`, no `package.json` / `requirements.txt`, no `Dockerfile`, no
`azure.yaml`, and no `infra/`. Copilot creates all of that live during the demo.

## The app we build live

An **AI Guest Concierge / shore-excursion recommender** for the fictional
**Blue Horizon Cruise Line**. A guest provides interests, travel style, accessibility
needs, and a port or sailing; the app calls the sibling `bluehorizon-excursions-api`
(`GET /excursions`, `GET /excursions/search`) and uses an LLM to recommend and explain
shore excursions. The finished app deploys to Azure Container Apps.

## Pre-built fallback

If the live build runs short on time, a complete, tested version lives on the
**`prebuilt/horizon-helper`** branch (a self-contained Python app plus `infra/` and
`azure.yaml`). Deploy it with:

```powershell
git checkout prebuilt/horizon-helper
azd auth login
azd up
```

Prerequisites for deployment: Azure CLI, Azure Developer CLI (`azd`), and permission to
create a resource group, Azure Container Registry, Log Analytics workspace, Azure
Container Apps environment, and Container App.
