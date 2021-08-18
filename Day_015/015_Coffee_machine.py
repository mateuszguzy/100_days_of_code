import os

from menu import MENU

# create global dictionary for ingredients and cash
machine = {
    "ingredients": {
        "water": 300,
        "milk": 200,
        "coffee": 100
    },
    "money": 0
}
coins = {
    "quarter": 0.25,
    "dime": 0.1,
    "nickel": 0.05,
    "penny": 0.01
}


def make_coffee(coffee_type):
    """Function deducts used ingredients from machine resources."""
    global machine
    for key, value in MENU[coffee_type]["ingredients"].items():
        machine["ingredients"][key] -= MENU[coffee_type]["ingredients"][key]
    print("Your coffee is ready!")
    main()


def report():
    """Function shows available ingredients in machine."""
    unit = ""
    for key, value in machine["ingredients"].items():
        if key == "water" or key == "milk":
            unit = "ml"
        elif key == "coffee":
            unit = "g"
        print("%s = %s%s" % (key.title(), value, unit))
    main()


def clean_console():
    os.system("clear")


def check_ingredients(coffee_type):
    """Function checks if wanted coffee type is possible to be made."""
    global machine
    for key, value in MENU[coffee_type]["ingredients"].items():
        if machine["ingredients"][key] < MENU[coffee_type]["ingredients"][key]:
            print("Sorry. Not enough %s.\n" % key)
            main()


def insert_money():
    """Function asks and counts how many coins have been inserted."""
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pennies?: "))
    amount = coins["quarter"] * quarters + coins["dime"] * dimes + coins["nickel"] * nickles + coins["penny"] * pennies
    return amount


def main():
    global machine
    # user input, to choose type of coffee
    coffee_type = input("\nWhat would you like? (espresso/latte/cappuccino): ")
    # "report" function which print available ingredients
    if coffee_type == "report":
        report()
    # "off" function which will shut the program
    elif coffee_type == "off":
        print("Shutting down.")
        quit()
    # function checking if machine has sufficient ingredients. If not prompt specific message for every ingredient
    check_ingredients(coffee_type)
    print("Please insert $%s.\n" % MENU[coffee_type]["cost"])
    # user input what and how many coins to insert (needed amount stated above)
    amount = insert_money()
    # function checking if given amount of coins is enough and if there's more give return amount value
    if amount < MENU[coffee_type]["cost"]:
        # clean_console()
        print("Sorry, not enough money. Money refunded.\n")
        main()
    elif amount > MENU[coffee_type]["cost"]:
        change = round((amount - MENU[coffee_type]["cost"]), 2)
        print("Here is $%s in change.\n" % change)
    # "make coffee" function - deduct ingredients values from machine resources, and print finish message
    make_coffee(coffee_type)


if __name__ == "__main__":
    main()
