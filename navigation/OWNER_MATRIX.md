---
    objective: Show who owns each type of change.
    why_it_exists: Ownership must be clear for human and AI collaboration.
    how_to_use: Use this before approving or rejecting a change.
    dependencies: repository.yaml
    owner: Architect
    update_policy: Update with role or ownership changes.
    examples: Builder can implement a ticket adapter but cannot redefine ticket architecture.
    related_files: CONTRIBUTING.md, standards/REVIEW_STANDARD.md
    ---


# Owner Matrix

| Area | Architect | Builder |
|---|---:|---:|
| Mission | Owns | Reads |
| Architecture | Owns | Implements |
| Interfaces | Owns | Implements |
| Runtime code | Reviews boundaries | Owns |
| Tests | Defines proof needs | Owns execution |
| Infrastructure | Sets requirements | Owns |
| Decisions | Owns | Supplies implementation evidence |
| Proof | Owns standards | Supplies measurements |
