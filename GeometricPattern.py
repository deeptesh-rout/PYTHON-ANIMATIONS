import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)
t.pensize(2)

colors = ['red', 'yellow', 'blue', 'green', 'orange', 'purple']

for i in range(50):
    t.pencolor(colors[i % 6])
    t.forward(i * 10)
    t.right(144)

turtle.hideturtle()
