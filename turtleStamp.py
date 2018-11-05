# turtleStamp.py
import turtle
screen = turtle.Screen()
screen.setup(600,600)
screen.bgcolor("lightgreen")
myStamp = turtle.Turtle(visible=False)
#myStamp.shape("turtle")
myStamp.color("blue")
# myStamp.speed(8)
myStamp.penup() # Do not draw the path
stepLen = 20
for i in range(31):
    myStamp.stamp() # Leave an impression on the canvas
    stepLen = stepLen + 3 # Increase the step length on every iteration
    myStamp.forward(stepLen) # Move along
    myStamp.right(24) # and turn
myStamp.penup() # Do not draw the path
myStamp.goto(0, 260) # Move
myStamp.color('red')
myStamp.write('Done!', align='center', font=('Arial', 20, 'bold'))
screen.exitonclick()