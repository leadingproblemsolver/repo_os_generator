---
    objective: Own coding_standard.
    why_it_exists: Standards convert implicit expectations into reviewable rules.
    how_to_use: Apply this standard during implementation and review.
    dependencies: CONTRIBUTING.md, repository.yaml
    owner: Builder
    update_policy: Update with a decision record if the standard changes architecture or ownership.
    examples: Reject changes that violate owned context boundaries.
    related_files: standards/README.md, decisions/
    ---

    # Coding Standard

Use typed Python, small modules, explicit dataclasses, deterministic tests, and stable interfaces. Runtime code must not read private repository context or mutate architecture docs.
