from __future__ import annotations

import json
from pathlib import Path
import pytest

from repo_os_generator.cli import main
from repo_os_generator.generator import GenerationError, generate_repository
from repo_os_generator.models import ProjectSpec, SpecError
from repo_os_generator.validator import validate_repository


def spec() -> ProjectSpec:
    return ProjectSpec.from_mapping({
        "name": "Test System",
        "slug": "test-system",
        "purpose": "Produce a verified result.",
        "primary_user": "Operator",
        "primary_workflow": "Input to output",
        "runtime": "Python",
        "core_subsystems": ["core"],
        "success_criteria": ["Tests pass"],
        "commands": {"run": "python app.py", "verify": "pytest"},
    })


def market_spec() -> ProjectSpec:
    return ProjectSpec.from_mapping({
        "name": "Market Routed System",
        "slug": "market-routed-system",
        "purpose": "Produce a verified result and expose it to a bounded market route.",
        "primary_user": "Operator",
        "primary_workflow": "Input to verified output",
        "runtime": "Python",
        "market_route": {
            "repo": "leadingproblemsolver/market-routed-system",
            "artifact_id": "mrs-v1",
            "artifact_url": "https://github.com/leadingproblemsolver/market-routed-system",
            "system": "Market Routed System",
            "wedge": "evidence-bounded operational routing",
            "target_roles": ["Head of Operations"],
            "pain_signals": ["fragmented operational evidence"],
            "proof_refs": ["CI receipt"],
            "desired_consequence": "one operator-reviewed workflow",
        },
    })


def test_spec_rejects_missing_fields() -> None:
    with pytest.raises(SpecError):
        ProjectSpec.from_mapping({"name": "x"})


def test_spec_rejects_unsafe_slug() -> None:
    raw = spec().__dict__ | {"slug": "Unsafe Slug"}
    with pytest.raises(SpecError):
        ProjectSpec.from_mapping(raw)


def test_generate_writes_contract_and_manifest(tmp_path: Path) -> None:
    target = tmp_path / "repo"
    result = generate_repository(spec(), target)
    assert result.target == target.resolve()
    assert (target / "repository.json").is_file()
    assert (target / "generation-manifest.json").is_file()
    assert "README.md" in result.files_written
    assert not (target / "market" / "market-artifact-manifest.json").exists()
    assert not (target / ".github" / "workflows" / "market-manifest.yml").exists()


def test_generate_emits_market_manifest_and_ci_only_from_explicit_route_spec(tmp_path: Path) -> None:
    target = tmp_path / "repo"
    result = generate_repository(market_spec(), target)
    market_path = target / "market" / "market-artifact-manifest.json"
    workflow_path = target / ".github" / "workflows" / "market-manifest.yml"
    assert market_path.is_file()
    assert workflow_path.is_file()
    payload = json.loads(market_path.read_text(encoding="utf-8"))
    assert payload["repo"] == "leadingproblemsolver/market-routed-system"
    assert payload["target_roles"] == ["Head of Operations"]
    assert payload["proof_refs"] == ["CI receipt"]
    workflow = workflow_path.read_text(encoding="utf-8")
    assert "Market Manifest Contract" in workflow
    assert "desired_consequence" in workflow
    assert "send" not in workflow.lower()
    assert "market/market-artifact-manifest.json" in result.files_written
    assert ".github/workflows/market-manifest.yml" in result.files_written


def test_market_route_rejects_partial_contract() -> None:
    raw = {
        "name": "Partial",
        "slug": "partial",
        "purpose": "Reject incomplete market state.",
        "primary_user": "Operator",
        "primary_workflow": "Input to output",
        "market_route": {
            "repo": "leadingproblemsolver/partial",
            "artifact_id": "partial-v1",
        },
    }
    with pytest.raises(SpecError, match="market_route missing required fields"):
        ProjectSpec.from_mapping(raw)


def test_generate_refuses_nonempty_target(tmp_path: Path) -> None:
    target = tmp_path / "repo"
    target.mkdir()
    (target / "important.txt").write_text("preserve", encoding="utf-8")
    with pytest.raises(GenerationError):
        generate_repository(spec(), target)
    assert (target / "important.txt").read_text(encoding="utf-8") == "preserve"


def test_force_replaces_reviewed_target(tmp_path: Path) -> None:
    target = tmp_path / "repo"
    target.mkdir()
    (target / "old.txt").write_text("old", encoding="utf-8")
    generate_repository(spec(), target, force=True)
    assert not (target / "old.txt").exists()


def test_generated_repository_validates(tmp_path: Path) -> None:
    target = tmp_path / "repo"
    generate_repository(spec(), target)
    report = validate_repository(target)
    assert report.valid, report.issues


def test_validator_detects_missing_contract(tmp_path: Path) -> None:
    target = tmp_path / "repo"
    generate_repository(spec(), target)
    (target / "repository.json").unlink()
    report = validate_repository(target)
    assert not report.valid
    assert any(issue.path == "repository.json" for issue in report.issues)


def test_cli_end_to_end(tmp_path: Path, capsys) -> None:
    spec_path = tmp_path / "spec.json"
    spec_path.write_text(json.dumps({
        "name": "CLI Test",
        "slug": "cli-test",
        "purpose": "Test the CLI",
        "primary_user": "Tester",
        "primary_workflow": "Run command",
    }), encoding="utf-8")
    target = tmp_path / "out"
    assert main(["init", "--spec", str(spec_path), "--target", str(target)]) == 0
    assert main(["validate", str(target), "--json"]) == 0
    output = capsys.readouterr().out
    assert '"valid": true' in output


def test_generation_is_deterministic(tmp_path: Path) -> None:
    first = tmp_path / "first"
    second = tmp_path / "second"
    one = generate_repository(spec(), first)
    two = generate_repository(spec(), second)
    assert one.manifest_sha256 == two.manifest_sha256
