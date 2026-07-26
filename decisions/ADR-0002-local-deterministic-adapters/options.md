---
    objective: Capture options for ADR-0002-local-deterministic-adapters.
    why_it_exists: The decision system requires this file for every architectural decision.
    how_to_use: Read alongside the sibling files before changing architecture.
    dependencies: decisions/ADR-0002-local-deterministic-adapters/README.md
    owner: Architect
    update_policy: Append new evidence rather than rewriting historical decisions.
    examples: Local deterministic adapters before external services
    related_files: ARCHITECTURE.md, repository.yaml
    ---

    # Options

1. Single service with internal helpers.
2. Bounded contexts with explicit interfaces.
3. Separate deployable services from day one.
