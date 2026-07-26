---
    objective: Capture problem for ADR-0003-memory-as-owned-context.
    why_it_exists: The decision system requires this file for every architectural decision.
    how_to_use: Read alongside the sibling files before changing architecture.
    dependencies: decisions/ADR-0003-memory-as-owned-context/README.md
    owner: Architect
    update_policy: Append new evidence rather than rewriting historical decisions.
    examples: Customer memory as a dedicated bounded context
    related_files: ARCHITECTURE.md, repository.yaml
    ---

    # Problem

Memory has consent, deletion, audit, and relevance concerns that differ from generic chat history.
