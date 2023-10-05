from turtle import Turtle
import random

t = Turtle()

steps = int(random.random() * 100)
lis = [0,90,180,270]

while True:
    t.fd(steps)
    t.rt(random.choice(lis))
    red = random.random()
    green = random.random()
    blue = random.random()
    t.color(red, green, blue)


