---
    objective: Describe the whole AI support platform at system level.
    why_it_exists: A single overview prevents code-first drift.
    how_to_use: Read before adding contexts or integrations.
    dependencies: ARCHITECTURE.md
    owner: Architect
    update_policy: Update when system components or relationships change.
    examples: Adding billing lookup requires a tool adapter, policy rules, tests, and proof.
    related_files: architecture/CONTEXT_MAP.md, architecture/INTERFACES.md
    ---


# System Overview

The system receives support messages, enriches them with customer and company context, generates a grounded response, records operational state, and escalates when automation should not continue. The local implementation is deterministic so behavior can be tested without external services.

## Component graph

```text
API -> Agent -> CRM
            -> Memory
            -> Knowledge Retriever
            -> Tool Registry
            -> Ticket Service
            -> Escalation Policy
            -> Evaluator
```
