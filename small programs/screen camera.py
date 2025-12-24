import curses

curses.start_color()
curses.use_default_colors()
curses.init_pair(1,84,0)

run = True
while run:
    screen = curses.initscr()
    y_max, x_max = curses.getmaxyx()
    
