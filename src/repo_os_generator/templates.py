"""Deterministic text templates for generated repository operating systems."""

from __future__ import annotations

from .models import ProjectSpec

DIRECTORIES = (
    "mission",
    "navigation",
    "architecture",
    "execution",
    "decisions",
    "proof",
    "standards",
    "docs",
    "src",
    "tests",
    "infra",
    "evidence",
)


def metadata(objective: str, owner: str, related: str) -> str:
    return (
        "---\n"
        f"objective: {objective}\n"
        "why_it_exists: Preserve explicit ownership and prevent repository drift.\n"
        "how_to_use: Read before changing this surface and update it with implementation reality.\n"
        "dependencies: repository.json\n"
        f"owner: {owner}\n"
        "update_policy: Update whenever the documented contract changes.\n"
        "examples: Follow the commands and acceptance evidence linked below.\n"
        f"related_files: {related}\n"
        "---\n\n"
    )


def root_readme(spec: ProjectSpec) -> str:
    non_goals = "\n".join(f"- {item}" for item in spec.non_goals) or "- Not yet specified."
    success = "\n".join(f"- [ ] {item}" for item in spec.success_criteria) or "- [ ] Define measurable success criteria."
    run = spec.commands.get("run", "Document the primary run command before release.")
    verify = spec.commands.get("verify", "Document the verification command before release.")
    return metadata(f"Explain and operate {spec.name}.", spec.owner, "repository.json, INDEX.md") + f"""# {spec.name}

{spec.purpose}

## Primary user

{spec.primary_user}

## Primary workflow

{spec.primary_workflow}

## Runtime

`{spec.runtime}`

## Quick start

```bash
{run}
```

## Verification

```bash
{verify}
```

## Non-goals

{non_goals}

## Release criteria

{success}

## Evidence boundary

Generated structure is not implementation proof. Claims become valid only after the linked command, test, deployment, or user evidence is reproducible.
"""


def index(spec: ProjectSpec) -> str:
    return metadata("Provide the deterministic reading and execution order.", spec.owner, "README.md") + """# Repository Index

1. `README.md` — user value and commands.
2. `mission/` — purpose, outcomes, principles, and non-goals.
3. `architecture/` — components, interfaces, state, and failure paths.
4. `execution/` — current bounded work and stop conditions.
5. `decisions/` — consequential choices and alternatives.
6. `proof/` — tests, benchmarks, deployments, and limitations.
7. `evidence/` — hiring-signal and AI–human provenance records.
8. `src/`, `tests/`, `infra/` — executable implementation.
"""


def directory_readme(directory: str, spec: ProjectSpec) -> str:
    responsibilities = {
        "mission": "Own the problem, user outcome, principles, and non-goals.",
        "navigation": "Own deterministic contributor and operator navigation.",
        "architecture": "Own runtime components, interfaces, state, data flow, and failure modes.",
        "execution": "Own bounded active work, constraints, proof, and continuity.",
        "decisions": "Own architecture decision records with alternatives and reversal conditions.",
        "proof": "Own reproducible correctness, performance, deployment, and user evidence.",
        "standards": "Own coding, review, security, reliability, and AI collaboration invariants.",
        "docs": "Own user, operator, and contributor documentation.",
        "src": "Own runtime implementation.",
        "tests": "Own behavioral, boundary, failure, and regression verification.",
        "infra": "Own build, deployment, release, rollback, and observability assets.",
        "evidence": "Own hiring-signal evidence and explicit AI–human provenance.",
    }
    responsibility = responsibilities[directory]
    return metadata(responsibility, spec.owner, "repository.json, INDEX.md") + f"# `{directory}/`\n\n{responsibility}\n"


def mission(spec: ProjectSpec) -> str:
    non_goals = "\n".join(f"- {item}" for item in spec.non_goals) or "- Not yet specified."
    return metadata("Define the bounded mission and exclusions.", spec.owner, "README.md") + f"""# Mission

## Purpose

{spec.purpose}

## User

{spec.primary_user}

## Workflow changed

{spec.primary_workflow}

## Non-goals

{non_goals}
"""


def architecture(spec: ProjectSpec) -> str:
    components = "\n".join(f"- `{item}`" for item in spec.core_subsystems) or "- Define the smallest runtime subsystems after repository reconnaissance."
    return metadata("Describe the current runtime architecture without speculative components.", spec.owner, "mission/MISSION.md") + f"""# Architecture

## Runtime

{spec.runtime}

## Core subsystems

{components}

## Required views

- System context and trust boundaries.
- Primary request or data flow.
- Stateful boundaries and side effects.
- Dependency failures and recovery paths.
- Deployment topology and verification path.

Do not mark a component implemented until code and reproducible verification exist.
"""


def active_work(spec: ProjectSpec) -> str:
    return metadata("Define exactly one active execution block.", spec.owner, "proof/RELEASE_EVIDENCE.md") + f"""# Active Work

```yaml
block:
  project: {spec.slug}
  objective: "Select the highest-value implementable vertical slice."
  allowed_scope: "One behavior or tightly coupled subsystem."
  next_action: "Replace this line with one executable action."
  proof_required:
    - failing or absent starting state
    - implementation diff
    - focused verification
    - regression verification
    - explanation and limitations
  stop_condition: "Proof is reproducible by another engineer."
```
"""


def release_evidence(spec: ProjectSpec) -> str:
    success = "\n".join(f"- [ ] {item}" for item in spec.success_criteria) or "- [ ] Define measurable success criteria."
    return metadata("Index reproducible release evidence and unresolved risks.", spec.owner, "README.md") + f"""# Release Evidence

## Correctness

{success}

## Deployability

- [ ] Clean checkout builds.
- [ ] Versioned artifact is produced.
- [ ] Runtime configuration is explicit.
- [ ] Readiness and primary workflow are verified.
- [ ] Failed release and rollback path are documented.

## Distribution

- [ ] Target user and access channel are explicit.
- [ ] Cold user reaches first value without private help.
- [ ] Activation event and feedback path are defined.

## Unresolved risks

Record unverified external services, credentials, benchmarks, deployments, or user claims here.
"""


def provenance(spec: ProjectSpec) -> str:
    return metadata("Separate human authorship, AI assistance, and verified evidence.", spec.owner, "proof/RELEASE_EVIDENCE.md") + """# AI–Human Provenance

## Human-owned

- Product intent, constraints, acceptance decisions, and consequential approvals.
- Independent reconstruction, debugging, deployment, and defense evidence when completed.

## AI-assisted

- Repository analysis, implementation drafts, tests, documentation, and packaging may be AI-assisted.
- AI-generated code is not represented as unaided human authorship.

## Evidence rule

A claim is publishable only when linked to reproducible code, commands, tests, deployment evidence, or observed user behavior. AI output alone is not proof.
"""
