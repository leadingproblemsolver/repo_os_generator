"""
    Ticket service

    Objective: Open or update support tickets with deterministic identifiers.
    Why it exists: Keeps implementation behavior explicit and reviewable inside the repository operating system.
    How to use: Import the public classes or functions from this module; do not bypass the interface contracts.
    Dependencies: Python standard library unless stated in the module imports.
    Owner: Builder.
    Update policy: Change this file only with a matching test, execution block, or decision record when behavior changes.
    Examples: See tests/ and scripts/smoke_agent.py for executable usage.
    Related files: architecture/INTERFACES.md
    """

from hashlib import sha256
from support_agent.models import Ticket, TicketPriority, TicketStatus, utc_now


class InMemoryTicketService:
    def __init__(self) -> None:
        self._tickets: dict[str, Ticket] = {}

    def open_or_update(self, customer_id: str, subject: str, summary: str, priority: TicketPriority = TicketPriority.NORMAL) -> Ticket:
        seed = f"{customer_id}:{subject.strip().lower()}"
        ticket_id = "tkt_" + sha256(seed.encode("utf-8")).hexdigest()[:10]
        existing = self._tickets.get(ticket_id)
        now = utc_now()
        if existing:
            ticket = Ticket(
                ticket_id=existing.ticket_id,
                customer_id=existing.customer_id,
                subject=existing.subject,
                summary=summary,
                priority=priority,
                status=existing.status,
                created_at=existing.created_at,
                updated_at=now,
            )
        else:
            ticket = Ticket(
                ticket_id=ticket_id,
                customer_id=customer_id,
                subject=subject,
                summary=summary,
                priority=priority,
                status=TicketStatus.OPEN,
                created_at=now,
                updated_at=now,
            )
        self._tickets[ticket_id] = ticket
        return ticket

    def mark_pending_human(self, ticket: Ticket) -> Ticket:
        updated = Ticket(
            ticket_id=ticket.ticket_id,
            customer_id=ticket.customer_id,
            subject=ticket.subject,
            summary=ticket.summary,
            priority=ticket.priority,
            status=TicketStatus.PENDING_HUMAN,
            created_at=ticket.created_at,
            updated_at=utc_now(),
        )
        self._tickets[updated.ticket_id] = updated
        return updated
