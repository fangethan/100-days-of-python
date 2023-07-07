#####Turtle Intro######

import turtle as t

tim = t.Turtle()
tim.shape("turtle")
tim.color("red")
# tim.forward(100)
# tim.backward(200)
# tim.right(90)
# tim.left(180)
# tim.setheading(0)


######## Challenge 1 - Draw a Square ############
for _ in range(4):
    tim.forward(100)
    tim.left(90)

