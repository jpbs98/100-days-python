MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

RESOURCES = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

COIN_VALUE = {
    "quarter": 0.25,
    "dime": 0.1,
    "nickel": 0.05,
    "penny": 0.01
}


def report():
    for key, v in RESOURCES.items():
        if key == "money":
            print(f"{key.title()}: ${v}")
        else:
            unit = "ml" if key in ["water", "milk"] else "g"
            print(f"{key.title()}: {v}{unit}")


def check_resources(drink):
    for key, val in MENU[drink]["ingredients"].items():
        if val > RESOURCES[key]:
            print(f"Sorry, there is not enough {key}")
            return False
    return True


def process_coins():
    quarters = float(input("how many quarters?: "))
    dimes = float(input("how many dimes?: "))
    nickels = float(input("how many nickels?: "))
    pennies = float(input("how many pennies?: "))

    return COIN_VALUE["quarter"] * quarters + COIN_VALUE["dime"] * dimes + COIN_VALUE["nickel"] * \
        nickels + COIN_VALUE["penny"] * pennies


def process_order(drink):
    for key, val in MENU[drink]["ingredients"].items():
        RESOURCES[key] -= val


def main():
    while True:
        order = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if order == "off":
            break

        if order == "report":
            report()
            continue

        if not check_resources(order):
            continue

        print("Please insert coins.")
        value_inserted = process_coins()
        cost = MENU[order]["cost"]
        if not value_inserted >= cost:
            print("Sorry, that's not enough money. Money refunded.")
            continue

        if value_inserted == cost:
            RESOURCES["money"] += value_inserted
        else:
            change = value_inserted - cost
            RESOURCES["money"] += cost
            print(f"Here is ${round(change, 2)} in change.")

        process_order(order)
        print(f"Here is your {order}. Enjoy!")


if __name__ == "__main__":
    main()
