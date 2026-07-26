---
    objective: Define project terms once to prevent duplicate explanations.
    why_it_exists: AI-native repositories drift when terms are defined differently across files.
    how_to_use: Consult this file before naming contexts, fields, metrics, or proof artifacts.
    dependencies: architecture/, proof/, src/support_agent/models.py
    owner: Architect
    update_policy: Update when a term becomes part of architecture, metrics, or execution language.
    examples: Memory item means a customer-specific durable fact, not generic chat history.
    related_files: ARCHITECTURE.md, repository.yaml
    ---


# Glossary

- **Agent kernel**: The orchestrator that turns an incoming customer message into a response, ticket state, memory update, and proof signal.
- **Bounded context**: A domain area with clear ownership and interface boundaries.
- **Customer memory**: Durable customer-specific information that improves future support while respecting consent and deletion requirements.
- **Company knowledge**: Approved support content retrieved to ground answers.
- **Execution block**: A feature-specific work unit containing why, context, inputs, outputs, constraints, acceptance, handoff, and proof.
- **Human escalation**: Routing a conversation to a human when risk, unresolved ambiguity, policy, or customer state requires review.
- **Proof**: Evidence that a feature works: benchmark, acceptance result, demonstration, validation, and metrics.
- **Repository operating system**: The navigational, architectural, proof, and execution layer that lets humans and AI collaborate without hidden context.
