import turtle
import time
screen = turtle.Screen()
screen.setup(600,600)
screen.bgcolor("lightgreen")
mpen = turtle.Turtle()
mpen.pensize(5)
mpen.pencolor("yellow")
mpen.fillcolor("red")
mpen.begin_fill()

for _ in range(5):
    mpen.forward(200)
    mpen.right(144)
mpen.end_fill()
time.sleep(2)

mpen.penup()
mpen.goto(-150,-120)
mpen.color("violet")
mpen.write("Done", font=('Arial', 40, 'normal'))
time.sleep(1)
turtle.done()
