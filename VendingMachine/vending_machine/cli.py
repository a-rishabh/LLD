import sys
from vending_machine.machine import VendingMachine
from vending_machine.cash import CashDrawer
from vending_machine.inventory import Inventory
from vending_machine.models import Product, Slot
from vending_machine.enums import Denomination

def build_demo_machine() -> VendingMachine:
    drawer = CashDrawer({
        Denomination.C25: 20,
        Denomination.C10: 20,
        Denomination.C5: 20,
        Denomination.C1: 20,
    })
    inv = Inventory({
        "A1": Slot(Product("A1", "Coke", 75), 5),
        "A2": Slot(Product("A2", "Pepsi", 85), 5),
        "B1": Slot(Product("B1", "Chips", 50), 3),
        "C1": Slot(Product("C1", "Candy", 65), 4),
    })
    return VendingMachine(drawer, inv)


def menu():
    print("\n=== 🥤 Vending Machine Demo ===")
    print("Commands:")
    print("  1. insert [denom] [count]    -> insert money (1,5,10,25,100)")
    print("  2. select [code]             -> choose product")
    print("  3. dispense                  -> dispense item / change")
    print("  4. cancel                    -> cancel + refund")
    print("  5. status                    -> show machine status")
    print("  6. quit")
    print("--------------------------------")


def main():
    vm = build_demo_machine()
    menu()
    while True:
        try:
            cmd = input("\n> ").strip().split()
            if not cmd:
                continue

            action = cmd[0].lower()
            if action == "quit":
                print("Goodbye 👋")
                sys.exit(0)

            elif action == "insert" and len(cmd) >= 3:
                denom_val = int(cmd[1])
                count = int(cmd[2])
                denom = Denomination(denom_val)
                vm.insert_money((denom, count))
                print(f"Inserted {count}x{denom_val}¢")

            elif action == "select" and len(cmd) >= 2:
                code = cmd[1].upper()
                vm.select_product(code)
                print(f"Selected {code}")

            elif action == "dispense":
                result = vm.dispense()
                print(f"➡️  Dispensed: {result}")

            elif action == "cancel":
                refund = vm.cancel()
                print(f"Refunded: {refund}")

            elif action == "status":
                print(vm.admin_status())

            else:
                print("Unknown command. Try again.")
        except Exception as e:
            print(f"❌ {e}")


if __name__ == "__main__":
    main()
