from turtle import Turtle
import random

score=0

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("red")
        self.speed("fastest")
        self.nom_nom()

    def nom_nom(self):
        x_axis = random.randint(-270, 270)
        y_axis = random.randint(-270, 270)
        self.goto(x_axis, y_axis)
        global score
        score+=1

