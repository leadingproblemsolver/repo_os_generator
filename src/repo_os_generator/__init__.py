"""Public package interface for the repository operating-system generator."""

from .generator import GenerationResult, generate_repository
from .validator import ValidationIssue, ValidationReport, validate_repository

__all__ = [
    "GenerationResult",
    "ValidationIssue",
    "ValidationReport",
    "generate_repository",
    "validate_repository",
]

__version__ = "1.0.0"
