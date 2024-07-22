import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.speed(0)
t.pensize(2)
t.color("green")

def draw_branch(branch_length):
    if branch_length > 5:
        t.forward(branch_length)
        t.right(20)
        draw_branch(branch_length - 15)
        t.left(40)
        draw_branch(branch_length - 15)
        t.right(20)
        t.backward(branch_length)

t.left(90)
t.up()
t.backward(100)
t.down()
draw_branch(100)

turtle.hideturtle()
