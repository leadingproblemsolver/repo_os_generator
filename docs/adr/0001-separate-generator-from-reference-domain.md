# ADR 0001 — Separate repository generation from the support-agent reference domain

## Status

Accepted.

## Context

The repository claimed to be a repository-operating-system generator, while its executable code only demonstrated a deterministic support agent. That mismatch weakened product clarity and evidence integrity.

## Decision

Add a dedicated `repo_os_generator` package and `repo-os` CLI. Keep `support_agent` as a reference domain that proves generated boundaries can hold executable code.

## Alternatives

1. Rename the repository to the support-agent sample. Rejected because the reusable generator contract is the strategic asset.
2. Generate repositories only through prompts. Rejected because generation, overwrite safety, and validation need deterministic behavior.

## Consequences

The repository now has two explicit surfaces: generator product and reference implementation. Future adapters must not blur those claims.
