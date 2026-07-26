"""
    HTTP API boundary

    Objective: Expose the support agent through a FastAPI application when FastAPI is installed.
    Why it exists: Keeps implementation behavior explicit and reviewable inside the repository operating system.
    How to use: Import the public classes or functions from this module; do not bypass the interface contracts.
    Dependencies: Python standard library unless stated in the module imports.
    Owner: Builder.
    Update policy: Change this file only with a matching test, execution block, or decision record when behavior changes.
    Examples: See tests/ and scripts/smoke_agent.py for executable usage.
    Related files: infra/Dockerfile
    """

from support_agent.agent import SupportAgent
from support_agent.models import SupportMessage

agent = SupportAgent()

try:
    from fastapi import FastAPI
except ImportError:  # pragma: no cover - optional runtime dependency path
    FastAPI = None


def create_app():
    if FastAPI is None:
        raise RuntimeError("FastAPI is required for HTTP serving. Install the api extra or use scripts/smoke_agent.py for local execution.")
    app = FastAPI(title="repo-os-generator — deterministic support-agent sample (no AI/LLM component)")

    @app.post("/support/respond")
    def respond(payload: dict[str, str]):
        message = SupportMessage(customer_id=payload["customer_id"], text=payload["text"], channel=payload.get("channel", "api"))
        response = agent.respond(message)
        return {
            "customer_id": response.customer_id,
            "answer": response.answer,
            "citations": response.citations,
            "ticket_id": response.ticket.ticket_id,
            "ticket_status": response.ticket.status.value,
            "escalation_required": response.escalation.required,
            "escalation_reason": response.escalation.reason,
            "evaluation_average": response.evaluation.average,
        }

    return app


if FastAPI is not None:
    app = create_app()
