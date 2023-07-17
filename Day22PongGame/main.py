from turtle import Screen, Turtle
import time
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Ping Pong Game")
screen.tracer(0)

paddle_left = Paddle((-350, 0))
paddle_right = Paddle((350, 0))


screen.listen()
screen.onkey(paddle_left.go_up, "w")
screen.onkey(paddle_left.go_down, "s")

screen.onkey(paddle_right.go_up, "Up")
screen.onkey(paddle_right.go_down, "Down")


game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
