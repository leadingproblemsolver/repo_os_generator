---
    objective: Capture context for tool-calling.
    why_it_exists: The execution contract requires complete feature context.
    how_to_use: Use this file during planning, implementation, review, and closure.
    dependencies: execution/ACTIVE_WORK.md
    owner: Architect
    update_policy: Update when the feature state changes.
    examples: tool-calling: Allowed tools execute through a controlled registry with audit results.
    related_files: execution/tool-calling/README.md
    ---

    # Context

The repository implements this feature through bounded contexts and deterministic tests. Production adapters must preserve the same behavior contract.
