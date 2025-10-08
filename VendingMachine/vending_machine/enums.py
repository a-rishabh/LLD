from enum import Enum

class Denomination(int, Enum):
    C1 = 1
    C5 = 5
    C10 = 10
    C25 = 25
    C100 = 100  # dollar

CANONICAL_DESC = [Denomination.C100, Denomination.C25, Denomination.C10, Denomination.C5, Denomination.C1]

class StateType(str, Enum):
    IDLE = "IDLE"
    HAS_MONEY = "HAS_MONEY"
    DISPENSE = "DISPENSE"
    CHANGE = "CHANGE"
