import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)
t.pensize(2)

colors = ['red', 'yellow', 'blue', 'green', 'orange', 'purple']

def draw_circle(radius):
    for _ in range(36):
        t.pencolor(colors[_ % 6])
        t.circle(radius)
        t.right(10)

draw_circle(100)

turtle.hideturtle()
