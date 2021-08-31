from turtle import Screen
from food import Food
from scoreboard import Scoreboard
from snake import Snake

WALL_BOUNDARY = 295

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen = Screen()
screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")
screen.setup(width=580, height=580)
screen.bgcolor("black")
screen.title("Snake game!")
screen.tracer(0)
game_is_on = True


def main():
    global game_is_on
    snake.starting_body()
    scoreboard.write(arg=f"Score: {scoreboard.score} High score: {scoreboard.high_score}", align="center", font=("Arial", 14, "normal"))
    while game_is_on:
        snake.move()

        # detect collision with food
        if snake.snake_body[0].distance(food) < 15:
            food.refresh()
            scoreboard.increase_score()
            scoreboard.update_score()
            snake.grow()

        # detect collision with wall
        if snake.snake_body[0].xcor() >= WALL_BOUNDARY or snake.snake_body[0].xcor() <= -WALL_BOUNDARY or \
                snake.snake_body[0].ycor() >= WALL_BOUNDARY or snake.snake_body[0].ycor() <= -WALL_BOUNDARY:
            scoreboard.reset()
            snake.reset()

        # detect collision with tail
        for piece in snake.snake_body[1:]:
            if snake.snake_body[0].distance(piece) < 10:
                scoreboard.reset()
                snake.reset()


if __name__ == "__main__":
    main()

screen.exitonclick()
