"""
    CRM client

    Objective: Provide customer profile lookup behind an adapter boundary.
    Why it exists: Keeps implementation behavior explicit and reviewable inside the repository operating system.
    How to use: Import the public classes or functions from this module; do not bypass the interface contracts.
    Dependencies: Python standard library unless stated in the module imports.
    Owner: Builder.
    Update policy: Change this file only with a matching test, execution block, or decision record when behavior changes.
    Examples: See tests/ and scripts/smoke_agent.py for executable usage.
    Related files: architecture/INTERFACES.md
    """

from support_agent.models import CustomerProfile


class InMemoryCRMClient:
    def __init__(self, profiles: dict[str, CustomerProfile] | None = None) -> None:
        self._profiles = profiles or {
            "cust_001": CustomerProfile(
                customer_id="cust_001",
                name="Avery Stone",
                plan="annual_pro",
                account_status="active",
                attributes={"region": "global", "renewal_days_ago": 7},
            )
        }

    def get_customer(self, customer_id: str) -> CustomerProfile:
        if customer_id not in self._profiles:
            return CustomerProfile(customer_id=customer_id, name="Customer", plan="unknown", account_status="unknown")
        return self._profiles[customer_id]
