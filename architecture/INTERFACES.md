---
    objective: Specify stable interface contracts for adapters.
    why_it_exists: Production services can replace local defaults only if interfaces remain stable.
    how_to_use: Read before changing method signatures or return types.
    dependencies: src/support_agent/*
    owner: Architect
    update_policy: Update with a decision record when interface behavior changes.
    examples: A vector-store retriever must return KnowledgeHit objects with article IDs and scores.
    related_files: src/support_agent/models.py, decisions/
    ---


# Interfaces

## MemoryStore

- `remember(customer_id, content, source)` records a durable memory item.
- `recall(customer_id)` returns customer memory ordered by newest first.

## KnowledgeRetriever

- `add_article(article)` stores approved knowledge.
- `search(query, limit)` returns scored knowledge hits.

## CRMClient

- `get_customer(customer_id)` returns account status and attributes.

## TicketService

- `open_or_update(customer_id, subject, summary, priority)` returns a ticket.

## ToolRegistry

- `execute(tool_name, arguments)` returns success status, display result, and audit metadata.

## EscalationPolicy

- `should_escalate(message, response, ticket)` returns a reasoned escalation decision.

## Evaluator

- `score(interaction)` returns groundedness, completeness, safety, and handoff scores.
