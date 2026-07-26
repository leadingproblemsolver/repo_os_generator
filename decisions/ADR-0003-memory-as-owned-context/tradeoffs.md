---
    objective: Capture tradeoffs for ADR-0003-memory-as-owned-context.
    why_it_exists: The decision system requires this file for every architectural decision.
    how_to_use: Read alongside the sibling files before changing architecture.
    dependencies: decisions/ADR-0003-memory-as-owned-context/README.md
    owner: Architect
    update_policy: Append new evidence rather than rewriting historical decisions.
    examples: Customer memory as a dedicated bounded context
    related_files: ARCHITECTURE.md, repository.yaml
    ---

    # Tradeoffs

Pros: clear ownership, testable boundaries, adapter flexibility. Costs: more upfront structure and more documentation discipline.
