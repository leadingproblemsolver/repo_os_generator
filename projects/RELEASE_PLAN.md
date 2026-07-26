---
    objective: Package project delivery into release stages.
    why_it_exists: A release plan connects roadmap intent to shippable units.
    how_to_use: Use this when cutting a deployment or internal demo.
    dependencies: ROADMAP.md, proof/RELEASE_EVIDENCE.md
    owner: Architect
    update_policy: Update before each release candidate.
    examples: Release 0.1 requires local agent smoke, tests, and repository validation.
    related_files: proof/QUALITY_GATES.md, infra/docker-compose.yml
    ---


# Release Plan

## Release 0.1 - Repository OS and local agent kernel

Included: repository operating system, deterministic agent kernel, local adapters, tests, validation script, smoke script, bilingual docs.

Required evidence: smoke output, pytest result, repository validation result.

## Release 0.2 - Persistent storage adapters

Included: database-backed memory, ticket storage, knowledge ingestion, migration scripts, privacy deletion path.

## Release 0.3 - External systems

Included: CRM adapter, ticketing adapter, LLM provider, vector retriever, deployment pipeline.
