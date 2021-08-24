from turtle import Turtle, Screen
import random
import time


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed = 0.03
        self.screen = Screen()
        self.direction = random.randint(0, 360)
        # self.direction = 355
        self.setheading(self.direction)

    def move(self):
        # if no collision ball moves
        # first generate random direction from 360deg
        # after collision with boundary or palette designate specific angle

        self.forward(10)
        time.sleep(self.speed)
        self.screen.update()

    def reflect(self):
        self.setheading(-self.heading())
        pass

