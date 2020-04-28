from turtle import Turtle, Screen, done
import random

screen = Screen()
t = Turtle(shape="turtle")
t.penup()
t.speed("fastest")

screen.screensize(200, 200)
for _ in range(5):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    t.goto(x, y)
    t.dot(20, 'blue')

x = -200
y = -200
t.goto(x, y)

def fd():
    t.forward(20)

def left():
    t.left(10)

def right():
    t.right(10)

def remove():
    t.dot(40, 'white')

screen.onkeypress(fd, 'Up')
screen.onkeypress(left, 'Left')
screen.onkeypress(right, 'Right')
screen.onkey(remove, 'space')
screen.listen()
done()