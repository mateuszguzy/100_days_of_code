import turtle
from turtle import Turtle, Screen
import colorgram
import random

turtle.colormode(255)
ash = Turtle()

colors_list = list()
painting_h = 0
painting_w = 0


def extract_colors():
    file_colors = colorgram.extract("image.jpg", 10)
    for color in file_colors:
        colors_list.append((color.rgb[0], color.rgb[1], color.rgb[2]))


def random_color():
    return random.choice(colors_list)


def set_size(height, width):
    global painting_w, painting_h
    painting_w = width
    painting_h = height


def make_dot():
    ash.dot(20, random_color())


def main():
    ash.penup()
    extract_colors()
    set_size(7, 7)
    step_y = 50
    for y in range(0, painting_h):
        step_x = 50
        for x in range(0, painting_w):
            ash.setx(step_x)
            step_x += 50
            make_dot()
        ash.sety(step_y)
        step_y += 50


if __name__ == "__main__":
    main()

screen = Screen()
screen.exitonclick()
