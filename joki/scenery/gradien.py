from turtle import *

COLOR = (0, 0.02745, 0.10196)  # (0, 7, 26)
TARGET = (0, 0.18823, 0.36862) # (0, 48, 94)

COLOR2 = (0.00784, 0.15294, 0.32549)  # (2, 39, 83)
TARGET2 = (0.98824, 0.76471, 0.54902) # (252, 195, 140)

screen = Screen()
screen.tracer(False)

screen.setup(width = 800, height = 600)
WIDTH, HEIGHT = screen.window_width(), screen.window_height()

deltas  = [(hue - COLOR[index]) / HEIGHT for index, hue in enumerate(TARGET)]
trans   = [(hue - TARGET[index]) / HEIGHT for index, hue in enumerate(COLOR2)]
deltas2 = [(hue - COLOR2[index]) / HEIGHT for index, hue in enumerate(TARGET2)]

turtle = Turtle()
turtle.color(COLOR)

turtle.penup()
turtle.goto(-WIDTH/2, HEIGHT/2)
turtle.pendown()
#turtle.speed(0)

direction = 1

for distance, y in enumerate(range(HEIGHT//2, HEIGHT//6, -1)):
    turtle.forward(WIDTH * direction)
    turtle.color([COLOR[i] + delta * 3.2 * distance for i, delta in enumerate(deltas)])
    turtle.sety(y)
    
    direction *= -1

for distance, y in enumerate(range(HEIGHT//6, 0, -1)):
    turtle.forward(WIDTH * direction)
    turtle.color([TARGET[i] + delta * 7 * distance for i, delta in enumerate(trans)])
    turtle.sety(y)
    
    direction *= -1

for distance, y in enumerate(range(0, -HEIGHT//2, -1)):
    turtle.forward(WIDTH * direction)
    turtle.color([COLOR2[i] + delta * 2 * distance for i, delta in enumerate(deltas2)])
    turtle.sety(y)
    
    direction *= -1

screen.tracer(True)
screen.exitonclick()
