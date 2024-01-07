import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
cars = CarManager()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
counter = 0
while game_is_on:
    if counter % 6 == 0:
        cars.create_car()
    time.sleep(0.1)
    screen.update()

    if player.level_complete():
        player.start_position()
        scoreboard.level_up()
        cars.increase_speed()

    if player.is_colliding(cars.cars):
        game_is_on = False
        scoreboard.game_over()
    counter += 1
    cars.move_cars()

screen.exitonclick()
