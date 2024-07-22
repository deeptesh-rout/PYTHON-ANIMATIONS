import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)
t.pensize(2)

colors = ['red', 'yellow', 'blue', 'green', 'orange', 'purple']

for i in range(36):
    t.pencolor(colors[i % 6])
    for _ in range(4):
        t.forward(100 + i * 5)
        t.right(90)
    t.right(10)

turtle.hideturtle()
