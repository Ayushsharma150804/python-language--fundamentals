# from gi.overrides.Gtk import MenuItem
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
Flag =True

while Flag:
    options=menu.get_items()
    user_input = input(f"choose you like: {options}")
    if user_input == "report":
        coffee_maker.report()
        money_machine.report()

    elif user_input == "off":
        Flag =False

    else:
        drink=menu.find_drink(user_input)
        # if coffee_maker.is_resource_sufficient(drink):
        #     if money_machine.make_payment(drink.cost):
        #         coffee_maker.make_coffee(drink)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
              coffee_maker.make_coffee(drink)





