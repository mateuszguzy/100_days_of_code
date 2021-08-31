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
        self.high_score = self.read_score()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)

    def update_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=(FONT, SCOREBOARD_FONT_SIZE, FONT_TYPE))

    def increase_score(self):
        self.score += 1

    def read_score(self):
        with open('high_score.txt') as file:
            score = int(file.read())
            print(score)
            return score
        pass

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('high_score.txt', mode='w') as file:
                file.write(str(self.score))
        self.score = 0
        self.update_score()

