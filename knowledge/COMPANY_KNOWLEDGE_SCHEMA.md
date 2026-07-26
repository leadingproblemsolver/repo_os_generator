---
    objective: Define the structure of approved support knowledge.
    why_it_exists: RAG quality depends on governed content and source attribution.
    how_to_use: Use this before adding ingestion or retrieval adapters.
    dependencies: src/support_agent/knowledge/retriever.py
    owner: Builder
    update_policy: Update when article schema or citation requirements change.
    examples: Each article has id, title, body, tags, and source.
    related_files: architecture/DATA_MODEL.md, proof/BENCHMARKS.md
    ---


# Company Knowledge Schema

Required fields: `article_id`, `title`, `body`, `tags`, `source`, and `updated_at`. Retrieval responses must include article ID, title, source, and score so customer answers can cite grounding.
