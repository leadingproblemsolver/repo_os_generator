---
    objective: Own ai_collaboration_standard.
    why_it_exists: Standards convert implicit expectations into reviewable rules.
    how_to_use: Apply this standard during implementation and review.
    dependencies: CONTRIBUTING.md, repository.yaml
    owner: Builder
    update_policy: Update with a decision record if the standard changes architecture or ownership.
    examples: Reject changes that violate owned context boundaries.
    related_files: standards/README.md, decisions/
    ---

    # AI Collaboration Standard

AI agents must read `braat.yaml`, `repository.yaml`, `INDEX.md`, and the relevant execution block before editing. They must not invent features, duplicate docs, or create unowned directories.
