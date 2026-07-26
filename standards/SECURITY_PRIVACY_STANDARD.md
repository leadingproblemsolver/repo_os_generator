---
    objective: Own security_privacy_standard.
    why_it_exists: Standards convert implicit expectations into reviewable rules.
    how_to_use: Apply this standard during implementation and review.
    dependencies: CONTRIBUTING.md, repository.yaml
    owner: Builder
    update_policy: Update with a decision record if the standard changes architecture or ownership.
    examples: Reject changes that violate owned context boundaries.
    related_files: standards/README.md, decisions/
    ---

    # Security and Privacy Standard

Treat customer memory and CRM attributes as sensitive operational data. Production adapters must support audit, access control, deletion, and least-privilege integration credentials.
