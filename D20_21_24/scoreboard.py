from turtle import Turtle
import os

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.score = 0
        with open(os.path.abspath("D20_21_24/high_score.txt")) as data:
            self.high_score = int(data.read())
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Scoreboard: {self.high_score}",align="center",font=("Arial", 20, "normal"))
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(os.path.abspath("D20_21_24/high_score.txt"),"w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
        
    
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over",align="center",font=("Arial", 24, "normal"))
        
        
    
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()