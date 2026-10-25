import sys


def parse_input() -> dict:
    inventory = {}
    for v in sys.argv[1:]:
        # ErrorCheck1: check format key:value
        try:
            key, value = v.split(":")
        except ValueError:
            print(f"Error - invalid parameter '{v}'")
            continue

        # ErrorCheck2: redundant key
        if key in inventory:
            print(f"Redundant item '{key}' - discarding")
            continue

        # ErrorCheck3: check value is int
        try:
            value_int = int(value)
        except ValueError as e:
            print(f"Quantity error for '{key}': {e}")
            continue

        inventory[key] = value_int
    return inventory


def inventory_stats(inventory: dict) -> None:
    total = sum(inventory.values())

    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    print(f"Total quantity of the {len(inventory)} items: {total}")
    if total == 0:
        return

    hi = lo = list(inventory.keys())[0]
    for k in inventory:
        pct = round(inventory[k] / total * 100, 1)
        print(f"Item {k} represents {pct}%")
        hi, lo = (
            (k if inventory[k] > inventory[hi] else hi),
            (k if inventory[k] < inventory[lo] else lo),
        )

    print(f"Item most abundant: {hi} with quantity {inventory[hi]}")
    print(f"Item least abundant: {lo} with quantity {inventory[lo]}")


def update_inventory(inventory: dict) -> None:
    inventory["magic_item"] = 1
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    inventory = parse_input()
    inventory_stats(inventory)
    update_inventory(inventory)
