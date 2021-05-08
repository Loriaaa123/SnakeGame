from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize()
        self.color("red")
        self.speed("fastest")
        self.new_food()

    def new_food(self):
        new_x = random.randint(-270, 270)
        new_y = random.randint(-270, 270)
        self.goto(new_x, new_y)


