from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.hideturtle()
        self.penup()
        self.setheading(180)
        self.car_body = list()

    def create(self):
        x_cord = 310
        random_y_cord = random.randint(-280, 260)
        random_color = random.choice(COLORS)
        for piece in range(2):
            piece = CarManager()
            piece.goto(x=x_cord, y=random_y_cord)
            piece.color(random_color)
            piece.showturtle()
            self.car_body.append(piece)
            x_cord += 20

    def move(self, level):
        for piece in self.car_body:
            piece.forward(STARTING_MOVE_DISTANCE + level * MOVE_INCREMENT)

