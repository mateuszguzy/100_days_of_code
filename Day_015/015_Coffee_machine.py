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
# TODO-25: implement "report" function which will print ingredients status
# TODO-27: implement "off" function which will shut the program no matter when typed
# TODO-30: function checking if machine has sufficient ingredients. If not prompt specific message for every ingredient
# TODO-40: user input what and how many coins to insert (total amount stated by app)
# TODO-50: function checking if given amount of coins is enough and if needed give return amount value
# TODO-70: "make coffee" function - deduct ingredients values from machine resources, and print finish message


def clean_console():
    os.system("clear")


def check_ingredients(coffee_type):
    """Function checks if wanted coffee type is possible to be made."""
    global machine
    for key, value in MENU[coffee_type]["ingredients"].items():
        # print("Machine: %s, %s Coffee: %s, %s"
        #       % (key, machine["ingredients"][key], key, MENU[coffee_type]["ingredients"][key]))
        if machine["ingredients"][key] < MENU[coffee_type]["ingredients"][key]:
            print("Sorry. Not enough %s." % key)
            main()


def insert_money():
    """Function asks and counts how many coins have been inserted."""
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pennies?: "))
    amount = coins["quarter"] * quarters + coins["dime"] * dimes + coins["nickel"] * nickles + coins["penny"] * pennies
    print(amount)
    return amount
    # check if given amount of money is enough
    # if amount < MENU[coffee_type]["ingredients"][key]









def main():
    global machine
    # user input, to choose type of coffee
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ")
    check_ingredients(coffee_type)
    print("Please insert $%s." % MENU[coffee_type]["cost"])
    amount = insert_money()
    if amount < MENU[coffee_type]["cost"]:
        clean_console()
        print("Sorry, not enough money. Money refunded.")
        main()



if __name__ == "__main__":
    main()
