import turtle

color_list = ['red','blue','green','gray','white','orange','brown','purple','black']
color_num = 0

turtle.title("Paint")
size = 2

X_list = []
turtle.pensize(1)

def drag(x,y):
    turtle.ondrag(None)
    turtle.setheading(turtle.towards(x, y))
    turtle.goto(x, y)
    turtle.ondrag(drag)

def size_up():
    global size
    turtle.pensize(size)
    size += 1

def size_down():
    global size
    size -= 1
    if size <= 1:
        size = 1
    else:
        turtle.pensize(size)

def delete(): 
    turtle.clear()

def penup():
    turtle.penup()

def pendown():
    turtle.pendown()
    
def colors(x,y):
    global color_num
    if y <= color_y and y >= color_y - 20:
        for z in range(len(color_list)):
            if x >= X_list[z]:
                color_num += 1
                
        turtle.color(color_list[int(color_num) - 1])
        color_num = 0
        
turtle.speed(0)
win = turtle.Screen()
max_x, max_y = win.screensize()

color_x = -200
color_y = max_y - 20

icons = turtle.Pen()
icons.speed(0)
icons.penup()
icons.setpos(color_x,color_y)
icons.setheading(0)
icons.pendown()

for i in range(len(color_list)):
    icons.fillcolor(color_list[i])
    icons.begin_fill()
    
    X_list.append(icons.pos()[0])
    for x in range(4):
        icons.forward(20)
        icons.right(90)

    icons.penup()
    icons.setheading(0)
    icons.forward(40)
    icons.pendown()
    
    icons.end_fill()

icons.penup()
icons.pensize(3)   
icons.goto(color_x - 10,color_y + 10)
icons.pendown()
icons.goto(color_x - 10,color_y - 40)
icons.setheading(0) 
icons.forward(max_x - 40)
icons.setheading(90)
icons.forward(50)
icons.left(90)
icons.forward(max_x - 40)
icons.hideturtle()

turtle.penup()
turtle.goto(0,0)
turtle.setheading(90)
turtle.pendown()

win.listen()

turtle.onscreenclick(colors)
turtle.ondrag(drag)
turtle.onkey(size_up,'Up')
turtle.onkey(size_down,'Down')
turtle.onkey(delete,'c')
turtle.onkey(penup,'u')
turtle.onkey(pendown,'d')

win.mainloop()
