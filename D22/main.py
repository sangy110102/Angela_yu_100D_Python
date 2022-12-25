#pong game

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
ball = Ball()
scoreboard = ScoreBoard()
paddle_r = Paddle(350,0)
paddle_l = Paddle(-350,0)
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(800,600)
screen.tracer(0)

screen.listen()
screen.onkey(paddle_r.up,"Up")
screen.onkey(paddle_r.down,"Down")
screen.onkey(paddle_l.up,"w")
screen.onkey(paddle_l.down,"s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    # R Side
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    
    # L Side    
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
    
    # if ball.xcor() > 380 or ball.xcor() < -380:
    #     game_is_on = False


screen.exitonclick()