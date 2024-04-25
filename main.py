from turtle import Turtle,Screen
from random import choice

timmy = Turtle()
screen = Screen()

screen.colormode(255)

color_list = [(239, 229, 213), (203, 161, 18), (217, 155, 70), (242, 230, 236), (49, 104, 158), (207, 151, 182), (226, 207, 135), (187, 66, 39), (229, 234, 242), (162, 29, 36), (29, 28, 69), (232, 240, 234), (36, 79, 40), (28, 67, 32), (143, 161, 183), (168, 43, 50), (76, 104, 77), (151, 30, 27), (150, 169, 152), (193, 93, 76)]
timmy.speed("fastest")
timmy.hideturtle()
def spot_generation():
    """to generate random color dots for the dot painting """
    for i in range(10):
        timmy.color(choice(color_list))
        timmy.dot(20)
        timmy.penup()
        timmy.fd(50)
        timmy.pendown()

timmy.setheading(225)
timmy.penup()
timmy.forward(300)
timmy.setheading(0)

for i in range(10):
    spot_generation() #calling function
    timmy.setheading(90)
    timmy.penup()
    timmy.fd(50)
    timmy.setheading(180)
    timmy.fd(500)
    timmy.setheading(0)

screen.exitonclick()