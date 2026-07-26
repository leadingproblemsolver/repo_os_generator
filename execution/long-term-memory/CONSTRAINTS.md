---
    objective: Capture constraints for long-term-memory.
    why_it_exists: The execution contract requires complete feature context.
    how_to_use: Use this file during planning, implementation, review, and closure.
    dependencies: execution/ACTIVE_WORK.md
    owner: Architect
    update_policy: Update when the feature state changes.
    examples: long-term-memory: Customer-specific facts are remembered and recalled responsibly.
    related_files: execution/long-term-memory/README.md
    ---

    # Constraints

- Do not invent unsupported policy claims.
- Do not bypass context boundaries.
- Do not store sensitive customer facts without an explicit source.
- Do not mark complete without proof.
