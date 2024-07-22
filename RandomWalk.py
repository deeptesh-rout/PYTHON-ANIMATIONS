import turtle
import random

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)
t.pensize(2)

colors = ['red', 'yellow', 'blue', 'green', 'orange', 'purple']

for i in range(200):
    t.pencolor(random.choice(colors))
    t.forward(random.randint(20, 50))
    t.right(random.randint(0, 360))

turtle.hideturtle()
