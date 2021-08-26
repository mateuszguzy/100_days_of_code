from turtle import Turtle
ALIGNMENT = "center"
FONT = "Arial"
SCOREBOARD_FONT_SIZE = 14
FONT_TYPE = "normal"
GAME_OVER_FONT_SIZE = 30


class Scoreboard(Turtle):
    def __init__(self, side):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        # set score info above each player
        if side == "left":
            self.goto(x=-250, y=270)
        elif side == "right":
            self.goto(x=250, y=270)
        # message on the middle of the screen about goal or end ot the game
        elif side == "message":
            self.goto(x=0, y=0)

    def show_score(self):
        # erase previous score and write a new one
        self.clear()
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=(FONT, SCOREBOARD_FONT_SIZE, FONT_TYPE))

    def increase_score(self):
        self.score += 1

    def game_over(self):
        self.write(arg="GAME OVER!", align=ALIGNMENT, font=(FONT, GAME_OVER_FONT_SIZE, FONT_TYPE))

    def goal(self):
        self.write(arg="GOAL!", align=ALIGNMENT, font=(FONT, GAME_OVER_FONT_SIZE, FONT_TYPE))
