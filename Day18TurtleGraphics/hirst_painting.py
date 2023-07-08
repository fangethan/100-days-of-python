import colorgram
import turtle as t
import random 

tim = t.Turtle()
tim.shape("turtle")
t.colormode(255)
tim.speed("fastest")

colors = colorgram.extract('image.jpeg', 30)

color_list = [] 

for color in colors:
    r = color.rgb.r 
    g = color.rgb.g  
    b = color.rgb.b  
    extracted_color = (r, g, b)  
    color_list.append(extracted_color)  

tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()