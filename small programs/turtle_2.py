import turtle

t = turtle.Pen()
for i in range(3):
    t.fd(150)
    t.left(120)

t.setheading(270)
t.fillcolor("magenta")
t.begin_fill()

for i in range(3):
    t.fd(150)
    t.left(90)

t.end_fill()
