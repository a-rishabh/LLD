from vending_machine.state import IdleState, HasMoneyState, DispenseState, ChangeState
from vending_machine.cash import CashDrawer
from vending_machine.payment import CashPayment
from vending_machine.models import Product, Slot
from vending_machine.inventory import Inventory
from vending_machine.machine import VendingMachine
from vending_machine.enums import Denomination


def build_machine():
    # minimal setup
    pass


def test_state_transitions():
    pass
