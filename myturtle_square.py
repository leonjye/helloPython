import turtle # Allows us to use turtles
screen = turtle.Screen() # Creates a playground for turtles
screen.setup(400, 400) # Set the size of the screen
screen.title('Turtle playground') # Set the title of the screen
screen.bgcolor('lightyellow') # Set the background color of the screen
# Draw a square
square = turtle.Turtle() # Create a turtle, assign to 'square'

square.color('hotpink') # Set the color of the turtle
for i in range(4): # Draw a square
    square.forward(100)
    square.left(90)
turtle.done()
#screen.exitonclick() # Wait for user to close the screen