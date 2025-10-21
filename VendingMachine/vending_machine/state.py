from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
from .errors import NotInRightState, InsufficientFunds, OutOfStock

if TYPE_CHECKING:
    from .machine import VendingMachine
    from .payment import CashPayment
    from .inventory import Inventory


# -------------------------------------------------------------------- #
#                            BASE STATE                                #
# -------------------------------------------------------------------- #

class State(ABC):
    """Base abstract class for all states."""

    def __init__(self, machine: "VendingMachine"):
        self.machine = machine

    @abstractmethod
    def insert_money(self, amount): ...
    @abstractmethod
    def select_product(self, code: str): ...
    @abstractmethod
    def dispense(self): ...
    @abstractmethod
    def cancel(self): ...


# -------------------------------------------------------------------- #
#                            IDLE STATE                                #
# -------------------------------------------------------------------- #



# -------------------------------------------------------------------- #
#                            HAS MONEY STATE                           #
# -------------------------------------------------------------------- #



# -------------------------------------------------------------------- #
#                            DISPENSE STATE                            #
# -------------------------------------------------------------------- #




# -------------------------------------------------------------------- #
#                            CHANGE STATE                              #
# -------------------------------------------------------------------- #


