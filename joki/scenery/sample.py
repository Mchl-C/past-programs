from turtle import *
import random

#-------------------------------------------------------------------------#
# Variables
COLOR = (0, 0.02745, 0.10196)  # (0, 7, 26)
TARGET = (0, 0.18823, 0.36862) # (0, 48, 94)
COLOR2 = (0.00784, 0.15294, 0.32549)  # (2, 39, 83)
TARGET2 = (1.00000, 0.68627, 0.29020) # (255, 175, 74)
stars = (0.49803, 0.62745, 0.74901) # (127, 160, 191)
moon_shade = (0.64314, 0.61176, 0.58824) # (164, 156, 150)
moon_shade2 = (0.73333, 0.70588, 0.68235) # (187, 180, 174)

screen = Screen()
screen.tracer(False)

screen.setup(width = 800, height = 600)
WIDTH, HEIGHT = screen.window_width(), screen.window_height()

deltas  = [(hue - COLOR[index]) / HEIGHT for index, hue in enumerate(TARGET)]
trans   = [(hue - TARGET[index]) / HEIGHT for index, hue in enumerate(COLOR2)]
deltas2 = [(hue - COLOR2[index]) / HEIGHT for index, hue in enumerate(TARGET2)]

#------------------------------------------------------------------------#
# Set up
turtle = Turtle()
turtle.color(COLOR)
turtle.penup()
turtle.goto(-WIDTH/2, HEIGHT/2)
turtle.pendown()
#turtle.speed(0)

direction = 1

def draw_stars():
    size = random.randint(1,3)
    x = random.randint(-WIDTH//2, WIDTH//2)
    y = random.randint(0, HEIGHT//2)

    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    
    turtle.dot(size)
    turtle.penup()

#------------------------------------------------------------------------#
# Sky gradient
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

for distance, y in enumerate(range(0, -int(HEIGHT * 0.4), -1)):
    turtle.forward(WIDTH * direction)
    turtle.color([COLOR2[i] + delta * 2.5 * distance for i, delta in enumerate(deltas2)])
    turtle.sety(y)
    
    direction *= -1

y_pos = -0.3 * HEIGHT
turtle.goto(-WIDTH/2, y_pos)
turtle.color("Black")

direction = 1
for x in range(-WIDTH//2,WIDTH//2):
    turtle.setheading(270)
    y_pos += random.uniform(-3,3)
    turtle.fd(abs(y_pos) * direction)
    turtle.setx(x)

    direction *= -1

# Stars
for i in range(100):
    turtle.color(stars)
    draw_stars()

# Moon
turtle.goto(0.2 * WIDTH, HEIGHT // 4)
turtle.fillcolor("#d9d9d9")
turtle.begin_fill()
turtle.circle((HEIGHT//12))
turtle.end_fill()

'''
- crater klo mau nambah uncomment part ini ~
r = 30

for i in range(10):
    crater = random.randint(10,r)
    x_pos = int(random.uniform(0.2 * WIDTH + 2*r, 0.2 * WIDTH + 2*(HEIGHT // 12) - 2*r))
    y_pos = int(random.uniform(HEIGHT // 4 - (HEIGHT // 12) + 2*r, HEIGHT // 4 + HEIGHT // 12 - 2*r))
    turtle.goto(x_pos, y_pos)
    #print(x_pos, y_pos)
    
    turtle.fillcolor(moon_shade2)
    turtle.begin_fill()
    turtle.circle(crater)
    turtle.end_fill()

r = 20
for i in range(10):
    crater = random.randint(5,r)
    x_pos = int(random.uniform(0.2 * WIDTH + r, 0.2 * WIDTH + 2*(HEIGHT // 12) - r))
    y_pos = int(random.uniform(HEIGHT // 4 - (HEIGHT // 12) + r, HEIGHT // 4 + HEIGHT // 12 - r))
    turtle.goto(x_pos, y_pos)
    #print(x_pos, y_pos)
    
    turtle.fillcolor(moon_shade)
    turtle.begin_fill()
    turtle.circle(crater)
    turtle.end_fill()
'''

turtle.hideturtle()
screen.tracer(True)
screen.exitonclick()
