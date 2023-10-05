from turtle import Turtle
import random

t = Turtle()

while True:
    t.circle(100)
    t.rt(10)
    red = random.random()
    green = random.random()
    blue = random.random()
    t.color(red, green, blue)

