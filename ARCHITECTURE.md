---
    objective: Describe the system architecture and ownership boundaries.
    why_it_exists: Architectural ambiguity makes AI-generated implementation drift and human onboarding slow.
    how_to_use: Read this before changing runtime code or adding external integrations.
    dependencies: architecture/SYSTEM_OVERVIEW.md, architecture/CONTEXT_MAP.md, src/support_agent/
    owner: Architect
    update_policy: Update when bounded contexts, interfaces, storage, integration, or deployment assumptions change.
    examples: Ticket creation belongs in tickets; escalation policy decides whether humans must review.
    related_files: architecture/INTERFACES.md, decisions/, repository.yaml
    ---


# Architecture

## System shape

The platform is organized as bounded contexts connected through explicit ports:

- `agent`: orchestration of customer messages, memory, retrieval, tools, tickets, escalation, and evaluation.
- `memory`: long-term customer memory records with consent-aware summaries.
- `knowledge`: company knowledge retrieval and citation packaging.
- `crm`: customer profile lookup and account context.
- `tickets`: support ticket lifecycle and audit trail.
- `tools`: controlled tool-calling registry.
- `escalation`: human handoff policy.
- `evaluation`: quality scoring and regression signals.
- `api`: HTTP boundary for external clients.

## Dependency rule

Domain models are shared through `src/support_agent/models.py`. Bounded contexts can depend on models and their own ports. The agent orchestrator can depend on all bounded contexts. Infrastructure adapters must not change domain contracts.

## Runtime flow

1. API receives a customer message.
2. Agent loads CRM profile and memory.
3. Agent retrieves relevant knowledge articles.
4. Tool registry executes allowed tools when policy permits.
5. Ticket service records issue state.
6. Escalation policy checks risk, sentiment, and unresolved intent.
7. Evaluator scores the response against acceptance criteria.
8. Agent returns answer, citations, ticket state, memory updates, and escalation status.

## Production integration path

The local in-memory adapters are executable defaults. Production replaces them with persistent adapters while preserving the same public methods and tests.
