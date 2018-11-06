import turtle
mypen = turtle.Turtle()

mypen.color("red", "yellow")
mypen.begin_fill()
for _ in range(6):
    mypen.circle(60, steps=5)
    mypen.left(60)
mypen.end_fill()
turtle.done()