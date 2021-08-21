from turtle import Turtle, Screen
import random

is_race_on = False
colors = ["red", "green", "blue", "orange", "yellow", "violet"]
champions = list()
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Choose your champion!", prompt=f"Choose champion color: {colors}")

if user_bet:
    is_race_on = True


def starting_pos():
    x_pos = -230
    y_pos = -80
    # create turtle models from two lists containing name and color
    for name, color in zip(range(0, 6), colors):
        name = Turtle("turtle")
        name.color(color)
        champions.append(name)
    # set each champion on it's starting position
    for champion in champions:
        champion.penup()
        champion.goto(x=x_pos, y=y_pos)
        y_pos += 30


def check_for_winner(champion):
    global is_race_on, user_bet
    finish_line = 230
    if champion.xcor() >= finish_line:
        if champion.pencolor().lower() == user_bet.lower():
            print("Congratulations, you've won!")
        else:
            print("You've lost.")
        print(f"Winning turtle: {champion.pencolor().upper()}.")
        is_race_on = False


def main():
    global is_race_on
    if is_race_on:
        starting_pos()
    while is_race_on:
        for champion in champions:
            distance = random.randint(0, 10)
            champion.forward(distance)
            check_for_winner(champion)


if __name__ == "__main__":
    main()

screen.exitonclick()

