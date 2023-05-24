from turtle import Turtle
COLOR = 'white'


class Paddle(Turtle):

    def __init__(self, xcor, ycor):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(5, 1)
        self.goto(xcor, ycor)
        self.color('white')

    def up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        self.goto(self.xcor(), self.ycor() - 20)


