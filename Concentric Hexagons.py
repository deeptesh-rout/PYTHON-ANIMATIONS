import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)
t.pensize(2)

colors = ['red', 'yellow', 'blue', 'green', 'orange', 'purple']

def draw_hexagon(size):
    for _ in range(6):
        t.forward(size)
        t.right(60)

for i in range(1, 13):
    t.pencolor(colors[i % 6])
    draw_hexagon(i * 20)
    t.right(5)

turtle.hideturtle()
