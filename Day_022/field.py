from turtle import Turtle, Screen


class Field:
    def __init__(self):
        self.field = Screen()
        self.field.bgcolor("black")
        self.field.title("Let's PONG!")
        self.field_height = 0
        self.field_width = 0
        self.bounds = Turtle()
        self.bounds.speed("fastest")
        self.bounds.hideturtle()
        self.bounds.color("white")

    def setup(self, width, height):
        self.field_height = height
        self.field_width = width
        self.field.setup(width=width, height=height)

    def set_bounds(self):
        # upper and lower bound
        self.bounds.penup()
        self.bounds.goto(x=-(self.field_width/2), y=((self.field_height/2)-20))
        self.write(self.field_width)
        self.bounds.goto(x=-(self.field_width/2), y=-((self.field_height/2)-20))
        self.write(self.field_width)
        # middle line
        self.bounds.goto(x=0, y=-((self.field_height/2)-20))
        self.bounds.setheading(90)
        for dash in range(25):
            distance = (self.field_height - 40) / 25
            self.write(distance)
            self.bounds.forward(distance)

    def write(self, distance):
        self.bounds.pendown()
        self.bounds.forward(distance)
        self.bounds.penup()



