from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
paddle1 = Paddle(350, 0)
paddle2 = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle1.down, 'Down')
screen.onkey(paddle1.up, 'Up')
screen.onkey(paddle2.down, 's')
screen.onkey(paddle2.up, 'w')
playing = True
line = Turtle()
line.pencolor('white')
line.hideturtle()
line.setheading(90)
line.penup()
line.goto(0, -400)

for i in range(20):
    line.pendown()
    line.forward(20)
    line.penup()
    line.forward(20)

while playing:
    screen.update()
    time.sleep(ball.timesleep)

    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    if ball.distance(paddle1) < 60 and ball.xcor() > 325:
        ball.paddle_bounce()

    elif ball.distance(paddle2) < 60 and ball.xcor() < -325:
        ball.paddle_bounce()
    elif ball.xcor() > 400:
        ball.reset_pos()
        paddle1.goto(350, 0)
        paddle2.goto(-350, 0)
        time.sleep(2)
        scoreboard.l_point()
    elif ball.xcor() < -400:
        ball.reset_pos()
        paddle1.goto(350, 0)
        paddle2.goto(-350, 0)
        time.sleep(2)
        scoreboard.r_point()
    if scoreboard.l_score > 6:
        scoreboard.l_wins()
        playing = False
    elif scoreboard.r_score > 6:
        scoreboard.r_wins()
        playing = False

screen.exitonclick()
