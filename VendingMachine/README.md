# Vending Machine — Low Level Design (LLD)

Design and implement a **Vending Machine** using SOLID OOP and the **State pattern**. This is a staple LLD interview problem that tests modeling, transitions, error handling, and payments.

---

## Problem Statement

Build a vending machine that:

* Accepts coins/bills or a card (pluggable payments).
* Lets a user **select a product** and **dispense** it.
* Handles **insufficient funds**, **out-of-stock**, **cancel/refund**, and **change**.
* Supports **admin operations**: refill inventory, collect cash, load coins.

**Constraints/Assumptions**

* Products have `code`, `name`, `price`, and `quantity`.
* Accepted denominations (configurable): `1, 5, 10, 25, 100` (cents).
* Return **change with the least coins** (greedy works with canonical US denominations).
* Timeouts / inactivity not modeled (keep MVP focused).

---

## Why This Problem (Interview Signals)

* **Stateful workflows** → State pattern & transitions.
* **Domain modeling** → Product, Inventory, Cash drawer, Payment.
* **Robustness** → Errors, refunds, race-free updates.
* **Extensibility** → Add new payments, discounts, or multi-buy without rewriting core.

---

## Core Entities & Responsibilities

| Entity           | Responsibility                                                                |
| ---------------- | ----------------------------------------------------------------------------- |
| `Product`        | Code, name, price (cents)                                                     |
| `Inventory`      | Tracks counts per product; refill/decrement                                   |
| `CashDrawer`     | Holds coins/bills; add/remove; make change                                    |
| `PaymentMethod`  | Interface for `cash`, `card` etc.                                             |
| `VendingMachine` | Orchestrator; holds current `State` and collaborators                         |
| `State`          | Abstract state with transitions: `Idle → HasMoney → Dispense → Change → Idle` |

---

## State Machine (MVP)

```
Idle
 ├─ insert_money(amount) → HasMoney
 └─ select_product(code) → error (need money)

HasMoney
 ├─ select_product(code) → (enough $ & in stock) ? Dispense : error/insufficient/change remain in HasMoney
 ├─ insert_money(amount) → HasMoney (accumulate)
 └─ cancel() → Change → Idle

Dispense
 ├─ dispense() → Change

Change
 ├─ return_change() → Idle
```

---

## Design Patterns

* **State**: encapsulates behavior per machine state (Idle/HasMoney/Dispense/Change).
* **Strategy (Payment)**: case-by-case payment methods (`CashPayment`, `CardPayment`).
* **Factory (optional)**: product creation from config/JSON.

---

## Key Scenarios to Support

* Pay exact, select item, dispense, no change.
* Pay extra, dispense, **return change**.
* Select with **insufficient funds** ⇒ helpful error.
* **Out-of-stock** ⇒ allow reselection or refund.
* **Cancel** anytime in `HasMoney` ⇒ refund all.
* **Admin**: refill items, load coins, empty cash.

---

## Project Structure (planned)

```
vending_machine/
  __init__.py
  enums.py          # Denominations, StateType
  errors.py         # Domain exceptions
  models.py         # Product, LineItem
  cash.py           # CashDrawer + change-making
  inventory.py      # Inventory
  payment.py        # PaymentMethod, CashPayment, (Card stub)
  state.py          # Abstract State + concrete Idle/HasMoney/Dispense/Change
  machine.py        # VendingMachine orchestrator
  cli.py            # Demo

tests/
  test_cash.py
  test_inventory.py
  test_state_flow.py
  test_machine.py
```

---

## Minimal Public API (MVP)

```python
vm.insert_money(25)          # cents
vm.select_product("A1")
vm.dispense()                # triggers state transition
vm.cancel()                  # in HasMoney → refund
vm.admin_refill("A1", 10)
```

---

## Interview Tips

* Open with the **state diagram**; show transitions.
* Keep **money** and **inventory** separate from the state logic (SRP).
* Emphasize **Strategy for payments** to support cards later without changing state code.
* Discuss edge cases early: out-of-stock, insufficient change, cancel/refund.
