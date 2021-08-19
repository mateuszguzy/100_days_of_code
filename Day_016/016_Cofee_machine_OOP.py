from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
machine = CoffeeMaker()
money = MoneyMachine()


def main():

    user_input = input(f"Choose a beverage: {menu.get_items()}: ")
    if user_input == "report":
        machine.report()
        money.report()
        main()
    elif user_input == "off":
        quit()
    else:
        drink = menu.find_drink(user_input)
        if machine.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                machine.make_coffee(drink)
                main()
            else:
                main()
        else:
            main()


if __name__ == "__main__":
    main()
