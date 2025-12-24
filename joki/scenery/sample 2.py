import turtle

# Create a screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle
t = turtle.Turtle()
t.speed(0)  # Set the fastest drawing speed

# Define the colors for the moon gradient
moon_colors = ["#ffffff", "#f0f0f0", "#d9d9d9", "#bfbfbf", "#a6a6a6", "#8c8c8c", "#737373", "#595959", "#404040", "#262626"]

# Set the starting position and size of the moon
x, y = -100, 0
moon_radius = 150

# Draw the moon with gradient and texture
t.penup()
t.goto(x, y - moon_radius)
t.pendown()
for color in moon_colors:
    t.fillcolor(color)
    t.begin_fill()
    t.circle(moon_radius, extent=180)
    t.end_fill()
    moon_radius -= 10

# Hide the turtle and keep the window open
t.hideturtle()
screen.mainloop()
