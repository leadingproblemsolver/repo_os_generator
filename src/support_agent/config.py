"""
    Runtime configuration

    Objective: Load explicit runtime settings from environment variables.
    Why it exists: Keeps implementation behavior explicit and reviewable inside the repository operating system.
    How to use: Import the public classes or functions from this module; do not bypass the interface contracts.
    Dependencies: Python standard library unless stated in the module imports.
    Owner: Builder.
    Update policy: Change this file only with a matching test, execution block, or decision record when behavior changes.
    Examples: See tests/ and scripts/smoke_agent.py for executable usage.
    Related files: .env.example, infra/
    """

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    environment: str
    log_level: str
    support_default_priority: str


def load_settings() -> Settings:
    return Settings(
        environment=os.getenv("SUPPORT_AGENT_ENV", "local"),
        log_level=os.getenv("SUPPORT_AGENT_LOG_LEVEL", "INFO"),
        support_default_priority=os.getenv("SUPPORT_DEFAULT_PRIORITY", "normal"),
    )
