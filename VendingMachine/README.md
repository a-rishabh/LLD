# 🥤 Vending Machine — Low Level Design (LLD)

A FAANG-style **Low Level Design** problem that models a real-world **Vending Machine** using Object-Oriented Design and key design patterns — **State**, **Strategy**, and **Factory**.

---

## 🎯 Goal

Design a vending machine that:
- Accepts cash or (future) card payments.
- Lets users **insert money**, **select products**, and **dispense** items.
- Handles **change**, **refunds**, **insufficient funds**, and **out-of-stock** scenarios.
- Allows **admin actions** like refilling stock and viewing cash totals.

---

## 🧩 System Overview

### 🧱 Core Entities

| Class | Responsibility |
|--------|----------------|
| `VendingMachine` | Orchestrates workflow via states |
| `State` (Idle, HasMoney, Dispense, Change) | Encapsulates behavior for each phase |
| `Inventory` | Tracks products and stock |
| `CashDrawer` | Stores coins/bills and makes change |
| `PaymentMethod` | Abstract payment strategy |
| `CashPayment` | Handles cash insertions and refunds |
| `Product` / `Slot` | Represents items and their quantities |

---

## 🧠 UML Class Diagram

```mermaid
classDiagram
    class VendingMachine {
        +insert_money(amount)
        +select_product(code)
        +dispense()
        +cancel()
        +transition_to(State)
    }

    class State {
        +insert_money(amount)
        +select_product(code)
        +dispense()
        +cancel()
    }

    class IdleState
    class HasMoneyState
    class DispenseState
    class ChangeState

    class PaymentMethod
    class CashPayment
    class CardPayment

    class CashDrawer {
        +add()
        +remove()
        +make_change()
    }

    class Inventory {
        +refill()
        +dispense()
        +available_products()
    }

    class Product {
        +code
        +name
        +price_cents
    }

    VendingMachine --> State
    State <|-- IdleState
    State <|-- HasMoneyState
    State <|-- DispenseState
    State <|-- ChangeState
    VendingMachine --> PaymentMethod
    PaymentMethod <|-- CashPayment
    PaymentMethod <|-- CardPayment
    VendingMachine --> Inventory
    VendingMachine --> CashDrawer
