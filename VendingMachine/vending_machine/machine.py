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

        # State instances (singletons per machine)
        self.idle_state = IdleState(self)
        self.has_money_state = HasMoneyState(self)
        self.dispense_state = DispenseState(self)
        self.change_state = ChangeState(self)

        # Initialize state
        self.state: State = self.idle_state

        # For tracking transaction data
        self.selected_code: Optional[str] = None
        self.last_dispensed = None
        self.last_change: Optional[dict] = None

    # ---------------- Core Actions ---------------- #

    def insert_money(self, amount: tuple[Denomination, int]):
        """Delegate to current state's insert_money logic."""
        self.state.insert_money(amount)

    def select_product(self, code: str):
        self.state.select_product(code)

    def dispense(self):
        """Trigger dispense flow depending on state."""
        return self.state.dispense()

    def cancel(self):
        """Cancel current transaction (if applicable)."""
        return self.state.cancel()

    