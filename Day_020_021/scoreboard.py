from turtle import Turtle
ALIGNMENT = "center"
FONT = "Arial"
SCOREBOARD_FONT_SIZE = 14
FONT_TYPE = "normal"
GAME_OVER_FONT_SIZE = 30


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=(FONT, SCOREBOARD_FONT_SIZE, FONT_TYPE))

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg="GAME OVER!", align=ALIGNMENT, font=(FONT, GAME_OVER_FONT_SIZE, FONT_TYPE))
