"""
    Tool registry

    Objective: Control support tool execution through auditable named tools.
    Why it exists: Keeps implementation behavior explicit and reviewable inside the repository operating system.
    How to use: Import the public classes or functions from this module; do not bypass the interface contracts.
    Dependencies: Python standard library unless stated in the module imports.
    Owner: Builder.
    Update policy: Change this file only with a matching test, execution block, or decision record when behavior changes.
    Examples: See tests/ and scripts/smoke_agent.py for executable usage.
    Related files: architecture/INTERFACES.md
    """

from collections.abc import Callable
from typing import Any
from support_agent.models import ToolResult

ToolHandler = Callable[[dict[str, Any]], ToolResult]


class ToolRegistry:
    def __init__(self) -> None:
        self._tools: dict[str, ToolHandler] = {}

    def register(self, name: str, handler: ToolHandler) -> None:
        if not name.strip():
            raise ValueError("tool name is required")
        self._tools[name] = handler

    def execute(self, tool_name: str, arguments: dict[str, Any]) -> ToolResult:
        handler = self._tools.get(tool_name)
        if handler is None:
            return ToolResult(tool_name=tool_name, success=False, message="Tool is not registered", metadata={"available": sorted(self._tools)})
        return handler(arguments)


def default_tools() -> ToolRegistry:
    registry = ToolRegistry()

    def lookup_order(arguments: dict[str, Any]) -> ToolResult:
        order_id = str(arguments.get("order_id", "unknown"))
        return ToolResult(tool_name="lookup_order", success=True, message=f"Order {order_id} is active in the local support ledger.", metadata={"order_id": order_id})

    registry.register("lookup_order", lookup_order)
    return registry
