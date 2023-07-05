from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


is_coffee_machine_on = True

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

while is_coffee_machine_on:
    choice = input("Hello customer! What would you like? (espresso/latte/cappuccino): ")

    if choice == "off":
        is_coffee_machine_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice.lower() in menu.get_items():
        if coffee_maker.is_resource_sufficient(menu.find_drink(choice.lower())):
            if money_machine.make_payment(menu.find_drink(choice.lower()).cost):
                coffee_maker.make_coffee(menu.find_drink(choice.lower()))
        
