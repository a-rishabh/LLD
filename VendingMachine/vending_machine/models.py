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

    