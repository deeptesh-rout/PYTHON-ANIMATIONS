import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)
t.pensize(2)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

for i in range(180):
    t.pencolor(colors[i % 6])
    t.forward(i * 2)
    t.right(90)
    t.forward(i * 2)
    t.right(90)

turtle.hideturtle()
