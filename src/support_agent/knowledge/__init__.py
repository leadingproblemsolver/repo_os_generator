"""
    Knowledge package exports

    Objective: Expose knowledge retrieval implementations.
    Why it exists: Keeps implementation behavior explicit and reviewable inside the repository operating system.
    How to use: Import the public classes or functions from this module; do not bypass the interface contracts.
    Dependencies: Python standard library unless stated in the module imports.
    Owner: Builder.
    Update policy: Change this file only with a matching test, execution block, or decision record when behavior changes.
    Examples: See tests/ and scripts/smoke_agent.py for executable usage.
    Related files: src/support_agent/knowledge/retriever.py
    """
from support_agent.knowledge.retriever import LexicalKnowledgeRetriever, default_knowledge
