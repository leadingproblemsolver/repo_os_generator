"""
    Repository OS validator

    Objective: Validate required root files, directory descriptions, and forbidden drift terms.
    Why it exists: Keeps implementation behavior explicit and reviewable inside the repository operating system.
    How to use: Import the public classes or functions from this module; do not bypass the interface contracts.
    Dependencies: Python standard library unless stated in the module imports.
    Owner: Builder.
    Update policy: Change this file only with a matching test, execution block, or decision record when behavior changes.
    Examples: See tests/ and scripts/smoke_agent.py for executable usage.
    Related files: repository.yaml
    """

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_ROOT_FILES = [
    "README.md", "INDEX.md", "CONTRIBUTING.md", "ARCHITECTURE.md", "ROADMAP.md",
    "GLOSSARY.md", "LICENSE", "CODE_OF_CONDUCT.md", "repository.yaml", "braat.yaml",
    "OPERABILITY.md", "Makefile", ".env.example",
]
REQUIRED_DIRS = [
    "mission", "navigation", "architecture", "execution", "projects", "proof", "knowledge",
    "decisions", "standards", "templates", "scripts", "assets", "docs", "src", "tests", "infra",
]
FORBIDDEN_TERMS = ["TO" + "DO", "tb" + "d", "mis" + "c"]
SKIP_DIRS = {".git", ".venv", "__pycache__", ".pytest_cache"}


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def _validate_bilingual_docs() -> None:
    english = ROOT / "docs" / "en"
    hindi = ROOT / "docs" / "hi"
    english_files = {path.relative_to(english) for path in english.rglob("*.md")}
    hindi_files = {path.relative_to(hindi) for path in hindi.rglob("*.md")}
    if english_files != hindi_files:
        fail(f"bilingual docs differ: en={sorted(map(str, english_files))}, hi={sorted(map(str, hindi_files))}")
    for relative in english_files:
        if not (english / relative).read_text(encoding="utf-8").strip():
            fail(f"empty English doc {relative}")
        if not (hindi / relative).read_text(encoding="utf-8").strip():
            fail(f"empty Hindi doc {relative}")


def main() -> None:
    for filename in REQUIRED_ROOT_FILES:
        if not (ROOT / filename).exists():
            fail(f"missing root file {filename}")
    for dirname in REQUIRED_DIRS:
        directory = ROOT / dirname
        if not directory.is_dir():
            fail(f"missing directory {dirname}")
        if not (directory / "README.md").exists():
            fail(f"missing directory description {dirname}/README.md")
    _validate_bilingual_docs()
    for path in ROOT.rglob("*"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.is_file() and path.suffix in {".md", ".py", ".yaml", ".yml", ".txt", ""}:
            text = path.read_text(encoding="utf-8", errors="ignore")
            for term in FORBIDDEN_TERMS:
                if term in text:
                    fail(f"forbidden term {term!r} found in {path.relative_to(ROOT)}")
    print("PASS: repository operating system validation passed")


if __name__ == "__main__":
    main()
