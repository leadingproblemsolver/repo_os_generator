---
objective: Index reproducible release evidence and explicit limitations.
why_it_exists: Publication claims must map to executable verification.
how_to_use: Run the commands below from a clean checkout.
dependencies: pyproject.toml, Makefile, tests/
owner: Builder
update_policy: Update with every release or changed verification surface.
examples: make verify
related_files: evidence/AI_HUMAN_PROVENANCE.md
---

# Release Evidence

## Verified locally

```bash
python -m pip install -e '.[test]'
make verify
```

The verification path exercises the deterministic generator, overwrite safety, generated-repository validation, the support-agent reference flow, and repository-OS structural validation.

## Not proven by offline tests

- Container execution in an environment with Docker or Podman.
- Hosted API behavior and external service adapters.
- User adoption, production scale, or long-term maintainability.
