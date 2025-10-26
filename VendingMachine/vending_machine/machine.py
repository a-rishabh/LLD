from typing import Optional
from .state import IdleState, HasMoneyState, DispenseState, ChangeState, State
from .payment import CashPayment
from .cash import CashDrawer
from .inventory import Inventory
from .enums import Denomination


class VendingMachine:
    """Main orchestrator class controlling flow via State Pattern."""

    def __init__(self, drawer: CashDrawer, inventory: Inventory):
        self.drawer = drawer
        self.inventory = inventory

        # Payment strategy (default cash)
        self.current_payment: CashPayment = CashPayment(self.drawer)

    