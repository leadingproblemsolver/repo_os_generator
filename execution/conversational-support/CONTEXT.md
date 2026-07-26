---
    objective: Capture context for conversational-support.
    why_it_exists: The execution contract requires complete feature context.
    how_to_use: Use this file during planning, implementation, review, and closure.
    dependencies: execution/ACTIVE_WORK.md
    owner: Architect
    update_policy: Update when the feature state changes.
    examples: conversational-support: Customer message is converted into a grounded, useful support response.
    related_files: execution/conversational-support/README.md
    ---

    # Context

The repository implements this feature through bounded contexts and deterministic tests. Production adapters must preserve the same behavior contract.
