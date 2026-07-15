# Blue Horizon Concierge Agent

**Greenfield — built live during the demo via GitHub Copilot plan mode.**

This repository is intentionally minimal. It exists so the live GitHub Copilot enablement demo can start from an almost blank application, then use Copilot plan mode to interview the presenter, write the BRD, design the architecture, create the implementation plan, build the app, and deploy it.

## Intended app

The app to be built live is an **AI Guest Concierge / shore-excursion recommender** for the fictional **Blue Horizon Cruise Line**. A guest will provide interests, travel style, accessibility needs, and a port or sailing. The application will call the sibling `bluehorizon-excursions-api` (`GET /excursions`, `GET /excursions/search`, and planned `GET /excursions/recommendations`) and use an LLM to recommend and explain shore excursions.

## Intended architecture

- Lightweight web front end for the guest concierge experience.
- Small TypeScript/Node API or agent backend.
- Excursion data from the sibling `bluehorizon-excursions-api`.
- LLM recommendations via Azure OpenAI or GitHub Models.
- Infrastructure as code with `azd` and Bicep.
- Deployment target: Azure Container Apps.

## What is here now

Only a tiny placeholder Node/Express service is included so `azd up` has a reliable pre-deploy fallback before the live build replaces it.

The audience should see the real application built from near-zero during the demo.

## Live-build artifacts

Copilot will generate these during the demo:

- `docs/BRD.md`
- `docs/architecture.md`
- `docs/implementation-plan.md`

## Local placeholder

```powershell
npm install
npm run build
npm start
```

Then open `http://localhost:3000`.

## Azure deployment

The presenter can deploy the placeholder or the completed live-built app with:

```powershell
azd auth login
azd env new bluehorizon-concierge-demo --location eastus2
azd up
```

Prerequisites: Azure CLI, Azure Developer CLI, Node.js, Docker or a compatible container build path available to `azd`, and permission to create a resource group, Azure Container Registry, Log Analytics workspace, Azure Container Apps environment, and Container App.

## Copilot custom assets

- `.github/copilot-instructions.md` guides Copilot toward the intended Blue Horizon stack and conventions.
- `.github/agents/solution-shaper.agent.md` uses the documented `.agent.md` front-matter style for Copilot custom agents.
- `.github/skills/brd-writer/SKILL.md` uses the documented repository skill-folder convention assumed for Copilot skills.
