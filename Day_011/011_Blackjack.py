from art import logo
import random

cards = {"1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10, "A":10}
# list needed to user random function on figures
cards_figures = list()
# global variables to use them in different functions
user_deck = list()
computer_deck = list()
points = dict()
# need to define starting value because it later cannot add to non-existing value
points["user"] = 0
points["computer"] = 0
player_still_drawing = True

# prepare list of figures to randomly choose from. Cannot from .keys() directly.
for figure in cards.keys():
    cards_figures.append(figure)

def starting_draw():
    """Function used only in first draw. Draws two cards for every player."""
    global computer_deck, user_deck, points
    # "random.choices" return a list, so not append but it just equals to result of this function
    user_deck = (random.choices(cards_figures, k = 2))
    computer_deck = (random.choices(cards_figures, k = 2))
    for card in user_deck:
        points["user"] += cards[card]

    for card in computer_deck:
        points["computer"] += cards[card]

def show_results():
    global points, player_still_drawing, user_deck, computer_deck
    # need to assign values to new variables becuase f-string doesn't work on square brackets reference
    user_points = points["user"]
    computer_points = points["computer"]
    computer_deck_covered = [computer_deck[0], "X"]
    #when player is still drawing second drawn card for computer is hidden
    if player_still_drawing == True:
        check_computer_deck = computer_deck_covered
        check_computer_points = cards[computer_deck[0]]
    # after player stops drawing we unhide second computers card and add it's value to computer's points
    else:
        check_computer_deck = computer_deck
        check_computer_points = computer_points

    print(f"\nUser deck {user_deck}\nComputer deck: {check_computer_deck}")
    print(f"\nUser points: {user_points}, Computer points: {check_computer_points}")

def computer_draw():
    global computer_deck
    """Function used when player no longer draw cards."""
    # single card is drawn
    draw_card("computer", computer_deck)
    # results are shown
    show_results()
    # function checks if any player won or computer draws again
    check_points()

def check_points():
    global points, player_still_drawing, user_deck, computer_deck
    user_points = points["user"]
    computer_points = points["computer"]
    # if any player exceedes 21 points, game ends
    if user_points > 21:
        print("\nComputer wins.")
        quit()
    elif computer_points > 21:
        print("\n!!! You win !!!")
        quit()
    # after user stopped drawing function decides if computer win or need to draw another card
    if player_still_drawing == False:
        if user_points < computer_points:
            print("\nComputer wins.")
            quit()
        elif user_points >= computer_points:
            computer_draw()
        elif user_points == computer_points:
            print("It's a draw")
            quit()

def question():
    """Function to determine if user takes another draw or rests."""
    global user_deck, player_still_drawing
    answer = input("\nDo you want to draw another card?\n(y)es || (n)o\n")
    # if player draws, system chooses another card
    if answer == "y":
        # card is added to deck of player provided as argument
        draw_card("user", user_deck)
    else:
        # function checks if user points did not excedeed 21
        check_points()
        # if player chooses to not draw another card, flag is set to False and from now on, only computer draws and checkes cards.
        player_still_drawing = False

def draw_card(*args):
    """Function used to draw single card for player which name and deck are provided as an argument"""
    global points
    new_card = random.choice(cards_figures)
    # card is added to deck of player provided as argument
    args[1].append(new_card)
    # card points are added to points dictionary
    points[args[0]] += cards[new_card]

def main():
    """Blackjack main function."""
    global player_still_drawing
    print(logo)
    # function overwrites global "user_deck" and "computer_deck"
    starting_draw()
    # show current points
    show_results()
    # while user is still playing, system needs to check if player want to draw another card
    # and if 21 points are not excedeed
    while player_still_drawing == True:
        # function asks user if willing to draw another card if yes it's drawn and added to deck
        question()
        show_results()
        # function checks if user points did not excedeed 21
        check_points()
        # show current points

if __name__ == "__main__":
    main()