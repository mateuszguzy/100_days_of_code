# TODO: make palette reflection angle depending on place on palette where ball hit
# https://gamedev.stackexchange.com/questions/4253/in-pong-how-do-you-calculate-the-balls-direction-when-it-bounces-off-the-paddl
# https://richardcarter.org/
# TODO: check game on different screen size (line 21)

from field import Field
from palette import Palette
from ball import Ball
from scoreboard import Scoreboard
import time


# create instances
new_field = Field()
left_palette = Palette()
right_palette = Palette()
# switch off screen tracking, only update when wanted
new_field.field.tracer(0)
new_field.field.listen()
# prepare field
new_field.set_field(width=1000, height=600)
new_field.set_bounds()
# create palettes and pass field dimensions to use them in palette class
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
    # game is on until ball passes the palette (scores)
    game_is_on = True
    # show prepared game (after update()) and wait 2s before start
    left_scoreboard.show_score()
    right_scoreboard.show_score()
    # every new start generates a ball in the middle of the field
    ball = Ball()
    # show whole prepared field using update
    new_field.field.update()
    # wait 2s for players to be ready
    time.sleep(2)
    # game in on until ball reach left/right edge
    while game_is_on:
        # ball is moving in constant random direction until reach palette or boundary
        ball.move()
        # detect collision with top and bottom boundary
        if ball.ycor() >= new_field.top_boundary - 15 or ball.ycor() <= new_field.bottom_boundary + 15:
            # trigger ball class reflection function
            ball.boundary_reflection()
        # when ball on X coordinate reach palette it checks if ball Y coordinate is within all palette
        # pieces Y coordinates. If yes ball is reflected if not it's a score
        # check ball position on right or left palette coordinate
        elif ball.xcor() >= right_palette.palette_x_cor - 20 or ball.xcor() <= left_palette.palette_x_cor + 20:
            # check for right palette if ball on +X
            if right_palette.palette_body[-1].ycor() - 25 < ball.ycor() < right_palette.palette_body[1].ycor() + 25 \
                    and ball.xcor() > 0:
                ball.palette_reflection()
                pass
            # check for left palette if ball on -X
            elif left_palette.palette_body[-1].ycor() - 25 < ball.ycor() < left_palette.palette_body[1].ycor() + 25 \
                    and ball.xcor() < 0:
                ball.palette_reflection()
                pass
            # else there's a score
            else:
                if ball.xcor() > 0:
                    # if ball is on +X coordinate add score for left player
                    left_scoreboard.score += 1
                    message.goal()
                    # break a game loop
                    game_is_on = False
                    # reset ball position
                    ball.reset()
                    # reset palette position to middle
                    left_palette.set_position("left")
                    right_palette.set_position("right")
                    # wait 2s, after erase communicate
                    time.sleep(2)
                    message.clear()
                    # start game loop over again
                    main()
                elif ball.xcor() < 0:
                    # if ball is on -X coordinate add score for right player
                    right_scoreboard.score += 1
                    message.goal()
                    game_is_on = False
                    ball.reset()
                    # reset palette position to middle
                    left_palette.set_position("left")
                    right_palette.set_position("right")
                    time.sleep(2)
                    message.clear()
                    main()
                pass


if __name__ == "__main__":
    main()

new_field.field.exitonclick()
