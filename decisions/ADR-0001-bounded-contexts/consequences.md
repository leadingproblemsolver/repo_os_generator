---
    objective: Capture consequences for ADR-0001-bounded-contexts.
    why_it_exists: The decision system requires this file for every architectural decision.
    how_to_use: Read alongside the sibling files before changing architecture.
    dependencies: decisions/ADR-0001-bounded-contexts/README.md
    owner: Architect
    update_policy: Append new evidence rather than rewriting historical decisions.
    examples: Bounded contexts as primary architecture
    related_files: ARCHITECTURE.md, repository.yaml
    ---

    # Consequences

New behavior must be placed in an owned context. Interface changes require architecture review and proof updates.
