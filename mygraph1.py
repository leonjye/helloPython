import turtle
screen = turtle.Screen()
star = turtle.Turtle()
star.color('red', 'yellow')
star.begin_fill()
star.pensize(50)
while True:
    star.forward(200)
    star.left(170)
    print(star.pos())
    if abs(star.pos()) < 1:
        break
star.end_fill()
screen.exitonclick() 