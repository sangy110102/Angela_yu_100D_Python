
from turtle import Turtle

starting_positions = [(0,0),(-20,0),(-40,0)]
move_distance = 20

class Snake:
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        
    def create_snake(self):
        for position in starting_positions:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
        
    def move(self):
        for seg_num in range(len(self.segments) - 1,0,-1):
            x = self.segments[seg_num - 1].xcor()
            y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x,y)
        self.segments[0].forward(move_distance)
        
    def up(self):
        if self.segments[0].heading != 270:
            self.segments[0].setheading(90)
        
    def down(self):
        if self.segments[0].heading != 90:
            self.segments[0].setheading(270)
        
    def left(self):
        if self.segments[0].heading != 0:
            self.segments[0].setheading(180)
        
    def right(self):
        if self.segments[0].heading != 180:
            self.segments[0].setheading(0)