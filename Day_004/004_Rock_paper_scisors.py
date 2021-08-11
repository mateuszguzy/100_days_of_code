import random

user_figure = int(input("What do you choose? Rock - '0', Paper - '1', Scissors - '2'\n"))
computer_figure = random.randint(0, 2)

if computer_figure == 0:
    if user_figure == 0:
        print("You: Rock")
        print("AI: Rock")
        print("It's a draw.")
    elif user_figure == 1:
        print("You: Paper")
        print("AI: Rock")
        print("You win!")
    else:
        print("You: Scissors")
        print("AI: Rock")
        print("AI wins")

if computer_figure == 1:
    if user_figure == 1:
        print("You: Paper")
        print("AI: Paper")
        print("It's a draw.")
    elif user_figure == 2:
        print("You: Scissors")
        print("AI: Paper")
        print("You win!")
    else:
        print("You: Rock")
        print("AI: Paper")
        print("AI wins")

if computer_figure == 2:
    if user_figure == 2:
        print("You: Scissors")
        print("AI: Scissors")
        print("It's a draw.")
    elif user_figure == 0:
        print("You: Rock")
        print("AI: Scissors")
        print("You win!")
    else:
        print("You: Paper")
        print("AI: Scissors")
        print("AI wins")