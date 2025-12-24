import curses

market = curses.initscr()
curses.start_color()
curses.use_default_colors()
curses.init_pair(1,180,0)
curses.init_pair(2,130,0)
curses.init_pair(3,110,0)

open_market = True
y_width, x_width = market.getmaxyx()
y_gap, x_gap = int(y_width/10), int(x_width/10)
description = ""

while open_market:
    #Market borders
    market.clear()
    market.addstr(0,int(x_width/2) - 20," __  __     __     __    _  _   ___  ___",curses.color_pair(2))
    market.addstr(1,int(x_width/2) - 20,"|  \/  |   /[]\   |[]|  | |/ / |      | ",curses.color_pair(2))
    market.addstr(2,int(x_width/2) - 20,"| |\/| |  / __ \  ||\\\  |   <  |---   | ",curses.color_pair(2))
    market.addstr(3,int(x_width/2) - 20,"|_|  |_| /_/  \_\ || \\\ |_|\_\ |___   | ",curses.color_pair(2))
    for i in range(x_width - 2*x_gap + 1):
        market.addstr(y_gap,i + x_gap,'_',curses.color_pair(1))
        market.addstr(y_width - y_gap,i + x_gap,'_',curses.color_pair(1))
        
    for i in range(1,y_width - 2*y_gap + 1,1):
        market.addstr(i + y_gap,x_gap,'|',curses.color_pair(1))
        market.addstr(i + y_gap,x_width - x_gap,'|',curses.color_pair(1))

    for i in range(x_width - 2*x_gap + 1):
        market.addstr(y_width - 2*y_gap,x_gap + i,'_',curses.color_pair(1))
        
    #Item list
    market.addstr(y_gap + 2, x_gap + 3,"coins : 100",curses.color_pair(3))
    market.addstr(y_gap + 3, x_width - x_gap - 11,"Price",curses.color_pair(3))
    
    item_list = ["Healt Pot","Short Sword","Wooden Buckler"]
    Items = {
        "Healt Pot" : 20,
        "Short Sword" : 30,
        "Wooden Buckler" : 40
    }
    Description = {
        "Healt Pot" : "Restore 60 HP",
        "Short Sword" : "+5 Attack Damage",
        "Wooden Buckler" : "+2 Def"
    }
    
    for i in range(len(Items)):
        market.addstr(y_gap + 5 + (i*2),x_gap + 3,(str(i+1) + '. ' + item_list[i]),curses.color_pair(3))
        market.addstr(y_gap + 5 + (i*2),x_width - x_gap - 10,str(Items[item_list[i]]),curses.color_pair(3))

    market.addstr(y_width - 2*y_gap + 2, x_gap + 2,description,curses.color_pair(3))
    market.addstr(y_width - 5,x_width - 5,'.')
    
    c = chr(market.getch())
    if(int(c) <= len(Items)):
        description = Description[item_list[int(c) - 1]];
    
    market.refresh()

