---
    objective: Capture proof for ticket-management.
    why_it_exists: The execution contract requires complete feature context.
    how_to_use: Use this file during planning, implementation, review, and closure.
    dependencies: execution/ACTIVE_WORK.md
    owner: Builder
    update_policy: Update when the feature state changes.
    examples: ticket-management: Support issues produce auditable tickets with priority and status.
    related_files: execution/ticket-management/README.md
    ---

    # Proof

Benchmark: local deterministic interaction.
Acceptance: tests pass and response contains a grounded answer, ticket state, and evaluation score.
Demonstration: `python scripts/smoke_agent.py`.
Validation: `python scripts/validate_repository_os.py` and `python -m pytest`.
Metrics: groundedness, completeness, safety, escalation correctness.
