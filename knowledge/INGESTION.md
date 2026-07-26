---
    objective: Describe knowledge ingestion rules.
    why_it_exists: Ungoverned ingestion can produce unsupported or stale support answers.
    how_to_use: Use before connecting documentation sources, help centers, or internal policy libraries.
    dependencies: knowledge/COMPANY_KNOWLEDGE_SCHEMA.md
    owner: Builder
    update_policy: Update when source systems, freshness rules, or approval workflows change.
    examples: Only approved refund policy articles can ground refund answers.
    related_files: src/support_agent/knowledge/retriever.py
    ---


# Knowledge Ingestion

Accepted content must be approved, source-attributed, dated, and retrievable by customer-facing intent. Production ingestion must reject duplicate IDs, track freshness, and preserve deletion or replacement history.
