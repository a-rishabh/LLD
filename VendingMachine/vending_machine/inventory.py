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
        pass

    def refill(self, code: str, quantity: int) -> None:
        pass

    # ---------------- User Ops ---------------- #

    def get_product(self, code: str) -> Product:
        pass

    def get_price(self, code: str) -> int:
        pass

    def check_stock(self, code: str) -> bool:
        pass
    def dispense(self, code: str) -> Product:
        """Dispense one unit of the given code."""
        pass

    # ---------------- Diagnostics ---------------- #

    def available_products(self) -> Dict[str, int]:
        """Return {code: quantity} for available items."""
        pass

    def __repr__(self) -> str:
        pass
