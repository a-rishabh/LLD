from collections import Counter
from typing import Dict
from .enums import Denomination, CANONICAL_DESC
from .errors import CannotMakeChange


class CashDrawer:
    """Manages all cash-in and change operations for the vending machine."""

    def __init__(self, initial: Dict[Denomination, int] | None = None):
        # store counts of each denomination
        self.drawer: Counter = Counter(initial or {})

    # ---------------- Core Ops ---------------- #

    def add(self, denom: Denomination, count: int = 1) -> None:
        """Add coins/bills into drawer."""
        self.drawer[denom] += count

    def remove(self, denom: Denomination, count: int = 1) -> None:
        """Remove coins/bills; raises if insufficient."""
        if self.drawer[denom] < count:
            raise CannotMakeChange(f"Not enough {denom.name} to remove")
        self.drawer[denom] -= count