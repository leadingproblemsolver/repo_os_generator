---
    objective: Show the current feature execution blocks.
    why_it_exists: Active work must be explicit so contributors do not rely on private task lists.
    how_to_use: Use this file to pick the next implementation or proof task.
    dependencies: execution/*/
    owner: Architect
    update_policy: Update whenever a feature starts, pauses, closes, or changes priority.
    examples: knowledge-retrieval is active until search behavior and citation proof pass.
    related_files: ROADMAP.md, proof/QUALITY_GATES.md
    ---

    # Active Work

- `conversational-support/` - Customer message is converted into a grounded, useful support response.
- `long-term-memory/` - Customer-specific facts are remembered and recalled responsibly.
- `knowledge-retrieval/` - Approved company knowledge is retrieved and cited.
- `ticket-management/` - Support issues produce auditable tickets with priority and status.
- `tool-calling/` - Allowed tools execute through a controlled registry with audit results.
- `human-escalation/` - High-risk or unresolved conversations route to human review.
- `evaluation-loop/` - Interactions produce scores that support continuous improvement.
