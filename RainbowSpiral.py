import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

for x in range(360):
    t.pencolor(colors[x % 6])
    t.width(x // 100 + 1)
    t.forward(x)
    t.right(45)

turtle.hideturtle()
