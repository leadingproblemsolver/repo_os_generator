---
    objective: Capture decision for ADR-0002-local-deterministic-adapters.
    why_it_exists: The decision system requires this file for every architectural decision.
    how_to_use: Read alongside the sibling files before changing architecture.
    dependencies: decisions/ADR-0002-local-deterministic-adapters/README.md
    owner: Architect
    update_policy: Append new evidence rather than rewriting historical decisions.
    examples: Local deterministic adapters before external services
    related_files: ARCHITECTURE.md, repository.yaml
    ---

    # Decision

Use bounded contexts inside one repository, with explicit interfaces and tests. This provides clear ownership without premature deployment complexity.
