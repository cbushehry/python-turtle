from turtle import *

# Store the screen in a variable to reuse
screen = Screen()

# Setup the screen for the live coding
screen.setup(800, 500)

# Set speed to 0 so the animation is instant
speed(0)

# Set the background color to BLACK
screen.bgcolor("black")

# Create the ORANGE planet
color("orange")
begin_fill()
circle(60)
end_fill()

# Move forwards
penup()
forward(100)
pendown()

# Create the GREY planet
color("grey")
begin_fill()
circle(20)
end_fill()

# Move forwards
penup()
forward(80)
pendown()

# Create the RED planet
color("red")
begin_fill()
circle(40)
end_fill()

# Move forwards
penup()
forward(90)
pendown()

# Create the GREEN planet
color("green")
begin_fill()
circle(30)
end_fill()

# Use the same screen variable to call exitonclick
screen.exitonclick()