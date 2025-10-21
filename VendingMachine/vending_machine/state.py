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
        self.machine.current_payment.insert(*amount)  # (denom, count)
        # Stay in HasMoneyState

    def select_product(self, code: str):
        inv = self.machine.inventory
        pay = self.machine.current_payment
        price = inv.get_price(code)
        if not inv.check_stock(code):
            raise OutOfStock(f"{code} is out of stock")

        if pay.inserted < price:
            raise InsufficientFunds(f"Need {price - pay.inserted}¢ more")

        # Proceed to dispense
        self.machine.selected_code = code
        self.machine.transition_to(self.machine.dispense_state)

    def dispense(self):
        raise NotInRightState("Select product before dispensing")

    def cancel(self):
        refund = self.machine.current_payment.refund()
        self.machine.transition_to(self.machine.idle_state)
        return refund


# -------------------------------------------------------------------- #
#                            DISPENSE STATE                            #
# -------------------------------------------------------------------- #

class DispenseState(State):
    def insert_money(self, amount):
        raise NotInRightState("Already dispensing")

    def select_product(self, code: str):
        raise NotInRightState("Product already selected")

    def dispense(self):
        inv = self.machine.inventory
        pay = self.machine.current_payment
        code = self.machine.selected_code
        product = inv.dispense(code)
        price = product.price_cents

        # Compute and transition to change state
        change = pay.dispense_change(price)
        self.machine.last_dispensed = product
        self.machine.last_change = change
        self.machine.transition_to(self.machine.change_state)
        return product

    def cancel(self):
        raise NotInRightState("Cannot cancel during dispensing")


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
