# Turtle - Block Game

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.tracer(0)
player = Player()
screen.update()

screen.setup(width=600, height=600)
screen.listen()
screen.onkey(player.up,"Up")
screen.onkey(player.down,"Down")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()
    
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False
            
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()
            
screen.exitonclick()