import turtle
mypen = turtle.Turtle()

mypen.color("red", "yellow")
mypen.shape("turtle")
mypen.begin_fill()
mypen.speed(1)
for _ in range(50):
    mypen.forward(200)
    mypen.left(170)
mypen.end_fill()
turtle.done()