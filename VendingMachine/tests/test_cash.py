import pytest
from vending_machine.cash import CashDrawer
from vending_machine.enums import Denomination
from vending_machine.errors import CannotMakeChange

def test_total_and_add_remove():
    cd = CashDrawer({Denomination.C25: 4, Denomination.C10: 2})
    assert cd.total_amount() == 4*25 + 2*10
    cd.add(Denomination.C1, 5)
    assert cd.total_amount() == 4*25 + 2*10 + 5*1
    cd.remove(Denomination.C25, 2)
    assert cd.drawer[Denomination.C25] == 2

def test_make_change_exact():
    pass

def test_cannot_make_change():
    cd = CashDrawer({Denomination.C25: 1})
    with pytest.raises(CannotMakeChange):
        cd.make_change(30)
