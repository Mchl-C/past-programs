from turtle import *

screen = Screen()
screen.tracer(False)

screen.setup(width = 500, height = 500)
WIDTH, HEIGHT = screen.window_width(), screen.window_height()

turtle = Turtle()
turtle.color("Black")
font = ("Helvetica", 84, "bold")

#---------------------------------------------------------------------#
turtle.penup()
turtle.goto(-150, -50)
turtle.pendown()

turtle.fillcolor("Black")
turtle.begin_fill()
turtle.fd(90)
turtle.left(120)
turtle.fd(60)
turtle.left(84)
turtle.fd(80)
turtle.end_fill()

#--------------------------------------------------------------------#
turtle.penup()
turtle.goto(-25, -50)
turtle.setheading(0)
turtle.pendown()

turtle.fillcolor("Black")
turtle.begin_fill()
turtle.fd(90)
turtle.left(120)
turtle.fd(130)
turtle.left(84)
turtle.fd(80)
turtle.end_fill()

#--------------------------------------------------------------------#
turtle.penup()
turtle.goto(100, -50)
turtle.setheading(0)
turtle.pendown()

turtle.fillcolor("Black")
turtle.begin_fill()
turtle.fd(90)
turtle.left(120)
turtle.fd(200)
turtle.left(84)
turtle.fd(80)
turtle.end_fill()

turtle.goto(-170,-160)
turtle.write("adidas", font = font)
screen.exitonclick()
