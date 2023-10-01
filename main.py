from turtle import *

def circle_set(size):
    pensize(2)
    speed(20)
    color("navy")
    circle(size)

def big_circle():
    for i in range(8):
        circle_set(i * 10)

for i in range(4):
    big_circle()
    left(90)

speed(20)
hideturtle()
exitonclick()