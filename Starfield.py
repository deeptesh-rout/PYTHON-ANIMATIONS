import turtle
import random

# Set up the screen
win = turtle.Screen()
win.bgcolor("black")
win.title("Starfield Animation")
win.tracer(0)

# Create a turtle for drawing stars
star = turtle.Turtle()
star.hideturtle()
star.speed(0)

# Function to draw a star
def draw_star(x, y, size, color):
    star.penup()
    star.goto(x, y)
    star.pendown()
    star.color(color)
    star.begin_fill()
    for _ in range(5):
        star.forward(size)
        star.right(144)
    star.end_fill()

# Create a field of stars
stars = []
for _ in range(100):
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    size = random.randint(5, 15)
    color = random.choice(['white', 'yellow', 'blue', 'green', 'red'])
    stars.append((x, y, size, color))

while True:
    win.update()
    star.clear()
    for s in stars:
        draw_star(*s)
    # Move stars downwards
    stars = [(x, y-2, size, color) if y > -300 else (x, 300, size, color) for x, y, size, color in stars]
