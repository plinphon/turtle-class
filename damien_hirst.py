import colorgram
from turtle import Turtle
from random import random

def convert(color):
    red = color.rgb[0]/255
    green = color.rgb[1]/255
    blue = color.rgb[2]/255
    return red,green,blue

t = Turtle()

colors = colorgram.extract('color.png',28)
colors.pop(0)
colors.pop(0)
colors.pop(1)

print(colors)

num=0
for i in range(5):
    t.penup()
    t.home()
    t.right(90)
    t.forward((i)*50)
    t.left(90)
    t.color(convert(colors[num]))
    t.pendown()
    t.dot(30)
    num+=1
    for u in range(4):
        t.penup()
        t.forward(50)
        t.color(convert(colors[num]))
        t.pendown()
        t.dot(30)
        num+=1

t.screen.mainloop()