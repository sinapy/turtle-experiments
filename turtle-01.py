import turtle
import numpy as np

t = turtle.Turtle()

t.speed(0)

def move(distance):
    t.goto(0,0)
    t.forward(distance)
    t.right(1)

for i in range(120):
    move(i+10)

for i in range(120, 0, -1):
    move(i+10)

for j in range(3):
    for i in range(30):
        move((i+10)/3)

    for i in range(30, 0, -1):
        move((i+10)/3)

