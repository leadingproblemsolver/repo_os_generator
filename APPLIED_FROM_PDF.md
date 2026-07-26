---
    objective: Record how the uploaded PDF contract was applied.
    why_it_exists: The generated repository must preserve the source operating contract.
    how_to_use: Use this file to audit the transformation from PDF/YAML contract to repository artifact.
    dependencies: Repository Operating System Generator.pdf, repo_os_gen.yaml
    owner: Architect
    update_policy: Update if the source contract or generated repository scope changes.
    examples: The PDF required root files, bilingual docs, execution blocks, decision files, proof files, and repository configuration; this repository implements those structures.
    related_files: README.md, repository.yaml, braat.yaml
    ---


# Applied Source Contract

The uploaded PDF and `repo_os_gen.yaml` specify a BRAAT v2 repository operating system, generated here against a deterministic customer-support sample domain (no AI/LLM component — see README.md). This repository applies that contract by generating:

- Required root documents and machine-readable repository configuration.
- Explicit directory ownership and descriptions.
- Bilingual documentation under `docs/en/` and `docs/hi/` with matching file names.
- Execution blocks for the core product features.
- Decision records with problem, options, decision, tradeoffs, consequences, and revisit triggers.
- Proof artifacts for benchmarks, acceptance, demonstration, validation, and metrics.
- A deterministic local runtime kernel that exercises conversation, memory, knowledge retrieval, ticket management, tools, escalation, and evaluation.
