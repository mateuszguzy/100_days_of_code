from turtle import Turtle, Screen


class Palette(Turtle):
    def __init__(self):
        super().__init__()
        self.screen = Screen()
        self.penup()
        self.color("white")
        self.shape("square")
        self.setheading(90)
        self.distance = 20
        self.palette_length = 120
        self.palette_body = list()
        self.speed("fastest")
        self.field_width = 0
        self.field_height = 0
        self.top_boundary = 0
        self.bottom_boundary = 0
        self.palette_x_cor = 0

    def create(self, side, field_width, field_height):
        self.field_height = field_height
        self.field_width = field_width
        self.top_boundary = ((self.field_height / 2) - 50)
        self.bottom_boundary = -((self.field_height / 2) - 50)
        y_cord_step = 0
        for piece in range(int(self.palette_length / 20)):
            piece = Palette()
            if side == "left":
                self.palette_x_cor = -((self.field_width / 2) - 30)
                piece.goto(x=self.palette_x_cor, y=((self.palette_length / 2) - y_cord_step))
            elif side == "right":
                self.palette_x_cor = ((self.field_width / 2) - 30)
                piece.goto(x=self.palette_x_cor, y=((self.palette_length / 2) - y_cord_step))

            y_cord_step += 20
            self.palette_body.append(piece)
        self.hideturtle()

    def up(self):
        for piece in range((len(self.palette_body) - 1), -1, -1):
            if self.palette_body[0].ycor() >= self.top_boundary - 10:
                pass
            else:
                self.palette_body[piece].forward(10)
            self.screen.update()

    def down(self):
        for piece in range(0, (len(self.palette_body))):
            if self.palette_body[-1].ycor() <= self.bottom_boundary + 20:
                pass
            else:
                self.palette_body[piece].backward(10)
        self.screen.update()


