"""Validation for generated or adopted repository operating systems."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import json

from .templates import DIRECTORIES


@dataclass(frozen=True)
class ValidationIssue:
    code: str
    path: str
    message: str
    severity: str = "error"


@dataclass(frozen=True)
class ValidationReport:
    root: Path
    issues: tuple[ValidationIssue, ...]

    @property
    def valid(self) -> bool:
        return not any(issue.severity == "error" for issue in self.issues)


def validate_repository(root: Path) -> ValidationReport:
    root = root.resolve()
    issues: list[ValidationIssue] = []
    for filename in ("README.md", "INDEX.md", "repository.json", "generation-manifest.json"):
        if not (root / filename).is_file():
            issues.append(ValidationIssue("missing_file", filename, "required root file is absent"))
    for directory in DIRECTORIES:
        if not (root / directory).is_dir():
            issues.append(ValidationIssue("missing_directory", directory, "required ownership surface is absent"))
        elif not (root / directory / "README.md").is_file():
            issues.append(ValidationIssue("missing_boundary", f"{directory}/README.md", "directory responsibility is undocumented"))
    repository_path = root / "repository.json"
    if repository_path.is_file():
        try:
            repository = json.loads(repository_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            issues.append(ValidationIssue("invalid_json", "repository.json", str(exc)))
        else:
            project = repository.get("project") if isinstance(repository, dict) else None
            for field in ("name", "slug", "purpose", "primary_user", "primary_workflow", "owner"):
                if not isinstance(project, dict) or not str(project.get(field, "")).strip():
                    issues.append(ValidationIssue("missing_contract_field", f"repository.json:project.{field}", "required project contract field is empty"))
    for path in root.rglob("*.md"):
        text = path.read_text(encoding="utf-8", errors="replace")
        if path.name != "README.md" or path.parent == root:
            continue
        if not text.lstrip().startswith("---"):
            issues.append(ValidationIssue("missing_metadata", path.relative_to(root).as_posix(), "boundary README lacks metadata header", "warning"))
    return ValidationReport(root=root, issues=tuple(issues))
