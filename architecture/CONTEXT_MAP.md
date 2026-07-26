---
    objective: Define bounded contexts and dependency direction.
    why_it_exists: Bounded contexts prevent broad, fragile changes.
    how_to_use: Use before creating modules or moving behavior.
    dependencies: src/support_agent/
    owner: Architect
    update_policy: Update when a context is added, removed, split, or merged.
    examples: Knowledge retrieval can score articles but cannot create tickets.
    related_files: ARCHITECTURE.md, architecture/INTERFACES.md
    ---


# Context Map

| Context | Responsibility | May call | Must not own |
|---|---|---|---|
| agent | Orchestration | all context ports | persistent implementation details |
| memory | Customer memory | models | CRM policy, knowledge search |
| knowledge | Retrieval | models | customer profile truth |
| crm | Customer profile | models | support tickets |
| tickets | Ticket lifecycle | models | response generation |
| tools | Controlled actions | models | architecture decisions |
| escalation | Handoff decision | models | ticket storage |
| evaluation | Quality scoring | models | response orchestration |
| api | External boundary | agent | domain logic |
