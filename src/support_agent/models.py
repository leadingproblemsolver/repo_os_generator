"""
    Domain models

    Objective: Define typed objects shared by all bounded contexts.
    Why it exists: Keeps implementation behavior explicit and reviewable inside the repository operating system.
    How to use: Import the public classes or functions from this module; do not bypass the interface contracts.
    Dependencies: Python standard library unless stated in the module imports.
    Owner: Architect.
    Update policy: Change this file only with a matching test, execution block, or decision record when behavior changes.
    Examples: See tests/ and scripts/smoke_agent.py for executable usage.
    Related files: architecture/DATA_MODEL.md
    """

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class TicketPriority(str, Enum):
    LOW = "low"
    NORMAL = "normal"
    HIGH = "high"
    URGENT = "urgent"


class TicketStatus(str, Enum):
    OPEN = "open"
    PENDING_HUMAN = "pending_human"
    RESOLVED = "resolved"


@dataclass(frozen=True)
class CustomerProfile:
    customer_id: str
    name: str
    plan: str
    account_status: str
    attributes: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class MemoryItem:
    customer_id: str
    content: str
    source: str
    created_at: datetime = field(default_factory=utc_now)


@dataclass(frozen=True)
class KnowledgeArticle:
    article_id: str
    title: str
    body: str
    tags: tuple[str, ...]
    source: str
    updated_at: datetime = field(default_factory=utc_now)


@dataclass(frozen=True)
class KnowledgeHit:
    article: KnowledgeArticle
    score: float


@dataclass(frozen=True)
class SupportMessage:
    customer_id: str
    text: str
    channel: str = "web"
    created_at: datetime = field(default_factory=utc_now)


@dataclass(frozen=True)
class Ticket:
    ticket_id: str
    customer_id: str
    subject: str
    summary: str
    priority: TicketPriority
    status: TicketStatus
    created_at: datetime = field(default_factory=utc_now)
    updated_at: datetime = field(default_factory=utc_now)


@dataclass(frozen=True)
class ToolResult:
    tool_name: str
    success: bool
    message: str
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class EscalationDecision:
    required: bool
    reason: str


@dataclass(frozen=True)
class EvaluationScore:
    groundedness: float
    completeness: float
    safety: float
    escalation_correctness: float

    @property
    def average(self) -> float:
        return round((self.groundedness + self.completeness + self.safety + self.escalation_correctness) / 4, 3)


@dataclass(frozen=True)
class SupportResponse:
    customer_id: str
    answer: str
    citations: tuple[str, ...]
    ticket: Ticket
    memory_used: tuple[str, ...]
    tool_results: tuple[ToolResult, ...]
    escalation: EscalationDecision
    evaluation: EvaluationScore
