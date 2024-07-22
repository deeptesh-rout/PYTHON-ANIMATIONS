import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)
t.pensize(2)

colors = ['red', 'yellow', 'blue', 'green', 'orange', 'purple']

def draw_petal():
    for _ in range(2):
        t.circle(100, 60)
        t.left(120)
        t.circle(100, 60)
        t.left(120)

for i in range(36):
    t.pencolor(colors[i % 6])
    draw_petal()
    t.right(10)

turtle.hideturtle()
