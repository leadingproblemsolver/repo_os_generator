"""
    Agent orchestrator

    Objective: Coordinate support response generation across bounded contexts.
    Why it exists: Keeps implementation behavior explicit and reviewable inside the repository operating system.
    How to use: Import the public classes or functions from this module; do not bypass the interface contracts.
    Dependencies: Python standard library unless stated in the module imports.
    Owner: Builder.
    Update policy: Change this file only with a matching test, execution block, or decision record when behavior changes.
    Examples: See tests/ and scripts/smoke_agent.py for executable usage.
    Related files: ARCHITECTURE.md
    """

from support_agent.crm.client import InMemoryCRMClient
from support_agent.escalation.policy import EscalationPolicy
from support_agent.evaluation.evaluator import InteractionEvaluator
from support_agent.knowledge.retriever import LexicalKnowledgeRetriever, default_knowledge
from support_agent.memory.store import InMemoryMemoryStore
from support_agent.models import SupportMessage, SupportResponse, TicketPriority
from support_agent.tickets.service import InMemoryTicketService
from support_agent.tools.registry import ToolRegistry, default_tools


class SupportAgent:
    def __init__(
        self,
        crm: InMemoryCRMClient | None = None,
        memory: InMemoryMemoryStore | None = None,
        knowledge: LexicalKnowledgeRetriever | None = None,
        tickets: InMemoryTicketService | None = None,
        tools: ToolRegistry | None = None,
        escalation: EscalationPolicy | None = None,
        evaluator: InteractionEvaluator | None = None,
    ) -> None:
        self.crm = crm or InMemoryCRMClient()
        self.memory = memory or InMemoryMemoryStore()
        self.knowledge = knowledge or default_knowledge()
        self.tickets = tickets or InMemoryTicketService()
        self.tools = tools or default_tools()
        self.escalation = escalation or EscalationPolicy()
        self.evaluator = evaluator or InteractionEvaluator()

    def respond(self, message: SupportMessage) -> SupportResponse:
        customer = self.crm.get_customer(message.customer_id)
        memories = self.memory.recall(message.customer_id)
        hits = self.knowledge.search(message.text, limit=2)
        priority = TicketPriority.HIGH if any(word in message.text.lower() for word in ("angry", "chargeback", "legal", "fraud")) else TicketPriority.NORMAL
        ticket = self.tickets.open_or_update(
            customer_id=message.customer_id,
            subject=self._subject_from_message(message.text),
            summary=message.text,
            priority=priority,
        )
        tool_results = tuple()
        if "order" in message.text.lower():
            tool_results = (self.tools.execute("lookup_order", {"order_id": "recent"}),)
        answer = self._compose_answer(customer.name, message.text, hits, memories, tool_results)
        escalation_decision = self.escalation.should_escalate(message.text, answer, ticket)
        if escalation_decision.required:
            ticket = self.tickets.mark_pending_human(ticket)
        if "remember" in message.text.lower():
            self.memory.remember(message.customer_id, "Customer asked for continuity on this support issue.", "customer-message")
        evaluation = self.evaluator.score(answer, hits, escalation_decision)
        return SupportResponse(
            customer_id=message.customer_id,
            answer=answer,
            citations=tuple(hit.article.article_id for hit in hits),
            ticket=ticket,
            memory_used=tuple(item.content for item in memories),
            tool_results=tool_results,
            escalation=escalation_decision,
            evaluation=evaluation,
        )

    def _compose_answer(self, customer_name: str, text: str, hits, memories, tool_results) -> str:
        if hits:
            primary = hits[0].article
            citation = primary.article_id
            knowledge_sentence = f"Based on {citation}, {primary.body}"
        else:
            knowledge_sentence = "I do not have enough approved company knowledge to fully resolve this automatically."
        memory_sentence = f"I also considered your previous context: {memories[0].content}" if memories else "No prior customer memory was needed for this response."
        tool_sentence = f" Tool result: {tool_results[0].message}" if tool_results else ""
        return f"Hi {customer_name}. {knowledge_sentence} {memory_sentence} I have opened or updated a support ticket so this issue remains traceable.{tool_sentence}"

    def _subject_from_message(self, text: str) -> str:
        words = text.strip().split()
        subject = " ".join(words[:8]) if words else "Customer support request"
        return subject[:80]
