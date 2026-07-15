---
name: brd-writer
description: Turns a presenter interview transcript into a structured Business Requirements Document for the Blue Horizon Concierge Agent.
---

# BRD Writer Skill

Use this skill when the live demo has an interview transcript or presenter answers that need to become `docs/BRD.md`.

## Inputs

- Interview transcript or summarized answers.
- Intended user persona and scenario.
- Known integrations, constraints, and success criteria.

## Output

Write a structured Business Requirements Document with these sections:

1. Executive Summary
2. Business Goals
3. Target Users and Personas
4. User Problems and Opportunities
5. In-Scope Capabilities
6. Out-of-Scope Items
7. Functional Requirements
8. Non-Functional Requirements
9. Data and Integration Requirements
10. UX Requirements
11. Security, Privacy, and Compliance Notes
12. Acceptance Criteria
13. Open Questions

## Blue Horizon guidance

- Treat Blue Horizon Cruise Line as fictional and generic.
- For the intended app, focus on an AI guest concierge that recommends shore excursions using guest interests, port or sailing context, the sibling excursions API, and an LLM-generated explanation.
- Keep requirements demo-friendly and implementable during a live build.
