from typing import Dict
from .models import Slot, Product
from .errors import InvalidSelection, OutOfStock


class Inventory:
    """Manages product slots and stock counts."""

    def __init__(self, slots: Dict[str, Slot] | None = None):
        # Keyed by product code like "A1", "B2"
        self.slots: Dict[str, Slot] = slots or {}

    # ---------------- Admin Ops ---------------- #

    def add_slot(self, product: Product, quantity: int) -> None:
        """Add a new slot or refill an existing one."""
        code = product.code
        if code in self.slots:
            self.slots[code].quantity += quantity
        else:
            self.slots[code] = Slot(product, quantity)

    def refill(self, code: str, quantity: int) -> None:
        if code not in self.slots:
            raise InvalidSelection(f"Slot {code} not found")
        self.slots[code].quantity += quantity

    # ---------------- User Ops ---------------- #

    def get_product(self, code: str) -> Product:
        if code not in self.slots:
            raise InvalidSelection(f"Invalid code {code}")
        return self.slots[code].product

    def get_price(self, code: str) -> int:
        if code not in self.slots:
            raise InvalidSelection(f"Invalid code {code}")
        return self.slots[code].product.price_cents

    def check_stock(self, code: str) -> bool:
        if code not in self.slots:
            raise InvalidSelection(f"Invalid code {code}")
        return self.slots[code].has_stock()

    def dispense(self, code: str) -> Product:
        """Dispense one unit of the given code."""
        if code not in self.slots:
            raise InvalidSelection(f"Invalid code {code}")
        slot = self.slots[code]
        if not slot.has_stock():
            raise OutOfStock(f"Product {code} is out of stock")
        slot.dispense_one()
        return slot.product

    # ---------------- Diagnostics ---------------- #

    def available_products(self) -> Dict[str, int]:
        """Return {code: quantity} for available items."""
        return {c: s.quantity for c, s in self.slots.items()}

    def __repr__(self) -> str:
        return f"Inventory({self.available_products()})"
