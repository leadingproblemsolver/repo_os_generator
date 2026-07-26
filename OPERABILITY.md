---
objective: Provide the shortest reliable path from repository clone to local proof.
why_it_exists: Contributors need one operating page that explains commands, expected outputs, and failure handling without a meeting.
how_to_use: Read this before running or changing the system; keep command names aligned with Makefile and scripts.
dependencies: README.md, Makefile, scripts/smoke_agent.py, scripts/validate_repository_os.py, tests/
owner: Builder
update_policy: Update when commands, runtime assumptions, or validation gates change.
examples: A junior contributor can run `make install`, `make verify`, and report the exact output.
related_files: README.md, INDEX.md, proof/VALIDATION.md
---

# Operability

## Local path

Use these commands from the repository root:

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -e ".[test]"
make verify
```

Expected result:

```text
PASS: repository operating system validation passed
2 passed
```

## Commands

| Command | Purpose | Owner |
|---|---|---|
| `make install` | Install the package with test dependencies | Builder |
| `make smoke` | Run one deterministic support-agent flow | Builder |
| `make validate` | Check repository operating-system rules | Architect + Builder |
| `make test` | Run behavioral tests | Builder |
| `make verify` | Run smoke, validation, and tests together | Builder |

## Operating rule

A change is not complete until it has:

1. a clear changed file list
2. a command that proves behavior
3. an updated proof note when behavior changes
4. no hidden setup outside this repository

## Failure handling

When a command fails, report:

```text
Command:
- exact command run

Expected:
- expected result

Actual:
- exact error or failed assertion

Files touched:
- file list

Likely cause:
- one sentence guess based on evidence
```

## Production boundary

The local repo uses deterministic in-memory adapters. Production work must replace adapters behind the existing interfaces without changing domain ownership:

| Area | Local adapter | Production direction |
|---|---|---|
| Memory | `InMemoryMemoryStore` | durable customer-memory store with privacy controls |
| Knowledge | `LexicalKnowledgeRetriever` | vector or hybrid retrieval over approved company knowledge |
| CRM | `InMemoryCRMClient` | CRM API adapter with timeout and error handling |
| Tickets | `InMemoryTicketService` | support desk adapter with idempotent ticket creation |
| Tools | `ToolRegistry` | approved tool gateway with audit records |
| API | optional FastAPI app | hosted API with auth, rate limits, logs, and tracing |

## Done definition

Done means:

- the requested behavior works locally
- `make verify` passes
- changed files match the assigned scope
- proof is written in the relevant `PROOF.md` or `proof/RELEASE_EVIDENCE.md`
- the next person can continue without a call
