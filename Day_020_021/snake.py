import time
from turtle import Turtle, Screen


class Snake:

    def __init__(self):
        self.snake_body = list()
        self.screen = Screen()
        self.speed = 0.1

    def starting_body(self):
        x_cord = 0
        y_cord = 0
        self.add_fragment(3)

        for piece in self.snake_body:
            piece.setposition(y=y_cord, x=x_cord)
            x_cord -= 20
        self.screen.update()

    def add_fragment(self, how_many):
        for piece in range(0, how_many):
            piece = Turtle("square")
            piece.color("white")
            piece.penup()
            # creating list of Objects - pieces of snake
            self.snake_body.append(piece)

    def move(self):
        self.screen.update()
        # last piece of snake takes place of the piece before it
        for piece in range((len(self.snake_body) - 1), 0, -1):
            new_cords = self.snake_body[piece - 1].position()
            new_orientation = self.snake_body[piece - 1].heading()
            self.snake_body[piece].setposition(new_cords)
            self.snake_body[piece].setheading(new_orientation)
        # sleep function cannot be in for loop because game lags with higher amount of snake pieces!!
        time.sleep(self.speed)
        self.snake_body[0].forward(20)

    def grow(self):
        piece = Turtle("square")
        piece.color("white")
        piece.penup()
        last_piece_position = self.snake_body[-1].position()
        piece.setposition(last_piece_position)
        self.snake_body.append(piece)
        # print(self.speed)

    # movement methods
    def up(self):
        if self.snake_body[0].heading() == 270:
            pass
        else:
            self.snake_body[0].setheading(90)

    def down(self):
        if self.snake_body[0].heading() == 90:
            pass
        else:
            self.snake_body[0].setheading(270)

    def left(self):
        if self.snake_body[0].heading() == 0:
            pass
        else:
            self.snake_body[0].setheading(180)

    def right(self):
        if self.snake_body[0].heading() == 180:
            pass
        else:
            self.snake_body[0].setheading(0)

