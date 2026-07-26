---
    objective: Provide English operations documentation.
    why_it_exists: Bilingual documentation is required with identical structure and file names.
    how_to_use: Read this document in the chosen language; keep section structure aligned across languages.
    dependencies: docs/en, docs/hi, OPERABILITY.md
    owner: Architect
    update_policy: Update both languages in the same change.
    examples: English and Hindi files share names and sections.
    related_files: documentation rules in braat.yaml
    ---

# Operations

## Local operation

Run `make verify` from the repository root after installing the package with test dependencies.

## Expected proof

A healthy local run passes the smoke script, repository validation, and behavioral tests.

## Production operation

Local operation uses deterministic adapters. Production operation requires replacing adapters behind existing interfaces while preserving tests, proof records, and domain boundaries.
