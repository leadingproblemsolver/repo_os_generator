---
    objective: Define core data objects.
    why_it_exists: Data model clarity makes integrations and tests reliable.
    how_to_use: Use alongside src/support_agent/models.py when adding or changing fields.
    dependencies: src/support_agent/models.py
    owner: Architect
    update_policy: Update when durable or API-visible fields change.
    examples: Ticket priority is a bounded value controlled by TicketPriority.
    related_files: architecture/INTERFACES.md
    ---


# Data Model

Core objects are implemented as typed dataclasses in `src/support_agent/models.py`: `CustomerProfile`, `MemoryItem`, `KnowledgeArticle`, `KnowledgeHit`, `SupportMessage`, `SupportResponse`, `Ticket`, `ToolResult`, `EscalationDecision`, and `EvaluationScore`.

Durable production storage must preserve object identity, timestamps, source attribution, and deletion/audit requirements.
