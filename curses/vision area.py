import curses

logo = ['o','i']

screen = curses.initscr()
y_max, x_max = screen.getmaxyx()
pad = curses.newpad(50, 50)

curses.start_color()
curses.use_default_colors()
curses.init_pair(1,84,0)

for i in range(5):
    pad.addstr(i,0,"123456789101112")

x = 14
y = 14

run = True
while run:
    screen.clear()

    screen.addstr(y,x,"P")
    screen.refresh()
    pad.refresh(0,0,0,0,3,3)    
    c = chr(screen.getch())
    if c == 'a':
        x -= 1
    elif c == 's':
        y += 1
    elif c == 'w':
        y -= 1
    elif c == 'd':
        x += 1


    
