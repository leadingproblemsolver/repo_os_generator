"""Command-line interface for repository generation and validation."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

from .generator import GenerationError, generate_repository
from .models import ProjectSpec, SpecError
from .validator import validate_repository


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(prog="repo-os", description="Generate and validate evidence-aware repository operating systems.")
    sub = root.add_subparsers(dest="command", required=True)
    init = sub.add_parser("init", help="Generate a repository OS from a JSON project specification.")
    init.add_argument("--spec", type=Path, required=True)
    init.add_argument("--target", type=Path, required=True)
    init.add_argument("--force", action="store_true")
    validate = sub.add_parser("validate", help="Validate a generated or adopted repository OS.")
    validate.add_argument("root", type=Path)
    validate.add_argument("--json", action="store_true", dest="as_json")
    example = sub.add_parser("example-spec", help="Print an executable project specification example.")
    example.add_argument("--output", type=Path)
    return root


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    try:
        if args.command == "init":
            result = generate_repository(ProjectSpec.from_json_file(args.spec), args.target, force=args.force)
            print(json.dumps({"target": str(result.target), "files_written": len(result.files_written), "manifest_sha256": result.manifest_sha256}, indent=2))
            return 0
        if args.command == "validate":
            report = validate_repository(args.root)
            payload = {"root": str(report.root), "valid": report.valid, "issues": [issue.__dict__ for issue in report.issues]}
            if args.as_json:
                print(json.dumps(payload, indent=2))
            else:
                print("PASS" if report.valid else "FAIL", report.root)
                for issue in report.issues:
                    print(f"{issue.severity.upper()} {issue.code} {issue.path}: {issue.message}")
            return 0 if report.valid else 1
        if args.command == "example-spec":
            content = json.dumps({
                "name": "Example Service",
                "slug": "example-service",
                "purpose": "Provide one bounded, reproducible user outcome.",
                "primary_user": "A precisely defined operator",
                "primary_workflow": "Input → validated transformation → observable output",
                "runtime": "Python 3.12",
                "owner": "Project owner",
                "license": "MIT",
                "non_goals": ["Unbounded platform scope"],
                "core_subsystems": ["api", "domain", "persistence"],
                "success_criteria": ["Clean checkout passes verification"],
                "commands": {"run": "make run", "verify": "make verify"},
            }, indent=2) + "\n"
            if args.output:
                args.output.write_text(content, encoding="utf-8")
            else:
                print(content, end="")
            return 0
    except (SpecError, GenerationError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
