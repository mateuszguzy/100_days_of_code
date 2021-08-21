from turtle import Turtle, Screen

ash = Turtle()
screen = Screen()
step = 10


def move_forward():
    global step
    ash.forward(step)


def turn_right():
    global step
    ash.right(step)


def turn_left():
    global step
    ash.left(step)


def move_backwards():
    global step
    ash.backward(step)


def clean():
    ash.clear()
    ash.penup()
    ash.home()
    ash.pendown()


def main():
    screen.listen()
    screen.onkey(move_forward, "w")
    screen.onkey(turn_left, "a")
    screen.onkey(turn_right, "d")
    screen.onkey(move_backwards, "s")
    screen.onkey(clean, "c")





if __name__ == "__main__":
    main()

screen.exitonclick()

