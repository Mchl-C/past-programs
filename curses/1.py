import curses
from curses.textpad import Textbox, rectangle

screen = curses.initscr()
run = True
c = ' '

red = False;
yellow = False;
green = False;

curses.start_color()
curses.use_default_colors()
curses.init_pair(1,curses.COLOR_RED,curses.COLOR_RED)
curses.init_pair(2,curses.COLOR_YELLOW,curses.COLOR_YELLOW)
curses.init_pair(3,curses.COLOR_GREEN,curses.COLOR_GREEN)

while run:
    curses.echo(False)
    screen.nodelay(True)
    screen.clear()
    screen.border()
    
    for x in range(4):
        screen.addstr(6 + (x*6),16,'_')
        for i in range(14):
            screen.addstr('_')

    for i in range(18):
        screen.addstr(7+i,15,'|')
        screen.addstr(7+i,30,'|')

    for i in range(14):
        screen.addstr(25 + i,22,'|')
        screen.addstr(25 + i,23,'|')

    try:
        c = chr(screen.getch())
    except:
        c = c

    if(c == 'a'):
        for i in range(4):
            for x in range(12):
                screen.addstr(8+i,17+x,' ',curses.color_pair(1))

    elif(c == 'b'):
        for i in range(4):
            for x in range(12):
                screen.addstr(14+i,17+x,' ',curses.color_pair(2))

    elif(c == 'c'):
        for i in range(4):
            for x in range(12):
                screen.addstr(20+i,17+x,' ',curses.color_pair(3))
                
    screen.refresh()
