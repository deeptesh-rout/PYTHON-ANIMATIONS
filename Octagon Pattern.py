import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)
t.pensize(2)

colors = ['red', 'yellow', 'blue', 'green', 'orange', 'purple']

def draw_octagon(size):
    for _ in range(8):
        t.forward(size)
        t.right(45)

for i in range(36):
    t.pencolor(colors[i % 6])
    draw_octagon(100)
    t.right(10)

turtle.hideturtle()
