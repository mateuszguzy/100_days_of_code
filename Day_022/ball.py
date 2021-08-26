from turtle import Turtle, Screen
import random
import time


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        # designate ball speed
        self.speed = 0.01
        self.screen = Screen()
        self.direction = random.randint(0, 360)
        # precise angle used for debugging
        # self.direction = 5
        self.setheading(self.direction)

    def move(self):
        self.forward(5)
        time.sleep(self.speed)
        self.screen.update()

    # both reflections from boundary and palette are calculated to have same angle as when approaching
    def palette_reflection(self):
        # reflection angle depends on ball current heading
        if 0 < self.heading() <= 90:
            self.setheading(180 - self.heading())
            pass
        elif 90 < self.heading() <= 180:
            self.setheading(180 - self.heading())
            pass
        elif 180 < self.heading() <= 270:
            self.setheading(360 - (self.heading() - 180))
            pass
        elif 270 < self.heading() <= 360:
            self.setheading(180 + (360 - self.heading()))
            pass

    def boundary_reflection(self):
        # reflection angle depends on ball current heading
        if 0 < self.heading() <= 90:
            self.setheading(270 + (90 - self.heading()))
            pass
        elif 90 < self.heading() <= 180:
            self.setheading(180 + (180 - self.heading()))
            pass
        elif 180 < self.heading() <= 270:
            self.setheading(90 + (270 - self.heading()))
            pass
        elif 270 < self.heading() <= 360:
            self.setheading((360 - self.heading()))
            pass
