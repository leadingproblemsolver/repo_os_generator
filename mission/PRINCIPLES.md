---
    objective: State product and technical principles.
    why_it_exists: Principles guide decisions when requirements conflict.
    how_to_use: Use these principles in decision records and review discussions.
    dependencies: decisions/, standards/
    owner: Architect
    update_policy: Update only through an architectural decision record.
    examples: Prefer transparent escalation over uncertain automated resolution.
    related_files: decisions/ADR-0001-bounded-contexts/decision.md
    ---


# Principles

- Ground customer answers in approved knowledge whenever policy-sensitive content is involved.
- Treat memory as a customer-benefit feature with consent, deletion, and audit requirements.
- Prefer small, explicit bounded contexts over broad service objects.
- Make every integration replaceable behind a stable interface.
- Escalate when uncertainty, risk, policy, or customer frustration exceeds defined thresholds.
- Make proof visible before claiming production readiness.
