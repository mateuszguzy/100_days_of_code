import os
from art import logo

bids = dict()

def clear():
    """Clears console"""
    os.system("clear")

def choose_winner():
    
    higher_bidder = ""
    higher_bid = 0
    bid_values = list()

    # create a list of bid values to sort them and choose higher
    for value in bids.values():

        bid_values.append(value)

    bid_values.sort()

    # after sort take last one (higher) and extract it's key from dictionary
    for key, value in bids.items():

        if value == bid_values[-1]:

            higher_bidder = key
            higher_bid = value

    print("Auction winner is: %s, with value of: $%s" % (higher_bidder, higher_bid))

def new_bid():

    name = input("What is your name?\n")
    bid = int(input("What is your bid?\n$ "))

    # if both values are provided place them in the dictionary
    if name and bid:

        bids[name] = bid

    answer = input("Is there another bidder? (y)es || (n)o\n")

    if answer == "y":

        clear()
        new_bid()

    else:

        clear()
        choose_winner()
        quit()

def main():
        
    print(logo)
    print("Welcome to the silent auction program.")
    new_bid()

if __name__ == "__main__":

    main()