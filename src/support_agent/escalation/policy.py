"""
    Escalation policy

    Objective: Decide when automation must route to human support.
    Why it exists: Keeps implementation behavior explicit and reviewable inside the repository operating system.
    How to use: Import the public classes or functions from this module; do not bypass the interface contracts.
    Dependencies: Python standard library unless stated in the module imports.
    Owner: Architect.
    Update policy: Change this file only with a matching test, execution block, or decision record when behavior changes.
    Examples: See tests/ and scripts/smoke_agent.py for executable usage.
    Related files: mission/PRINCIPLES.md
    """

from support_agent.models import EscalationDecision, Ticket, TicketPriority


class EscalationPolicy:
    high_risk_terms = ("chargeback", "legal", "lawsuit", "fraud", "angry", "cancel now", "complaint")

    def should_escalate(self, message_text: str, draft_answer: str, ticket: Ticket) -> EscalationDecision:
        lowered = message_text.lower()
        if ticket.priority in {TicketPriority.HIGH, TicketPriority.URGENT}:
            return EscalationDecision(required=True, reason="Ticket priority requires human review")
        if any(term in lowered for term in self.high_risk_terms):
            return EscalationDecision(required=True, reason="Message contains high-risk or high-friction customer language")
        if not draft_answer.strip():
            return EscalationDecision(required=True, reason="No safe automated answer was produced")
        return EscalationDecision(required=False, reason="Automation is within local policy boundary")
