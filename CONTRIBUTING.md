---
    objective: Define how humans and AI agents change the repository safely.
    why_it_exists: A repository operating system fails when contribution requires private context.
    how_to_use: Follow the change workflow, update the owned documents, and run validation before submission.
    dependencies: standards/, execution/, decisions/, proof/, tests/
    owner: Architect
    update_policy: Update when review process, ownership, or validation commands change.
    examples: A new CRM adapter requires an execution block, tests, and interface notes if behavior changes.
    related_files: CODE_OF_CONDUCT.md, standards/REVIEW_STANDARD.md, scripts/validate_repository_os.py
    ---


# Contributing

## Change workflow

1. Locate the owning context in `INDEX.md`.
2. Read the relevant execution block in `execution/`.
3. Implement the smallest complete change inside the correct boundary.
4. Add or update tests that prove the behavior.
5. Update proof, decision records, or architecture only when the change alters behavior, ownership, or contracts.
6. Run:

```bash
python scripts/validate_repository_os.py
python scripts/smoke_agent.py
python -m pytest
```

## Non-negotiables

- Do not change mission, architecture, or interfaces from implementation files.
- Do not create unowned directories.
- Do not duplicate documentation; link to the owning file.
- Do not merge behavior without proof.
- Do not add external service assumptions without an adapter contract.

## Pull request evidence

Every meaningful pull request must state: changed files, owning context, tests run, proof added, and risks introduced.
