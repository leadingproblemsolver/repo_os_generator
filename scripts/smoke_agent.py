"""
    Smoke test script

    Objective: Run an executable demonstration of the local agent flow.
    Why it exists: Keeps implementation behavior explicit and reviewable inside the repository operating system.
    How to use: Import the public classes or functions from this module; do not bypass the interface contracts.
    Dependencies: Python standard library unless stated in the module imports.
    Owner: Builder.
    Update policy: Change this file only with a matching test, execution block, or decision record when behavior changes.
    Examples: See tests/ and scripts/smoke_agent.py for executable usage.
    Related files: proof/DEMONSTRATION.md
    """

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from support_agent.agent import SupportAgent
from support_agent.models import SupportMessage


def main() -> None:
    agent = SupportAgent()
    response = agent.respond(SupportMessage(customer_id="cust_001", text="Please help with my annual refund and remember this issue for next time"))
    print("answer:", response.answer)
    print("citations:", ",".join(response.citations))
    print("ticket:", response.ticket.ticket_id, response.ticket.status.value)
    print("escalation:", response.escalation.required, response.escalation.reason)
    print("evaluation_average:", response.evaluation.average)


if __name__ == "__main__":
    main()
