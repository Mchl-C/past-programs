import random
import turtle
import math

lst = ['Sin Theta','Da ren','Mikael','Se Grace']
x,y = 0,0
degree_turn = 360 / len(lst)
degree = 90

def triggered(a,b):
    tap.clear()

    arrow = turtle.Pen()
    arrow.speed(0)
    arrow.penup()
    arrow.setpos(0,-5)
    arrow.pendown()

    x2,y2 = 0,0
    cdg = 90

    arrow.width(3)
    movement = random.randint(12, 23)

    for i in range(144):
        arrow.hideturtle()
        arrow.penup()
        arrow.setpos(x2,y2)
        arrow.setheading(cdg)
        arrow.pendown()
        arrow.forward(100)
        cdg -= movement
        arrow.showturtle()
        arrow.clear()

    arrow.setpos(x2,y2)
    arrow.setheading(cdg + movement)
    arrow.forward(100)

    res = int(abs(cdg) // degree_turn) % len(lst)
    print(res)
    print("result is : %s"%lst[res])

    turtle.setpos(-120,-200)
    turtle.write("The result is : %s"%(lst[res]),font = ("Times New Roman",20,"normal"))

scr = turtle.Screen()
scr.bgcolor("#85a54a")
scr.title("Fortune Wheel")

turtle.speed(0)
turtle.penup()
turtle.hideturtle()
turtle.setpos(-165,200)
turtle.write("Fortune Wheel",font = ("Verdana",30,"bold"))

p = turtle.Pen()
p.speed(0)
p.penup()
p.setpos(0,-150)
p.pendown()

p.width(3)
p.color('#228B22')
p.fillcolor('#365f0c')
p.begin_fill()
p.circle(150)
p.end_fill()

p.width(1)
p.color('white')

for i in range(len(lst)):
    p.penup()
    p.setpos(x,y)
    p.setheading(degree)
    p.pendown()
    p.forward(150)
    degree += degree_turn

p.hideturtle()
p.penup()

tap = turtle.Pen()
tap.penup()
tap.hideturtle()
tap.setpos(-100,-200)
tap.write("Tap anywhere to spin",font = ("Verdana",15,"normal"))

turtle.listen()
turtle.onscreenclick(triggered)

