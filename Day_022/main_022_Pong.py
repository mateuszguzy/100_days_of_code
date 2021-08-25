from field import Field
from turtle import Screen
from palette import Palette
from ball import Ball
from scoreboard import Scoreboard
import time

# create instances
screen = Screen()
# switch off screen tracking, only update when wanted
screen.tracer(0)
screen.listen()
# create instances
new_field = Field()
left_palette = Palette()
right_palette = Palette()
# prepare field
new_field.set_field(width=1000, height=600)
new_field.set_bounds()
# create palettes
left_palette.create("left", new_field.field_width, new_field.field_height)
right_palette.create("right", new_field.field_width, new_field.field_height)
# trigger key usage
new_field.field.onkey(left_palette.up, "w")
new_field.field.onkey(right_palette.up, "Up")
new_field.field.onkey(left_palette.down, "s")
new_field.field.onkey(right_palette.down, "Down")
# create scoreboards instances, for each player and for main messages
left_scoreboard = Scoreboard("left")
right_scoreboard = Scoreboard("right")
message = Scoreboard("message")


def main():
    game_is_on = True
    # show prepared game (after update()) and wait 2s before start
    left_scoreboard.show_score()
    right_scoreboard.show_score()
    ball = Ball()
    screen.update()
    time.sleep(2)
    # game in on until ball reach left/right edge
    while game_is_on:
        # ball is moving in constant random direction until reach palette or boundary
        ball.move()
        if ball.ycor() >= new_field.top_boundary - 15 or ball.ycor() <= new_field.bottom_boundary + 15:
            ball.boundary_reflection()
        # when ball on X coordinate reach palette it checks if ball Y coordinate is within all palette
        # pieces coordinates. If yes ball is reflected
        elif ball.xcor() >= right_palette.palette_x_cor - 20 or ball.xcor() <= left_palette.palette_x_cor + 20:
            if right_palette.palette_body[-1].ycor() - 25 < ball.ycor() < right_palette.palette_body[1].ycor() + 25 and \
                    ball.xcor() > 0:
                ball.palette_reflection()
                pass
            elif left_palette.palette_body[-1].ycor() - 25 < ball.ycor() < left_palette.palette_body[1].ycor() + 25 and \
                    ball.xcor() < 0:
                ball.palette_reflection()
                pass
            else:
                if ball.xcor() > 0:
                    left_scoreboard.score += 1
                    message.goal()
                    game_is_on = False
                    ball.reset()
                    left_palette.reset()
                    right_palette.reset()
                    time.sleep(2)
                    message.clear()
                    main()
                elif ball.xcor() < 0:
                    right_scoreboard.score += 1
                    message.goal()
                    game_is_on = False
                    ball.reset()
                    left_palette.reset()
                    right_palette.reset()
                    time.sleep(2)
                    message.clear()
                    main()
                pass

        else:

            pass
            # scoreboard


if __name__ == "__main__":
    main()

screen.exitonclick()
