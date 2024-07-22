import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)

colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']

for i in range(300):
    t.pencolor(colors[i % 6])
    t.forward(i * 2)
    t.right(121)

turtle.hideturtle()
