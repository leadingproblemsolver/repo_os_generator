"""Safe, deterministic repository-OS generation."""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path
import json
import os
import tempfile

from .models import ProjectSpec
from . import templates


class GenerationError(RuntimeError):
    """Raised when generation cannot proceed without risking existing work."""


@dataclass(frozen=True)
class GenerationResult:
    target: Path
    files_written: tuple[str, ...]
    manifest_sha256: str


def generate_repository(spec: ProjectSpec, target: Path, *, force: bool = False) -> GenerationResult:
    target = target.resolve()
    if target.exists() and any(target.iterdir()) and not force:
        raise GenerationError(f"target is not empty: {target}; pass force=True only after review")
    target.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=f".{spec.slug}-", dir=target.parent) as tmp:
        stage = Path(tmp) / spec.slug
        stage.mkdir()
        files = _render(spec)
        for relative, content in files.items():
            path = stage / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content.rstrip() + "\n", encoding="utf-8")
        manifest = _manifest(stage)
        (stage / "generation-manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        if target.exists():
            for child in target.iterdir():
                if child.is_dir():
                    import shutil
                    shutil.rmtree(child)
                else:
                    child.unlink()
        else:
            target.mkdir()
        for child in stage.iterdir():
            os.replace(child, target / child.name)
    final_manifest = json.loads((target / "generation-manifest.json").read_text(encoding="utf-8"))
    digest = sha256(json.dumps(final_manifest, sort_keys=True).encode("utf-8")).hexdigest()
    return GenerationResult(target=target, files_written=tuple(sorted(final_manifest["files"])), manifest_sha256=digest)


def _render(spec: ProjectSpec) -> dict[str, str]:
    files: dict[str, str] = {
        "README.md": templates.root_readme(spec),
        "INDEX.md": templates.index(spec),
        "repository.json": json.dumps({
            "schema_version": "1.0.0",
            "project": {
                "name": spec.name,
                "slug": spec.slug,
                "purpose": spec.purpose,
                "primary_user": spec.primary_user,
                "primary_workflow": spec.primary_workflow,
                "runtime": spec.runtime,
                "owner": spec.owner,
                "license": spec.license,
                "non_goals": list(spec.non_goals),
                "core_subsystems": list(spec.core_subsystems),
                "success_criteria": list(spec.success_criteria),
                "commands": spec.commands,
            },
            "truth_statuses": ["implemented", "partially_implemented", "documented", "planned", "deferred"],
        }, indent=2, sort_keys=True),
        "mission/MISSION.md": templates.mission(spec),
        "architecture/ARCHITECTURE.md": templates.architecture(spec),
        "execution/ACTIVE_WORK.md": templates.active_work(spec),
        "proof/RELEASE_EVIDENCE.md": templates.release_evidence(spec),
        "evidence/AI_HUMAN_PROVENANCE.md": templates.provenance(spec),
        ".gitignore": ".venv/\n__pycache__/\n.pytest_cache/\n.env\n*.log\ndist/\nbuild/\n",
        ".env.example": "# Declare required runtime variables here without secrets.\n",
    }
    if spec.market_route is not None:
        files["market/market-artifact-manifest.json"] = json.dumps(
            spec.market_route.to_manifest(), indent=2, sort_keys=True
        )
        files["market/README.md"] = (
            "# Market routing\n\n"
            "`market-artifact-manifest.json` is an explicit producer-side contract for the "
            "SignalOps + Clay market distribution router. It contains operator-supplied market "
            "facts only; generating this repository does not authorize outreach, CRM mutation, "
            "or claim adoption/revenue.\n"
        )
    for directory in templates.DIRECTORIES:
        files.setdefault(f"{directory}/README.md", templates.directory_readme(directory, spec))
    return files


def _manifest(root: Path) -> dict[str, object]:
    files: dict[str, str] = {}
    for path in sorted(item for item in root.rglob("*") if item.is_file()):
        relative = path.relative_to(root).as_posix()
        files[relative] = sha256(path.read_bytes()).hexdigest()
    return {"schema_version": "1.0.0", "files": files}
