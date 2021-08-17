from art import logo, vs
from game_data import game_data
import random, os

# assign game_data to another variable so it can be mutated
data = game_data
# define main variables used to comparison
compare_a = dict()
compare_b = dict()
# general user score
points = 0
# flag to end while loop
the_end = False

def clear_console():
    os.system("clear")

def check_answer():
    """Function checks if user answer is correct, and either gives points or quits game."""
    global the_end, points, compare_a, compare_b
    answer = input("Who has more instagram followers? (A) or (B)\n")
    if (answer == "A" or answer == "a") and compare_a["follower_count"] > compare_b["follower_count"]:
        points += 1
    elif (answer == "B" or answer == "b") and compare_a["follower_count"] < compare_b["follower_count"]:
        points += 1
    # if no correct answer change flag to True and end a main loop
    else:
        the_end = True

def reassing_data():
    """Make previous compare A as compare B, to choose new random B."""
    global compare_a, compare_b
    compare_a = compare_b

def choose_data():
    """Select random data from game data and removes it from list."""
    global data, compare_a, compare_b, points
    # only select random compare_a for first question, other are compare_b reassigned
    if points == 0:
        compare_a = random.choice(data)
        data.remove(compare_a)
    compare_b = random.choice(data)
    data.remove(compare_b)

def main():
    global the_end, points, compare_a, compare_b
    while the_end == False:
        # clear console only for new comparison, when lost leave the last comparison
        if the_end == False:
            clear_console()
        print(logo)
        print(f"Your points: {points}")
        choose_data()
        print("A: %s, a %s, from %s" % (compare_a["name"], compare_a["description"], compare_a["country"]))
        print(vs)
        print("B: %s, a %s, from %s" % (compare_b["name"], compare_b["description"], compare_b["country"]))
        check_answer()
        reassing_data()
    print(f"You lose with a score: {points}")
    quit()

if __name__ == "__main__":
    main()