import turtle as t
import random

t.colormode(255)

t.speed('fastest')
t.hideturtle()

for i in range(-5, 5):
    for j in range(-5, 5):
        t.penup()
        t.goto(j*50, i*50)
        t.pendown()
        t.dot(20, (random.randint(0, 255) for x in range(3)))

screen = t.Screen()
screen.exitonclick()
