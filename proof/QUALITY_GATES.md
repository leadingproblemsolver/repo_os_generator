---
    objective: Own quality_gates proof content.
    why_it_exists: Proof is required before a feature can be called complete.
    how_to_use: Use this file during feature closure and release review.
    dependencies: execution/, tests/, scripts/
    owner: Architect
    update_policy: Update when proof requirements or evidence changes.
    examples: A feature closes only after benchmark, acceptance, demonstration, validation, and metrics are visible.
    related_files: proof/README.md, execution/*/PROOF.md
    ---

    # Quality Gates

A feature fails if it has no execution block, no automated test, no smoke or demonstration path, no acceptance result, or unclear ownership.
