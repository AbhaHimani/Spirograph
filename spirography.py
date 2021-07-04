import turtle as t
from turtle import Screen
import random
t.colormode(255)
tim = t.Turtle()
def random_color():
    r= random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color = (r, g, b)
    return random_color

tim.speed("fastest")

def make_circle():

    for _ in range(36):
        tim.color(random_color())
        tim.circle(100)
        current_heading = tim.heading()
        tim.setheading(current_heading + 10)
        tim.circle(100)
make_circle()
screen= t.Screen()
screen.exitonclick()