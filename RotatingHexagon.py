import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)
t.pensize(2)

colors = ['red', 'yellow', 'blue', 'green', 'orange', 'purple']

for i in range(72):
    t.pencolor(colors[i % 6])
    for _ in range(6):
        t.forward(100)
        t.right(60)
    t.right(5)

turtle.hideturtle()
