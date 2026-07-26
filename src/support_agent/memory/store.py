"""
    Memory store

    Objective: Provide customer memory recall and write behavior.
    Why it exists: Keeps implementation behavior explicit and reviewable inside the repository operating system.
    How to use: Import the public classes or functions from this module; do not bypass the interface contracts.
    Dependencies: Python standard library unless stated in the module imports.
    Owner: Builder.
    Update policy: Change this file only with a matching test, execution block, or decision record when behavior changes.
    Examples: See tests/ and scripts/smoke_agent.py for executable usage.
    Related files: architecture/INTERFACES.md
    """

from collections import defaultdict
from support_agent.models import MemoryItem


class InMemoryMemoryStore:
    def __init__(self) -> None:
        self._items: dict[str, list[MemoryItem]] = defaultdict(list)

    def remember(self, customer_id: str, content: str, source: str) -> MemoryItem:
        item = MemoryItem(customer_id=customer_id, content=content.strip(), source=source)
        self._items[customer_id].insert(0, item)
        return item

    def recall(self, customer_id: str) -> tuple[MemoryItem, ...]:
        return tuple(self._items.get(customer_id, ()))
