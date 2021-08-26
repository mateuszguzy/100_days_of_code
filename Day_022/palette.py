from turtle import Turtle, Screen


class Palette(Turtle):
    def __init__(self):
        # inherit attributes from Turtle class
        super().__init__()
        self.screen = Screen()
        self.penup()
        self.color("white")
        self.shape("square")
        self.setheading(90)
        # distance how much a palette will move with one key stroke
        self.distance = 10
        self.palette_length = 120
        self.palette_body = list()
        self.speed("fastest")
        self.field_width = 0
        self.field_height = 0
        self.top_boundary = 0
        self.bottom_boundary = 0
        self.palette_x_cor = 0

    def create(self, side, field_width, field_height):
        # height and width passed to set palette position depending on screen size
        self.field_height = field_height
        self.field_width = field_width
        # set where are boundaries
        self.top_boundary = ((self.field_height / 2) - 50)
        self.bottom_boundary = -((self.field_height / 2) - 50)
        # variable used to set next palette pieces
        y_cord_step = 0
        for piece in range(int(self.palette_length / 20)):
            piece = Palette()
            # when provided palette side make it on +X or -X coordinates
            if side == "left":
                self.palette_x_cor = -((self.field_width / 2) - 30)
                piece.goto(x=self.palette_x_cor, y=((self.palette_length / 2) - y_cord_step))
            elif side == "right":
                self.palette_x_cor = ((self.field_width / 2) - 30)
                piece.goto(x=self.palette_x_cor, y=((self.palette_length / 2) - y_cord_step))
            y_cord_step += 20
            self.palette_body.append(piece)
        self.hideturtle()

    def set_position(self, side):
        """Function to reset palette position after a goal."""
        y_cord_step = 0
        for piece in range(len(self.palette_body)):
            # need to distinguish left and right because of X coordinates
            if side == "left":
                self.palette_body[piece].goto(x=self.palette_x_cor, y=((self.palette_length / 2) - y_cord_step))
            elif side == "right":
                self.palette_body[piece].goto(x=self.palette_x_cor, y=((self.palette_length / 2) - y_cord_step))
            y_cord_step += 20

    def up(self):
        # move palette so last piece takes place of previous block, no gap between blocks when animated
        for piece in range((len(self.palette_body) - 1), -1, -1):
            # when boundary is reached palette stop moving
            if self.palette_body[0].ycor() >= self.top_boundary - 10:
                pass
            else:
                self.palette_body[piece].forward(self.distance)
            self.screen.update()

    def down(self):
        # move palette so last piece takes place of previous block, no gap between blocks when animated
        for piece in range(0, (len(self.palette_body))):
            # when boundary is reached palette stop moving
            if self.palette_body[-1].ycor() <= self.bottom_boundary + 20:
                pass
            else:
                self.palette_body[piece].backward(self.distance)
        self.screen.update()


