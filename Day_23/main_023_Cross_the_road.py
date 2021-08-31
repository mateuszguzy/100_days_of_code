# TODO-50: When car hits turtle game is over, turtle should be checked each time is distance to every present car
#  is not too close
# TODO-60: When game is over score is reset and starts from beginning

import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
screen.onkey(player.move, "Up")
level = Scoreboard()
cars = list()
create_car = 0
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    create_car = random.randint(0, 2)
    if create_car == 1:
        car = CarManager()
        car.create()
        cars.append(car)

    for car in cars:
        car.move(level=level.level)
        if car.car_body[1].xcor() <= -310:
            cars.remove(car)
            car.hideturtle()
            # print("DELETED")
        for piece in car.car_body:
            # print(f"CAR X: {piece.xcor()}, Y: {piece.ycor()}")
            # print(f"PLAYER X: {player.xcor()}, Y: {player.ycor()}")

            # if -15 <= int(piece.xcor()) <= 15:
            #     print(piece.turtlesize())
            #     # print(f"CAR X: {piece.xcor()}, Y: {piece.ycor()}")
            #     # print(f"PLAYER X: {int(player.xcor())}, Y: {player.ycor()}")
            #     # if player.ycor() - 10 < int(piece.ycor()) < player.ycor() + 10:
            #     if piece.ycor() - 20 <= player.ycor() <= piece.ycor() + 20:
            if piece.distance(player) <= 15:

                print("HIT")
                level.game_over()
                game_is_on = False

    if player.ycor() == 280:
        level.level_up()
        player.new_level()





screen.exitonclick()

