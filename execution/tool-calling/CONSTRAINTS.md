---
    objective: Capture constraints for tool-calling.
    why_it_exists: The execution contract requires complete feature context.
    how_to_use: Use this file during planning, implementation, review, and closure.
    dependencies: execution/ACTIVE_WORK.md
    owner: Architect
    update_policy: Update when the feature state changes.
    examples: tool-calling: Allowed tools execute through a controlled registry with audit results.
    related_files: execution/tool-calling/README.md
    ---

    # Constraints

- Do not invent unsupported policy claims.
- Do not bypass context boundaries.
- Do not store sensitive customer facts without an explicit source.
- Do not mark complete without proof.
