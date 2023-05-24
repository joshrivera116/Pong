from turtle import Turtle
from random import choice

COORD = [10, -10]


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.shapesize(1, 1)
        self.penup()
        self.x_move = choice(COORD)
        self.y_move = choice(COORD)
        self.timesleep = 0.09

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1
        if self.timesleep > 0.03:
            self.timesleep -= 0.01

    def reset_pos(self):
        self.home()
        self.paddle_bounce()
        self.timesleep = 0.09

