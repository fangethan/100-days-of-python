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

def are_resources_sufficient(drink_of_choice):
    global total_profit
    if drink_of_choice == "espresso":
        if resources["water"] >= MENU["espresso"]["ingredients"]["water"] and resources["coffee"] >= MENU["espresso"]["ingredients"]["coffee"]:
            
            resources["water"] -= MENU["espresso"]["ingredients"]["water"]
            resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
            total_profit += MENU["espresso"]["cost"]
    
    elif drink_of_choice == "latte":
        if (resources["water"] >= MENU["latte"]["ingredients"]["water"] and resources["milk"] >= MENU["latte"]["ingredients"]["milk"] and
            resources["coffee"] >= MENU["latte"]["ingredients"]["coffee"]):
            
            resources["water"] -= MENU["latte"]["ingredients"]["water"]
            resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
            resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
            total_profit += MENU["latte"]["cost"]
    else:
        if (resources["water"] >= MENU["cappuccino"]["ingredients"]["water"] and resources["milk"] >= MENU["cappuccino"]["ingredients"]["milk"] and
            resources["coffee"] >= MENU["cappuccino"]["ingredients"]["coffee"]):
            
            resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
            resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
            resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
            total_profit += MENU["cappuccino"]["cost"]

is_coffee_machine_on = True

while is_coffee_machine_on:
    choice = input("Hello customer! What would you like? (espresso/latte/cappuccino): ")

    if choice == "off":
        is_coffee_machine_on = False
    elif choice == "report":
        printReport()
    elif choice.lower() in MENU:
        print(choice)
        are_resources_sufficient(choice.lower())


