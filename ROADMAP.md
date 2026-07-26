---
    objective: Make sequencing explicit for product and repository maturity.
    why_it_exists: Continuous improvement requires visible priorities and completion definitions.
    how_to_use: Use this file to decide what should be worked on next and what proof closes each stage.
    dependencies: execution/, proof/BENCHMARKS.md, decisions/
    owner: Architect
    update_policy: Review weekly or before any major implementation push.
    examples: Stage 1 closes only after local smoke, tests, and repository validation pass.
    related_files: execution/ACTIVE_WORK.md, proof/METRICS.md
    ---


# Roadmap

## Stage 1 - Local agent kernel

Completion definition: deterministic local agent handles support conversation, memory, knowledge retrieval, ticket creation, tool execution, escalation decision, and evaluation score.

## Stage 2 - Persistent memory and knowledge

Completion definition: customer memory and company knowledge use production storage with migration, backup, deletion, consent, and retrieval tests.

## Stage 3 - CRM and ticketing integrations

Completion definition: adapter contracts connect to selected CRM and ticketing systems with retry, audit logging, and failure-safe fallback.

## Stage 4 - LLM and RAG hardening

Completion definition: provider integration supports prompt versioning, retrieval citation checks, safety constraints, and regression benchmarks.

## Stage 5 - Operations and continuous improvement

Completion definition: dashboards, incident playbooks, eval reports, feedback loops, and release gates are active.
