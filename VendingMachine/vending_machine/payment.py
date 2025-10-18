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
        self.drawer.add(denom, count)
        self.inserted += denom * count

    def pay(self, amount_due: int) -> bool:
        if self.inserted < amount_due:
            raise InsufficientFunds(f"Need {amount_due - self.inserted}¢ more")
        # Payment succeeds, any extra change handled externally
        return True

    def compute_change(self, amount_due: int) -> Optional[dict]:
        """Compute change (without updating drawer)."""
        if self.inserted < amount_due:
            raise InsufficientFunds(f"Need {amount_due - self.inserted}¢ more")
        change = self.inserted - amount_due
        if change == 0:
            return {}
        if not self.drawer.can_make_change(change):
            raise CannotMakeChange(f"Cannot return {change}¢ in change")
        return self.drawer._greedy_change(change, dry_run=True)

    def dispense_change(self, amount_due: int) -> dict:
        """Actually dispense change and update drawer."""
        change_amount = self.inserted - amount_due
        if change_amount <= 0:
            return {}
        return self.drawer.make_change(change_amount)

    def refund(self) -> dict:
        """Refund full amount inserted."""
        if self.inserted == 0:
            return {}
        refund_amount = self.inserted
        self.inserted = 0
        # No drawer removal—assume manual refund
        return {"REFUND": refund_amount}


# -------------------------------------------------------------------- #
#                            CARD PAYMENT (Stub)                       #
# -------------------------------------------------------------------- #

class CardPayment(PaymentMethod):
    """Stub for card-based payment system."""

    def __init__(self):
        self.charged = False

    def pay(self, amount_due: int) -> bool:
        # Simulate successful card authorization
        self.charged = True
        return True

    def refund(self) -> None:
        if self.charged:
            self.charged = False