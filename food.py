from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("magenta")
        self.penup()
        self.refresh()

    def refresh(self):
        x = random.randint(-260, 260)
        y = random.randint(-260, 260)
        self.speed("fastest")
        self.goto(x=x, y=y)
