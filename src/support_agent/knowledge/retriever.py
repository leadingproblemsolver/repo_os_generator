"""
    Knowledge retriever

    Objective: Retrieve approved company knowledge with deterministic lexical scoring.
    Why it exists: Keeps implementation behavior explicit and reviewable inside the repository operating system.
    How to use: Import the public classes or functions from this module; do not bypass the interface contracts.
    Dependencies: Python standard library unless stated in the module imports.
    Owner: Builder.
    Update policy: Change this file only with a matching test, execution block, or decision record when behavior changes.
    Examples: See tests/ and scripts/smoke_agent.py for executable usage.
    Related files: knowledge/COMPANY_KNOWLEDGE_SCHEMA.md
    """

import re
from support_agent.models import KnowledgeArticle, KnowledgeHit

_TOKEN = re.compile(r"[a-zA-Z0-9]+")


def _tokens(text: str) -> set[str]:
    return {match.group(0).lower() for match in _TOKEN.finditer(text)}


class LexicalKnowledgeRetriever:
    def __init__(self) -> None:
        self._articles: dict[str, KnowledgeArticle] = {}

    def add_article(self, article: KnowledgeArticle) -> None:
        if not article.article_id.strip():
            raise ValueError("article_id is required")
        self._articles[article.article_id] = article

    def search(self, query: str, limit: int = 3) -> tuple[KnowledgeHit, ...]:
        query_tokens = _tokens(query)
        if not query_tokens:
            return tuple()
        hits: list[KnowledgeHit] = []
        for article in self._articles.values():
            article_tokens = _tokens(" ".join([article.title, article.body, " ".join(article.tags)]))
            overlap = len(query_tokens & article_tokens)
            if overlap:
                score = overlap / max(len(query_tokens), 1)
                hits.append(KnowledgeHit(article=article, score=round(score, 3)))
        hits.sort(key=lambda hit: hit.score, reverse=True)
        return tuple(hits[:limit])


def default_knowledge() -> LexicalKnowledgeRetriever:
    retriever = LexicalKnowledgeRetriever()
    retriever.add_article(KnowledgeArticle(
        article_id="refund-policy-001",
        title="Refund policy for annual plans",
        body="Annual plan refunds are reviewed by support when the request is made within fourteen days of renewal. Escalate billing disputes or unclear account status to a human specialist.",
        tags=("refund", "billing", "annual", "renewal"),
        source="internal-support-policy",
    ))
    retriever.add_article(KnowledgeArticle(
        article_id="memory-policy-001",
        title="Customer memory use",
        body="Customer memory can store support-relevant preferences or recurring issues. Do not store sensitive facts unless policy, consent, and deletion requirements are satisfied.",
        tags=("memory", "privacy", "customer"),
        source="internal-privacy-policy",
    ))
    return retriever
