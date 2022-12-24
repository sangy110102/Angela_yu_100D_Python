# Turtle Race

from turtle import Turtle,Screen
import random
is_race_on = False
screen = Screen()
screen.title("Turtle Race")
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make Your Bet",prompt="Which turtle win the race? Enter a color : ").lower()
colors = ["red","orange","yellow","green","blue","purple"]
y_positions = [ -70, -40, -10, 20, 50, 80 ]
all_turtles = []


for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        turtle.setx(turtle.xcor() + random.randint(1, 10))
        if turtle.xcor() >= 230:
            is_race_on = False
            winner_color = turtle.pencolor()


print(f"The winner was {winner_color}.")
if user_bet.lower() == winner_color.lower():
    print(f"You won the bet!")
else:
    print(f"Sorry, you lost.")

screen.exitonclick()