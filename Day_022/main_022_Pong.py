# TODO-20: palette class with methods that:
# TODO-25: can assign key bind, move palette up and down, detect end of window
# TODO-30: ball class, with methods that:
# TODO-40: detect collision, detect goal, set direction after collision
# TODO-50: scoreboard
from field import Field
from turtle import Screen

new_field = Field()
screen = Screen()


def main():

    screen.setup()
    new_field.setup(1000, 600)
    new_field.set_bounds()


if __name__ == "__main__":
    main()


screen.exitonclick()
