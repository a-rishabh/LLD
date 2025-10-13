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

    def total_amount(self) -> int:
        """Return total value in cents."""
        return sum(denom * cnt for denom, cnt in self.drawer.items())

    def can_make_change(self, amount: int) -> bool:
        """Greedy check — true if we can make change with current coins."""
        try:
            _ = self._greedy_change(amount, dry_run=True)
            return True
        except CannotMakeChange:
            return False
        
    def make_change(self, amount: int) -> Dict[Denomination, int]:
        """Dispense change; updates drawer."""
        change = self._greedy_change(amount)
        for denom, cnt in change.items():
            self.remove(denom, cnt)
        return change

    # ---------------- Helpers ---------------- #

    def _greedy_change(self, amount: int, dry_run: bool = False) -> Dict[Denomination, int]:

        pass

    def __repr__(self) -> str:
        pass