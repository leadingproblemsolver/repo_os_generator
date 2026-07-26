---
objective: Provide simple junior contributor navigation in English.
why_it_exists: Bilingual contributor documentation must keep the same file names and section structure.
how_to_use: Read before starting first assigned work.
dependencies: docs/hi/JUNIOR_NAVIGATION_GUIDE.md, navigation/JUNIOR_NAVIGATION_GUIDE_HI.md
owner: Architect
update_policy: Update English and Hindi versions in the same change.
examples: A junior contributor can run the repo and report proof clearly.
related_files: navigation/START_HERE.md, OPERABILITY.md
---

# Junior Navigation Guide

## Goal

This repository is not only code. It is a working system.

Your job is to start in the right place, avoid unsafe changes, protect architecture, test every change, and explain exactly where you are stuck if blocked.

## Reading order

Read these first:

1. `README.md`
2. `INDEX.md`
3. `OPERABILITY.md`
4. `ARCHITECTURE.md`
5. `execution/ACTIVE_WORK.md`

## First command

Run this from the repository root:

```bash
make verify
```

If it passes, the local repo is healthy. If it fails, report the exact error.

## Role rule

A junior contributor normally works as Builder.

Builder owns implementation, tests, small fixes, docs updates linked to behavior, and proof.

Builder does not change mission, architecture, interfaces, or product direction without approval.

## Feature work

For feature work, start inside:

`execution/<feature-name>/`

Read:

- `WHY.md`
- `CONTEXT.md`
- `ACCEPTANCE.md`
- `CONSTRAINTS.md`
- `PROOF.md`

If the reason and acceptance criteria are not clear, do not start coding.

## Daily heuristics

- Do not edit a file you cannot explain.
- Do not call work complete without a test.
- Prefer a small clear change over a large unclear refactor.
- Do not duplicate explanations.
- A feature without proof is not complete.
- Leave the repo easier for the next person.

## Blocked format

Use this format:

```text
I am stuck at:
- area

Expected:
- expected result

Actual:
- actual result

Files checked:
- file list

Command run:
- command

Error:
- exact error

My guess:
- evidence-based guess
```

## Completion format

Use this format:

```text
Task:
- assigned task

Files changed:
- file list

What changed:
- short explanation

How I tested:
- commands and results

Proof:
- proof location

Open questions:
- remaining uncertainty

Risk:
- what could still break
```

## Mindset

The goal is not only to write code. The goal is to keep a repository that humans and AI can run without confusion.
