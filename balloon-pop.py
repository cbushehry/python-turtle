from turtle import *

hideturtle()
diameter = 200
pop_diameter = 300

# draws the balloon on screen
def draw_balloon():
    color("blue")
    dot(diameter)

# called when we press the Up arrow key
def inflate_balloon():
    global diameter
    diameter += 10  # Increment the diameter
    draw_balloon()

    # are we ready to pop?
    if diameter >= pop_diameter:
        clear()
        diameter = 200
        # Updated to write "POP!" in a larger font
        write("POP!", font=("Arial", 40, "bold"))  # Adjust font name, size, and type as needed

draw_balloon()

# Setup screen and key bindings
screen = Screen()
screen.onkey(inflate_balloon, "Up")
screen.listen()
done()
