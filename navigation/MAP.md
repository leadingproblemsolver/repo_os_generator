---
    objective: Map repository relationships.
    why_it_exists: Obvious relationships prevent duplicate documentation and hidden context.
    how_to_use: Use this when deciding whether to edit docs, code, tests, or proof.
    dependencies: INDEX.md, repository.yaml
    owner: Architect
    update_policy: Update when primary relationships change.
    examples: Runtime behavior change links to execution block, proof, tests, and relevant architecture.
    related_files: architecture/CONTEXT_MAP.md
    ---


# Repository Map

```text
mission -> roadmap -> execution -> implementation -> tests -> proof -> decisions when boundaries change
architecture -> interfaces -> src/support_agent -> tests -> proof
knowledge -> retrieval rules -> src/support_agent/knowledge -> evaluation
standards -> code review -> implementation and scripts
```
