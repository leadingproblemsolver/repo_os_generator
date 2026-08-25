"""Typed input contracts for deterministic repository generation."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any
import json


class SpecError(ValueError):
    """Raised when a project specification cannot safely drive generation."""


def _string_tuple(value: Any) -> tuple[str, ...]:
    if value is None:
        return ()
    if not isinstance(value, list) or not all(isinstance(item, str) and item.strip() for item in value):
        raise SpecError("list fields must contain non-empty strings")
    return tuple(item.strip() for item in value)


@dataclass(frozen=True)
class MarketRouteSpec:
    """Explicit market-routing contract consumed by SignalOps/Clay distribution tooling.

    All fields are operator supplied. The generator never infers an ICP, buyer, pain,
    proof state, or desired consequence from repository prose.
    """

    repo: str
    artifact_id: str
    artifact_url: str
    system: str
    wedge: str
    target_roles: tuple[str, ...]
    pain_signals: tuple[str, ...]
    proof_refs: tuple[str, ...]
    desired_consequence: str

    @classmethod
    def from_mapping(cls, raw: dict[str, Any]) -> "MarketRouteSpec":
        required = (
            "repo",
            "artifact_id",
            "artifact_url",
            "system",
            "wedge",
            "target_roles",
            "proof_refs",
            "desired_consequence",
        )
        missing = [key for key in required if not raw.get(key)]
        if missing:
            raise SpecError(f"market_route missing required fields: {', '.join(missing)}")
        target_roles = _string_tuple(raw.get("target_roles"))
        proof_refs = _string_tuple(raw.get("proof_refs"))
        pain_signals = _string_tuple(raw.get("pain_signals"))
        if not target_roles or not proof_refs:
            raise SpecError("market_route target_roles and proof_refs must be non-empty")
        return cls(
            repo=str(raw["repo"]).strip(),
            artifact_id=str(raw["artifact_id"]).strip(),
            artifact_url=str(raw["artifact_url"]).strip(),
            system=str(raw["system"]).strip(),
            wedge=str(raw["wedge"]).strip(),
            target_roles=target_roles,
            pain_signals=pain_signals,
            proof_refs=proof_refs,
            desired_consequence=str(raw["desired_consequence"]).strip(),
        )

    def to_manifest(self) -> dict[str, object]:
        return {
            "repo": self.repo,
            "artifact_id": self.artifact_id,
            "artifact_url": self.artifact_url,
            "system": self.system,
            "wedge": self.wedge,
            "target_roles": list(self.target_roles),
            "pain_signals": list(self.pain_signals),
            "proof_refs": list(self.proof_refs),
            "desired_consequence": self.desired_consequence,
        }


@dataclass(frozen=True)
class ProjectSpec:
    name: str
    slug: str
    purpose: str
    primary_user: str
    primary_workflow: str
    runtime: str = "unspecified"
    owner: str = "Project owner"
    license: str = "UNLICENSED"
    non_goals: tuple[str, ...] = ()
    core_subsystems: tuple[str, ...] = ()
    success_criteria: tuple[str, ...] = ()
    commands: dict[str, str] = field(default_factory=dict)
    market_route: MarketRouteSpec | None = None

    @classmethod
    def from_mapping(cls, raw: dict[str, Any]) -> "ProjectSpec":
        required = ("name", "slug", "purpose", "primary_user", "primary_workflow")
        missing = [key for key in required if not str(raw.get(key, "")).strip()]
        if missing:
            raise SpecError(f"missing required fields: {', '.join(missing)}")
        slug = str(raw["slug"]).strip()
        if not slug.replace("-", "").replace("_", "").isalnum() or slug != slug.lower():
            raise SpecError("slug must contain lowercase letters, numbers, hyphens, or underscores")
        commands = raw.get("commands") or {}
        if not isinstance(commands, dict) or not all(isinstance(k, str) and isinstance(v, str) for k, v in commands.items()):
            raise SpecError("commands must be a string-to-string mapping")
        market_raw = raw.get("market_route")
        if market_raw is None:
            market_route = None
        elif not isinstance(market_raw, dict):
            raise SpecError("market_route must be an object")
        else:
            market_route = MarketRouteSpec.from_mapping(market_raw)
        return cls(
            name=str(raw["name"]).strip(),
            slug=slug,
            purpose=str(raw["purpose"]).strip(),
            primary_user=str(raw["primary_user"]).strip(),
            primary_workflow=str(raw["primary_workflow"]).strip(),
            runtime=str(raw.get("runtime", "unspecified")).strip() or "unspecified",
            owner=str(raw.get("owner", "Project owner")).strip() or "Project owner",
            license=str(raw.get("license", "UNLICENSED")).strip() or "UNLICENSED",
            non_goals=_string_tuple(raw.get("non_goals")),
            core_subsystems=_string_tuple(raw.get("core_subsystems")),
            success_criteria=_string_tuple(raw.get("success_criteria")),
            commands=dict(commands),
            market_route=market_route,
        )

    @classmethod
    def from_json_file(cls, path: Path) -> "ProjectSpec":
        try:
            raw = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            raise SpecError(f"cannot read project specification: {exc}") from exc
        if not isinstance(raw, dict):
            raise SpecError("project specification root must be an object")
        return cls.from_mapping(raw)
