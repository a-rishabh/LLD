from abc import ABC, abstractmethod
from typing import Optional
from .cash import CashDrawer
from .enums import Denomination
from .errors import InsufficientFunds, CannotMakeChange


class PaymentMethod(ABC):
    """Abstract strategy for payments."""

    @abstractmethod
    def pay(self, amount_due: int) -> bool:
        """Returns True if payment successful."""
        pass

    @abstractmethod
    def refund(self) -> None:
        """Refund money to user."""
        pass


# -------------------------------------------------------------------- #
#                            CASH PAYMENT                              #
# -------------------------------------------------------------------- #

class CashPayment(PaymentMethod):
    """Implements payment via coins/bills."""

    def __init__(self, drawer: CashDrawer):
        self.drawer = drawer
        self.inserted: int = 0

    def insert(self, denom: Denomination, count: int = 1) -> None:
        """Simulate inserting cash into machine."""
        pass

    def pay(self, amount_due: int) -> bool:
        pass

    def compute_change(self, amount_due: int) -> Optional[dict]:
        """Compute change (without updating drawer)."""
        pass

    def dispense_change(self, amount_due: int) -> dict:
        """Actually dispense change and update drawer."""
        pass

    def refund(self) -> dict:
        """Refund full amount inserted."""
        pass
