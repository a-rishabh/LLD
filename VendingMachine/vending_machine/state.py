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

class IdleState(State):
    def insert_money(self, amount):
        self.machine.current_payment.insert(*amount)
        self.machine.transition_to(self.machine.has_money_state)

    def select_product(self, code: str):
        raise NotInRightState("Insert money first")

    def dispense(self):
        raise NotInRightState("No product selected")

    def cancel(self):
        raise NotInRightState("Nothing to cancel in IDLE")


# -------------------------------------------------------------------- #
#                            HAS MONEY STATE                           #
# -------------------------------------------------------------------- #

class HasMoneyState(State):
    def insert_money(self, amount):
        pass

    def select_product(self, code: str):
        pass

    def dispense(self):
        pass

    def cancel(self):
        pass


# -------------------------------------------------------------------- #
#                            DISPENSE STATE                            #
# -------------------------------------------------------------------- #

class DispenseState(State):
    def insert_money(self, amount):
        pass

    def select_product(self, code: str):
        pass

    def dispense(self):
        pass

    def cancel(self):
        pass


# -------------------------------------------------------------------- #
#                            CHANGE STATE                              #
# -------------------------------------------------------------------- #

class ChangeState(State):
    def insert_money(self, amount):
        pass

    def select_product(self, code: str):
        pass

    def dispense(self):
        """Dispense change and return to idle."""
        pass

    def cancel(self):
        pass
