import turtle  # Import the turtle module

# Create a screen object to control the window
screen = turtle.Screen()

# Create a turtle object
pen = turtle.Turtle()

# Set the number of steps to move forward
steps = 100

# Draw the first side
pen.forward(steps)  # Corrected the typo from 'foward' to 'forward'
pen.left(120)

# Draw the second side
pen.forward(steps)
pen.left(120)

# Draw the third side
pen.forward(steps)
pen.left(120)

# Complete the drawing and keep the window open
turtle.done()
