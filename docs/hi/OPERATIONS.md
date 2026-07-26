---
    objective: Provide Hindi ऑपरेशन्स documentation.
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

Test dependencies install करने के बाद repository root से `make verify` चलाएँ।

## Expected proof

Healthy local run में smoke script, repository validation, और behavioral tests pass होते हैं।

## Production operation

Local operation deterministic adapters से चलता है। Production operation में existing interfaces को preserve करते हुए adapters replace करने होंगे, और tests, proof records, domain boundaries बनाए रखने होंगे।
