---
    objective: Explain and run the repository without external meetings.
    why_it_exists: The source contract requires the repository itself to be the primary cognitive interface for human and AI collaboration.
    how_to_use: Start here, then follow INDEX.md for deterministic navigation and scripts/smoke_agent.py for an executable check.
    dependencies: repository.yaml, braat.yaml, INDEX.md, ARCHITECTURE.md, src/support_agent/agent.py
    owner: Architect
    update_policy: Update whenever repository entrypoints, architecture, or operating rules change.
    examples: A contributor can read this file, run the smoke script, and know where work belongs.
    related_files: INDEX.md, ARCHITECTURE.md, ROADMAP.md, navigation/START_HERE.md
    ---


# repo-os-generator

## Production correction

This release now contains an actual deterministic generator and validator. `repo-os init` consumes a bounded JSON project specification, stages a repository operating system atomically, refuses to overwrite nonempty targets by default, writes a content-hash manifest, and validates the resulting ownership surfaces. The existing `support_agent` package remains an explicit reference domain rather than the generator itself.

```bash
repo-os init --spec examples/project-spec.json --target /tmp/incident-first-check-analyzer
repo-os validate /tmp/incident-first-check-analyzer
```


This repository is a **repository-operating-system generator**: a reusable structure (ownership roles, execution blocks, decision records, proof artifacts) produced from a PDF/YAML contract. This instance validates the generator against one sample domain — customer support — using a **deterministic, non-AI reference implementation**. No LLM, embedding, or retrieval-augmented-generation call exists anywhere in `src/`; "knowledge retrieval" is keyword matching and "answer composition" is string templating. Swapping in real AI components is exactly the kind of change the port boundaries under `src/support_agent/` are designed to accept — it just hasn't been done yet.

## What the sample implementation actually does

Demonstrates the generator's structure against a deterministic, in-memory support-agent simulation: conversational response composition (template-based, not AI), customer memory recall/write, lexical (keyword) knowledge lookup, in-memory CRM and ticketing, keyword-triggered escalation, and rule-based evaluation. Real conversational AI, retrieval-augmented generation, and persistent storage are not implemented — they are the intended next step behind the existing port interfaces, not a current capability.

## Start in five minutes

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -e ".[test]"
make verify
```

The verify command runs the smoke script, repository-OS validation, and behavioral tests. The smoke script exercises memory, knowledge retrieval, ticket creation, escalation policy, and evaluation using deterministic local adapters. Production adapters belong behind the same ports defined under `src/support_agent/`.

## Operating model

- Architect owns cognition: mission, architecture, interfaces, priorities, decisions, evaluation, and proof.
- Builder owns throughput: implementation, integrations, tests, infrastructure, deployment, and operational hardening.
- Every feature has an execution block under `execution/`.
- Every architectural decision has a decision record under `decisions/`.
- Every feature has proof under `proof/` or inside its execution block.

## Human handoff

Before sending this repository to a junior or intern, include `navigation/JUNIOR_NAVIGATION_GUIDE_HI.md`. It gives the safest reading order, first command, role limits, blocked-message format, and completion format in simple Hindi.

## Repository boundaries

This repository intentionally separates product cognition from implementation code. Cognitive assets live in `mission/`, `navigation/`, `architecture/`, `execution/`, `decisions/`, `proof/`, `standards/`, and `templates/`. Runtime code lives in `src/`, tests in `tests/`, and deployment assets in `infra/`.

## Operability

Use `OPERABILITY.md` as the single command and proof guide. A change is complete only when `make verify` passes and the relevant proof file is updated.

## Current production-readiness position

The repository is complete enough for local execution, contributor onboarding, deterministic evaluation, and adapter replacement. External production services such as a hosted database, CRM, ticketing system, vector store, and LLM provider must be connected by implementing the existing ports without changing domain boundaries.
