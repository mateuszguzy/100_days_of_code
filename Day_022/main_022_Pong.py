# TODO-30:
# TODO-40: detect goal
# TODO-50: scoreboard
from field import Field
from turtle import Screen
from palette import Palette
from ball import Ball

game_is_on = True
new_field = Field()
screen = Screen()
ball = Ball()
screen.tracer(0)
# palette creation
left_palette = Palette()
right_palette = Palette()
# left_palette.create("left")
# right_palette.create("right")
# trigger key usage
new_field.field.listen()
# define key bind for each palette
new_field.field.onkey(left_palette.up, "w")
new_field.field.onkey(right_palette.up, "Up")
new_field.field.onkey(left_palette.down, "s")
new_field.field.onkey(right_palette.down, "Down")


def main():
    global game_is_on
    screen.setup()
    new_field.set_field(width=1000, height=600)
    new_field.set_bounds()
    left_palette.create("left", new_field.field_width, new_field.field_height)
    right_palette.create("right", new_field.field_width, new_field.field_height)
    screen.update()

    while game_is_on:
        ball.move()
        # detect collisions
        if ball.ycor() >= new_field.top_boundary - 18:
            if 0 < ball.heading() < 90:
                new_heading = 270 + (90 - ball.heading())
                ball.setheading(new_heading)
                pass
            elif 90 < ball.heading() < 180:
                new_heading = 180 + (180 - ball.heading())
                ball.setheading(new_heading)
                pass
        elif ball.ycor() <= new_field.bottom_boundary + 18:
            if 180 < ball.heading() < 270:
                new_heading = 90 + (270 - ball.heading())
                ball.setheading(new_heading)
                pass
            elif 270 < ball.heading() < 360:
                new_heading = (360 - ball.heading())
                ball.setheading(new_heading)
                pass
        else:
            for l_piece, r_piece in zip(left_palette.palette_body, right_palette.palette_body):
                # with pallets
                if ball.distance(l_piece) <= 20 or ball.distance(r_piece) <= 20:
                    # print(ball.heading())
                    if 0 < ball.heading() < 90:
                        new_heading = 180 - ball.heading()
                        ball.setheading(new_heading)
                        pass
                    elif 90 < ball.heading() < 180:
                        new_heading = 180 - ball.heading()
                        ball.setheading(new_heading)
                        pass
                    elif 180 < ball.heading() < 270:
                        new_heading = 360 - (ball.heading() - 180)
                        ball.setheading(new_heading)
                        pass
                    elif 270 < ball.heading() < 360:
                        new_heading = 180 + (360 - ball.heading())
                        ball.setheading(new_heading)
                        pass


if __name__ == "__main__":
    main()

screen.exitonclick()
