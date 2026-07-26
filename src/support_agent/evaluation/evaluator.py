"""
    Evaluator

    Objective: Score support interactions for continuous improvement.
    Why it exists: Keeps implementation behavior explicit and reviewable inside the repository operating system.
    How to use: Import the public classes or functions from this module; do not bypass the interface contracts.
    Dependencies: Python standard library unless stated in the module imports.
    Owner: Architect.
    Update policy: Change this file only with a matching test, execution block, or decision record when behavior changes.
    Examples: See tests/ and scripts/smoke_agent.py for executable usage.
    Related files: proof/METRICS.md
    """

from support_agent.models import EscalationDecision, EvaluationScore, KnowledgeHit


class InteractionEvaluator:
    def score(self, answer: str, knowledge_hits: tuple[KnowledgeHit, ...], escalation: EscalationDecision) -> EvaluationScore:
        groundedness = 1.0 if knowledge_hits and any(hit.article.article_id in answer for hit in knowledge_hits) else 0.4
        completeness = 1.0 if len(answer.split()) >= 24 else 0.6
        safety = 1.0 if "guarantee" not in answer.lower() else 0.5
        escalation_correctness = 1.0 if escalation.reason else 0.6
        return EvaluationScore(
            groundedness=groundedness,
            completeness=completeness,
            safety=safety,
            escalation_correctness=escalation_correctness,
        )
