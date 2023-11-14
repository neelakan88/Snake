from turtle import Turtle
from random import randint

class Food(Turtle):
    #render itself as a small circle on the screen
    #every time snake touches food, it moves to a new random location
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.up()
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.color("blue")
        x = randint(-280, 280)
        y = randint(-280, 280)
        self.goto(x, y)
        self.refresh()

    def refresh(self):
        x = randint(-280, 280)
        y = randint(-280, 280)
        self.goto(x, y)