from turtle import Screen
from snake import Snake

snake = Snake()
screen = Screen()
screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game!")
screen.tracer(0)
game_is_on = True


def main():
    snake.starting_body()
    while game_is_on:
        snake.move()


if __name__ == "__main__":
    main()


screen.exitonclick()
