from turtle import Turtle
from random import random

t = Turtle()

angle = int(input('angle : '))
turn = ((angle- 2) * 180)/angle

for i in range(angle):
    t.fd(50)
    t.right(180-turn)
    red = random()
    green = random()
    blue = random()
    t.color(red, green, blue)

t.screen.mainloop()