#####Turtle Intro######

import turtle as t
import random

tim = t.Turtle()
tim.shape("turtle")
tim.color("red")
colours = [
    "CornflowerBlue",
    "DarkOrchid",
    "IndianRed",
    "DeepSkyBlue",
    "LightSeaGreen",
    "wheat",
    "SlateGray",
    "SeaGreen",
]
t.colormode(255)

# tim.forward(100)
# tim.backward(200)
# tim.right(90)
# tim.left(180)
# tim.setheading(0)


######## Challenge 1 - Draw a Square ############
# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)


######## Challenge 2 - Draw a Dashed Line ############
# for _ in range (10):
#     tim.color("blue")
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


######## Challenge 3 - Drawing different shapes ############

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)

# for shapes_sides in range(3,11):
#     draw_shape(shapes_sides)

######## Challenge 4 - Generate a random walk ############
# directions = [0, 90, 180, 270]
# tim.pensize(15)
tim.speed("fastest")


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour


# for _ in range(200):
#     tim.color(random.choice(colours))
#     tim.color(random_colour())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

######## Challenge 5 - Generate a spiral graph ############
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_colour())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)
