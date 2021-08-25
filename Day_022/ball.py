from turtle import Turtle, Screen
import random
import time


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed = 0.02
        self.screen = Screen()
        # self.direction = random.randint(0, 360)
        self.direction = 5
        self.setheading(self.direction)

    def move(self):
        self.forward(5)
        time.sleep(self.speed)
        self.screen.update()

    def palette_reflection(self):
        if 0 < self.heading() < 90:
            self.setheading(180 - self.heading())
            pass
        elif 90 < self.heading() < 180:
            self.setheading(180 - self.heading())
            pass
        elif 180 < self.heading() < 270:
            self.setheading(360 - (self.heading() - 180))
            pass
        elif 270 < self.heading() < 360:
            self.setheading(180 + (360 - self.heading()))
            pass

    def boundary_reflection(self):
        if 0 < self.heading() < 90:
            self.setheading(70 + (90 - self.heading()))
            pass
        elif 90 < self.heading() < 180:
            self.setheading(180 + (180 - self.heading()))
            pass
        elif 180 < self.heading() < 270:
            self.setheading(90 + (270 - self.heading()))
            pass
        elif 270 < self.heading() < 360:
            self.setheading((360 - self.heading()))
            pass
