# GitHub Copilot instructions

This repository is a greenfield live-demo scaffold for the fictional Blue Horizon Cruise Line AI Guest Concierge.

When building the app live:

- Start by interviewing the presenter before writing code.
- Produce `docs/BRD.md`, `docs/architecture.md`, and `docs/implementation-plan.md` before implementation.
- Prefer a TypeScript/Node backend that calls the sibling `bluehorizon-excursions-api`.
- Add a lightweight web front end for collecting guest interests, port/sailing, accessibility needs, and travel style.
- Use Azure OpenAI or GitHub Models for recommendation explanations.
- Keep deployment compatible with `azd` + Bicep + Azure Container Apps.
- Keep Blue Horizon fictional and generic; do not use Carnival branding.
- Keep secrets in environment variables and never commit credentials.
