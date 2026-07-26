"""
    Agent behavioral tests

    Objective: Prove core agent behavior through deterministic tests.
    Why it exists: Keeps implementation behavior explicit and reviewable inside the repository operating system.
    How to use: Import the public classes or functions from this module; do not bypass the interface contracts.
    Dependencies: Python standard library unless stated in the module imports.
    Owner: Builder.
    Update policy: Change this file only with a matching test, execution block, or decision record when behavior changes.
    Examples: See tests/ and scripts/smoke_agent.py for executable usage.
    Related files: proof/VALIDATION.md
    """

from support_agent.agent import SupportAgent
from support_agent.models import SupportMessage, TicketStatus


def test_agent_returns_grounded_response_and_ticket() -> None:
    agent = SupportAgent()
    response = agent.respond(SupportMessage(customer_id="cust_001", text="I need help with my annual refund after renewal"))
    assert "refund-policy-001" in response.answer
    assert response.citations == ("refund-policy-001",)
    assert response.ticket.ticket_id.startswith("tkt_")
    assert response.evaluation.average >= 0.85


def test_high_risk_message_escalates_to_human() -> None:
    agent = SupportAgent()
    response = agent.respond(SupportMessage(customer_id="cust_001", text="I am angry and considering a chargeback for this billing issue"))
    assert response.escalation.required is True
    assert response.ticket.status is TicketStatus.PENDING_HUMAN
