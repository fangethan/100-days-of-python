from turtle import Screen, Turtle
import time
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong Game")
screen.tracer(0)

paddle_left = Paddle((-350, 0))
paddle_right = Paddle((350, 0))

ball = Ball()

screen.listen()
screen.onkey(paddle_left.go_up, "w")
screen.onkey(paddle_left.go_down, "s")

screen.onkey(paddle_right.go_up, "Up")
screen.onkey(paddle_right.go_down, "Down")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (
        ball.distance(paddle_right) < 50
        and ball.xcor() > 320
        or ball.distance(paddle_left) < 50
        and ball.xcor() < -320
    ):
        ball.bounce_x()

screen.exitonclick()
