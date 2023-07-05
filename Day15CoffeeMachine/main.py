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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

total_profit = 0

def printReport():
    print("Resources remaining:")
    print("Water: " + str(resources["water"]) + "ml")
    print("Milk: " + str(resources["milk"]) + "ml")
    print("Coffee: " + str(resources["coffee"]) + "g")
    print("Money: " + "$" + str(total_profit))

def sufficient_resources(drink_of_choice):
    for ingredient in drink_of_choice["ingredients"]:
        if resources[ingredient] < drink_of_choice["ingredients"][ingredient]:
            print("Sorry there is not enough " + ingredient + ".")
            return False    
    return True

def calculate_profit(drink_of_choice):
    global total_profit
    total_profit += drink_of_choice["cost"]

def make_coffee(drink_of_choice):
    for ingredient in drink_of_choice["ingredients"]:
        resources[ingredient] -= drink_of_choice["ingredients"][ingredient]


def process_coins():
    quarters_amount = int(input("How many quarters? ")) * 0.25
    dimes_amount = int(input("How many dimes? ")) * 0.1
    nickles_amount = int(input("How many nickles? ")) * 0.05
    pennies_amount = int(input("How many pennies? ")) * 0.01

    total = quarters_amount + dimes_amount + nickles_amount + pennies_amount

    return total


is_coffee_machine_on = True

while is_coffee_machine_on:
    choice = input("Hello customer! What would you like? (espresso/latte/cappuccino): ")

    if choice == "off":
        is_coffee_machine_on = False
    elif choice == "report":
        printReport()
    elif choice.lower() in MENU:
        if sufficient_resources(MENU[choice.lower()]):
            payment = process_coins()
            if payment >= MENU[choice.lower()]["cost"]:
                change = round(payment - MENU[choice.lower()]["cost"],2)
                print("Here is your change: $" + str(change))
                make_coffee(MENU[choice.lower()])
                calculate_profit(MENU[choice.lower()])
                print('Here is your ' + choice.lower() + "! Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")


