from dataclasses import dataclass

@dataclass(frozen=True)
class Product:
    code: str
    name: str
    price_cents: int

@dataclass
class Slot:
    product: Product
    quantity: int = 0

    def has_stock(self) -> bool:
        return self.quantity > 0

    def dispense_one(self) -> None:
        if not self.has_stock():
            from .errors import OutOfStock
            raise OutOfStock(f"{self.product.code} is out of stock")
        self.quantity -= 1