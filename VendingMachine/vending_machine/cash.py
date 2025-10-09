from collections import Counter
from typing import Dict
from .enums import Denomination, CANONICAL_DESC
from .errors import CannotMakeChange


class CashDrawer:
    """Manages all cash-in and change operations for the vending machine."""

    def __init__(self, initial: Dict[Denomination, int] | None = None):
        # store counts of each denomination
        self.drawer: Counter = Counter(initial or {})