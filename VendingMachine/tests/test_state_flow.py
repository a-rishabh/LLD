from vending_machine.state import IdleState, HasMoneyState, DispenseState, ChangeState
from vending_machine.cash import CashDrawer
from vending_machine.payment import CashPayment
from vending_machine.models import Product, Slot
from vending_machine.inventory import Inventory
from vending_machine.machine import VendingMachine
from vending_machine.enums import Denomination


def build_machine():
    # minimal setup
    drawer = CashDrawer({Denomination.C25: 10})
    inv = Inventory({
        "A1": Slot(Product("A1", "Coke", 75), 3)
    })
    vm = VendingMachine(drawer, inv)
    return vm


def test_state_transitions():
    vm = build_machine()
    assert isinstance(vm.state, IdleState)

    vm.insert_money((Denomination.C25, 4))  # 100¢
    assert isinstance(vm.state, HasMoneyState)

    vm.select_product("A1")
    assert isinstance(vm.state, DispenseState)

    prod = vm.dispense()
    assert prod.name == "Coke"
    assert isinstance(vm.state, ChangeState)

    change = vm.dispense()  # triggers ChangeState.dispense()
    assert isinstance(change, dict)
    assert isinstance(vm.state, IdleState)
