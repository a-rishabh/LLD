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