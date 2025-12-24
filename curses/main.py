import random, curses,time
from curses.textpad import Textbox, rectangle

#======================================================================================
# Classes

#player
class player:
    x_pos = 10
    y_pos = 6
    hp = 30
    max_hp = 30
    dmg = 2
    exp = 0
    lv = 1
    exp_to_lv_up = 10
    state = 'alive'
    attack_range = 1
    defs = 10
    crit_chance = 5

# Goblin
class goblin:
    e_pos = 15
    ey_pos = 12
    e_turn = 1
    hp = 4
    dmg = 4
    max_money_drop = 6
    state = 'alive'

# guide
class guide:
    interact = 0
    quest_num = 0
    quest_in_progress = False

#======================================================================================
# Item Id
# Naming rule : use capital letter for each word begining 
Item1 = "Health Pot"
Item2 = "Short Sword"
Item3 = "Cloth Armor"
Item4 = "Wooden Shield"

Description = {
    Item1 : "Restore 1/4 of total HP",
    Item2 : "+5 Attack Damage",
    Item3 : "+10 Max Hp",
    Item4 : "+2 Def"
}
#======================================================================================
# Variables

tutorial = True
player_char = '0'
screen = curses.initscr()
y_width,x_width = screen.getmaxyx()
y_gap, x_gap = int(y_width/10), int(x_width/10)

goblin_gang = []
G_amount = 10
an = G_amount-1
G_positions = []
total_turns = 0

hp_pot_used = False
hp_potX = 20
hp_potY = 20
potion_heal_amount = 0

start = True
help_on = False
equipment_tab = False
open_info = False
open_backpack = False
open_market = False
open_quest = False

backpack = [Item1, Item2]

money = 100
caption = " "

#Quests
quest = []

#Equipment
helmet     = ""
armor      = ""
left_hand  = ""
right_hand = ""
gauntlet   = ""
greave     = ""
acc1       = ""
acc2       = ""

#colors
curses.start_color()
curses.use_default_colors()
curses.init_pair(1,156,0)
curses.init_pair(2,32,0)
curses.init_pair(3,curses.COLOR_WHITE,0)
curses.init_pair(4,180,0)
curses.init_pair(5,curses.COLOR_YELLOW,0)
curses.init_pair(6,curses.COLOR_GREEN,0)
curses.init_pair(7,130,0)
curses.init_pair(8,110,0)
curses.init_pair(9,124,0)
curses.init_pair(10,curses.COLOR_BLACK,curses.COLOR_BLACK)

for i in range(G_amount):
    goblin_gang.append(goblin)
    goblin.ey_pos = random.randint(8,35)
    goblin.e_pos = random.randint(8,35)
    G_positions.append(goblin.ey_pos)
    G_positions.append(goblin.e_pos)
    print('goblin %d x_pos : '%i,goblin_gang[i].ey_pos,'  y_pos : ', goblin_gang[i].e_pos)

#======================================================================================
#Keys
move_left = 'a'
move_right = 'd'
move_up = 'w'
move_down = 's'

info = 'i'
inventory = 'b'
equipment = 'e'
exit_market = 'm'
help_key = 'h'
quit = 'q'
chat = '\n' #(with npc)
quest_key = 'p'
yes = 'y'
no = 'n'

#======================================================================================
#Items Functions
def use_hp_pot():
    global heal_amount
    print('Hp pot used')
    hp_pot_heal_amount = int(1/4*player.max_hp)
    heal_amount = hp_pot_heal_amount

def short_sword():
    global left_hand,player
    left_hand = Item2
    player.dmg += 5

def cloth_shirt():
    global armor
    armor = Item3
    player.max_hp += 10
    player.hp += 10

def wooden_shield():
    global right_hand
    right_hand = Item4
    player.defs += 2

#======================================================================================
# functions
#Free Heal
def free_heal(player_xpos,player_ypos,player_hp):
    global hp_potX,hp_potY,heal_amount
    
    if hp_potX == player_xpos and hp_potY == player_ypos:
        heal_amount = int(player.max_hp/24)
        hp_potX,hp_potY = 0,0
        print('free heal used')

#crit
def crit():
    global player
    return random.choices([0,1],weights = (100 - player.crit_chance,player.crit_chance),k = 1)

#Backpack
def bp():
    global open_backpack, backpack, money, Description
    while open_backpack:
        screen.clear()
        for i in range(y_width - 5):
            screen.addstr(i + 5,15,'|',curses.color_pair(3))
            screen.addstr(i + 5,x_width - 15, '|',curses.color_pair(3))
            if i % 2 == 0:
                screen.addstr(i+5,14,'/',curses.color_pair(3))
                screen.addstr(i+5,x_width - 14,'\\',curses.color_pair(3))
            else:
                screen.addstr(i+5,14,'\\',curses.color_pair(3))
                screen.addstr(i+5,x_width - 14,'/',curses.color_pair(3))
            if i % 5 == 0:
                screen.addstr(i+5,8,'/\\',curses.color_pair(3))
                screen.addstr(i+5,x_width - 8,'/\\',curses.color_pair(3))
            if i % 5 == 1:
                screen.addstr(i+5,8,'\/',curses.color_pair(3))
                screen.addstr(i+5,x_width - 8,'\/',curses.color_pair(3))
                
        for i in range(x_width - 5):
            screen.addstr(5,i + 5,'_',curses.color_pair(3))
            screen.addstr(y_width - 2*y_gap,i + 5,'_', curses.color_pair(3))

        screen.addstr(7,18,"Money : %d"%money,curses.color_pair(3))
            
        for i in range(len(backpack)):
            screen.addstr(i+10,18,str(i+1) + '. ',curses.color_pair(3))
            screen.addstr(i+10,20,backpack[i],curses.color_pair(3))
            
        screen.addstr(1,17,"/",curses.color_pair(3))
        for i in range(x_width - 34):
            screen.addstr(1,18+i,"=",curses.color_pair(3))
        screen.addstr(1,x_width - 17,"\\",curses.color_pair(3))
        
        for i in range(3):
            for x in range(x_width - 34):
                if(x == 0):
                    screen.addstr(2 + i,16-i,"/",curses.color_pair(3))
                elif(x == x_width - 34 - 1):
                    screen.addstr(2 + i,x_width - 16 + i,"\\",curses.color_pair(3))
        
        screen.addstr(3,int(x_width/2) - 6,"B A C K P A C K",curses.color_pair(1))

        screen.addstr(0,int(x_width/2) - 16,'Click the item num for info...')

        screen.refresh()
        
        c = chr(screen.getch())
        if c == 'b':
            open_backpack = False
        else:
            try:
                if(int(c) <= len(backpack)):
                    first_num = int(c);                    
                    screen.addstr(y_width - 2*y_gap + 2,17,'Description',curses.color_pair(3))
                    screen.addstr(y_width - 2*y_gap + 3,17,Description[backpack[int(c) - 1]],curses.color_pair(3))
                    screen.addstr(0,int(x_width/2) - 16,'Click the item num again to use...',curses.color_pair(5))
                    c = chr(screen.getch())
                    if c == ' ':
                        screen.clear()
                    else:
                        try:
                            if(int(c) == first_num):
                                Function[backpack[int(c) - 1]]()
                                backpack.remove(backpack[int(c) - 1])
                        except ValueError:
                            open_backpack = True
            except ValueError:
                pass
    player.hp += heal_amount

#Market Place
def market_place():
    global open_market,caption,money,exit_market
    warning = " "
    while open_market:
        #Market borders
        screen.clear()
        screen.addstr(0,int(x_width/2) - 20," __  __     __     __    _  _   ___  ___",curses.color_pair(7))
        screen.addstr(1,int(x_width/2) - 20,"|  \\/  |   /[]\\   |[]|  | |/ / |      | ",curses.color_pair(7))
        screen.addstr(2,int(x_width/2) - 20,"| |\\/| |  / __ \\  ||\\\\  |   <  |---   | ",curses.color_pair(7))
        screen.addstr(3,int(x_width/2) - 20,"|_|  |_| /_/  \\_\\ || \\\\ |_|\\_\\ |___   | ",curses.color_pair(7))
        for i in range(x_width - 2*x_gap + 1):
            screen.addstr(y_gap,i + x_gap,'_',curses.color_pair(4))
            screen.addstr(y_width - y_gap,i + x_gap,'_',curses.color_pair(4))
            
        for i in range(1,y_width - 2*y_gap + 1,1):
            screen.addstr(i + y_gap,x_gap,'|',curses.color_pair(4))
            screen.addstr(i + y_gap,x_width - x_gap,'|',curses.color_pair(4))

        for i in range(x_width - 2*x_gap + 1):
            screen.addstr(y_width - 2*y_gap,x_gap + i,'_',curses.color_pair(4))
            
        #Item list
        screen.addstr(y_gap + 3, x_gap + 3,"Money : ",curses.color_pair(8))
        screen.addstr(y_gap + 3, x_gap + 10,str(money),curses.color_pair(8))
        screen.addstr(y_gap + 3, x_width - x_gap - 11,"Price",curses.color_pair(8))
        
        item_list = [Item1,Item2,Item3,Item4]
        Items = {
            Item1 : 20,
            Item2 : 30,
            Item3 : 40,
            Item4 : 30
        }
        
        for i in range(len(Items)):
            screen.addstr(y_gap + 6 + (i*2),x_gap + 3,(str(i+1) + '. ' + item_list[i]),curses.color_pair(8))
            screen.addstr(y_gap + 6 + (i*2),x_width - x_gap - 10,str(Items[item_list[i]]),curses.color_pair(8))

        screen.addstr(y_width - 2*y_gap + 2, x_gap + 2,caption,curses.color_pair(8))
        screen.addstr(y_width - y_gap + 1,x_gap + 1,warning,curses.color_pair(5))
        screen.addstr(y_gap + 1,int(x_width/2) - 12,"Tap any item to see info...",curses.color_pair(5))

        c = chr(screen.getch())
        if(c == exit_market):
            screen.clear()
            open_market = False
        else:
            try:
                if(int(c) <= len(Items)):
                    first_num = int(c)
                    caption = Description[item_list[int(c) - 1]]
                    screen.addstr(y_width - 2*y_gap + 2, x_gap + 2,caption,curses.color_pair(8))
                    screen.addstr(y_gap + 1,int(x_width/2) - 22,"Tap again to buy or tap other key to cancel...",curses.color_pair(5))
                    c = chr(screen.getch())
                    try:
                        if(int(c) == first_num):
                            if(money >= int(Items[item_list[int(c) - 1]])):
                                money -= int(Items[item_list[int(c) - 1]])
                                backpack.append(item_list[int(c) - 1])
                            else:
                                warning = "You can't efford that item..."
                        else:
                            caption = " "
                    except ValueError:
                        caption = " "
            except ValueError:
                caption = " "

        screen.addstr(y_width - 2,x_width - 2,'.')
        screen.refresh()

#Guide
def Guide(y,x):
    screen.nodelay(0)
    global guide
    c = ''
    for i in range(4,y_width - 4,1):
        screen.addstr(i,6,'|')
        screen.addstr(i,x_width - 6,'|')

    for i in range(6,x_width - 5,1):
        screen.addstr(3,i,'_')
        screen.addstr(y_width - 4,i,'_')

    for i in range(10):
        screen.addstr(5,i + 22,'̅',curses.color_pair(5))
    screen.addstr(4,22,'|',curses.color_pair(5))
    screen.addstr(4,31,'|',curses.color_pair(5))
    screen.addstr(4,24,'MARKET',curses.color_pair(6))

    chat_dialog = ['','Hello There, I am a guide from this game,\n\t\t you can call me "guide" haha...',
                   'Get it? cause I am guide','What is it? Its not funny? Alright whatever',
                   'Anyway since you can come all the way here,\n\t that means you must have understand how to move',
                   'Its simple, just tap those ASWD buttons','Why am I still tell you when you have known it already lol',
                   'You will automaticly attack enemies inside attack range',
                   'since you r the only one here, \n\t I will give you some eassyyyyy quests',
                   "r u ready? I won't take no for an answer",'#quest_1',"How is ur hunt going?"]
                   
    quest_log = ['kill 5 goblins, yep those red Gs why are them red? they um.. sunbathing for too long']

    chat_x = int(x/2) - int(len(chat_dialog[guide.interact+1])/10)
    chat_y = y - 4
    try:
        c = chr(screen.getch())
    except:
        c = c
    
    if c == chat and not guide.quest_in_progress:
        guide.interact += 1

    if chat_dialog[guide.interact][0:6] == '#quest':
        screen.addstr(chat_y-1,chat_x,quest_log[guide.quest_num])
        screen.addstr("\n\t\t accept quest?[y/n]")
        c = chr(screen.getch())
        if(c == 'y' and not guide.quest_in_progress):
            quest.append(quest_log[guide.quest_num])
            guide.quest_in_progress = True
        else:
            guide.interact -= 1
    else:
        if guide.quest_in_progress:
            screen.addstr(chat_y,chat_x,chat_dialog[guide.interact + 2])
        else:
            screen.addstr(chat_y,chat_x,chat_dialog[guide.interact])

        screen.addstr(y + 10,chat_x + 4,"Tap enter again to continue...")
    screen.refresh()

#Quest
def Quest():
    global quest,quest_key,open_quest
    win = curses.newwin(y_width - 5*y_gap,x_width - 6*x_gap,2*y_gap,2*x_gap)
    size_y,size_x = win.getmaxyx()
    tx,ty = 2,3

    while open_quest:
        win.border()
        win.addstr(1,int(size_x/2) - 6,"Quest List",curses.color_pair(5))
        for i in range(len(quest)):
            win.addstr(3+i,2,str(i+1) + '. ')
            for x in range(len(quest[i])):
                if tx > size_x - 3:
                    ty += 1
                    tx = 2
                win.addstr(ty,tx,quest[i][x])
                tx += 1

        win.addstr(size_y - 2,int(size_x/2) - 11,f"Tap {quest_key} again to exit...")
        c = chr(win.getch())
        if(c == quest_key):
            open_quest = False

        win.refresh()

#Player Info
def player_info():
    global player,open_info,info
    player_data = curses.newwin(y_width - 5*y_gap,x_width - 6*x_gap,2*y_gap,2*x_gap)
    size_y,size_x = player_data.getmaxyx()

    while open_info:
        player_data.border()
        player_data.addstr(1,int(size_x/2) - 6,"Player Info",curses.color_pair(5))
        player_data.addstr(3,2,"Name        : ")
        player_data.addstr("Player_1")
        player_data.addstr(4,2,"Lv          : ")
        player_data.addstr(str(player.lv))
        player_data.addstr(5,2,"Hp          : ")
        player_data.addstr(str(player.hp))
        player_data.addstr('/')
        player_data.addstr(str(player.max_hp))
        player_data.addstr(6,2,"Dmg         : ")
        player_data.addstr(str(player.dmg))
        player_data.addstr(7,2,"Def         : ")
        player_data.addstr(str(player.defs))
        player_data.addstr(8,2,"Crit chance : ")
        player_data.addstr(str(player.crit_chance))
        player_data.addstr('%')
        player_data.addstr(9,2,"Exp         : ")
        player_data.addstr(str(player.exp))
        player_data.addstr('/')
        player_data.addstr(str(player.exp_to_lv_up))
        player_data.addstr(10,2,"Money       : ")
        player_data.addstr(str(money))

        player_data.addstr(size_y - 2,int(size_x/2) - 11,f"Tap {info} again to exit...")
        
        c = chr(player_data.getch())
        if(c == info):
            open_info = False
        player_data.refresh()

#Equipment
def Equipment():
    global equipment_tab,helmet,armor,weapon,gauntlet,greave,acc1,acc2,equipment
    win = curses.newwin(y_width - 5*y_gap,x_width - 6*x_gap,2*y_gap,2*x_gap)
    size_y,size_x = win.getmaxyx()
    while equipment_tab:
        win.border()
        win.addstr(1,int(size_x/2) - 4,"Equipment")
        win.addstr(3,2,"Helmet     : ")
        win.addstr(helmet)
        win.addstr(4,2,"Armor      : ")
        win.addstr(armor)
        win.addstr(5,2,"Left hand  : ")
        win.addstr(left_hand)
        win.addstr(6,2,"Right hand : ")
        win.addstr(right_hand)
        win.addstr(7,2,"Gauntlet   : ")
        win.addstr(gauntlet)
        win.addstr(8,2,"Greave     : ")
        win.addstr(greave)
        win.addstr(9,2,"Accesories : ")
        win.addstr(acc1)
        win.addstr(10,2,"Accesories : ")
        win.addstr(acc2)

        win.addstr(size_y - 2,int(size_x/2) - 11,f"Tap {equipment} again to exit...")
        c = chr(win.getch())
        if(c == equipment):
            equipment_tab = False
        win.refresh()

#help function
def help_function():
    global help_on
    win = curses.newwin(y_width - 5*y_gap,x_width - 6*x_gap,2*y_gap,2*x_gap)
    size_y,size_x = win.getmaxyx()
    while help_on:
        win.border()
        win.addstr(1,int(size_x/2) - 7,"Key Functions")
        win.addstr(3,2,"i : Player Info")
        win.addstr(4,2,"e : Equipment Tab")
        win.addstr(5,2,"h : Show Help")
        win.addstr(6,2,"b : Open Backpack")
        win.addstr(7,2,"q : quit game")
        win.addstr(8,2,"m : exit market")
        win.addstr(9,2,"a/s/w/d : Movement Keys")
        win.addstr(10,2,"enter : interact with npcs")
        win.addstr(11,2,"p : open quest log")

        win.addstr(size_y - 2,int(size_x/2) - 11,"Tap h again to exit...")
        c = chr(win.getch())
        if(c == "h"):
            help_on = False
        win.refresh()

def enemy_movement(turn,state,enemy_dmg,enemy_Xpos,enemy_Ypos,x_pos,y_pos,player_range):
    global enemy_xpos, enemy_ypos
    global enemy_damage, player_damage
    
    enemy_xpos,enemy_ypos = 0,0
    enemy_damage, player_damage = 0,0
    
    if turn == 0:
        if enemy_Xpos > x_pos + 1:
            enemy_xpos -= 1
        if enemy_Xpos < x_pos - 1:
            enemy_xpos += 1
        if enemy_Ypos > y_pos + 1:
            enemy_ypos -= 1
        if enemy_Ypos < y_pos - 1:
            enemy_ypos += 1
        if (enemy_Ypos >= y_pos - player_range and enemy_Ypos <= y_pos + player_range and state == 'alive'
            and enemy_Xpos >= x_pos - 1 and enemy_Xpos <= x_pos + 1):
            enemy_damage = int(enemy_dmg/player.defs) + 1
            player_damage = player.dmg
            crit_res = crit()
            if(crit_res[0] == 1):
                player_damage *= 2
            
def enemy_info(enemy_type,enemy_hp,enemy_dmg,enemy_state,enemy_xpos,enemy_ypos):
    lenght = len(enemy_type)
    if enemy_state == 'alive':
        if (enemy_xpos - player.x_pos >= -5 and enemy_xpos - player.x_pos <= 5
            and enemy_ypos - player.y_pos >= -5 and enemy_ypos - player.y_pos <= 5): 
            screen.addstr(0,x_width - (x_width - 40),'[%s]'%enemy_type,curses.color_pair(6))
            screen.addstr(0,x_width - (x_width - (57 - lenght)),'Hp : %s'%enemy_hp,curses.color_pair(6))
            screen.addstr(0,x_width - (x_width - (65 - lenght)),'Dmg : %s'%enemy_dmg,curses.color_pair(6))
        
Function = {
    Item1 : use_hp_pot,
    Item2 : short_sword,
    Item3 : cloth_shirt,
    Item4 : wooden_shield
}

#======================================================================================
#start screen
while start:
    curses.echo(False)
    curses.resize_term(40,84)
    sscreen = curses.initscr()
    sscreen.nodelay(1)

    sy,sx = sscreen.getmaxyx()
    y1 = int(sy/10)
    x1 = int(sx/10)
    c = ''


    sscreen.clear()
    sscreen.border()

    #Tutorial Button
    screen.addstr(3*y1,2*x1-5,"|   |",curses.color_pair(5))
    screen.addstr(3*y1-1,2*x1-5,"|   |",curses.color_pair(5))
    screen.addstr(3*y1-2,2*x1-5," ___",curses.color_pair(5))
    screen.addstr(3*y1-1,2*x1-3,"A",curses.color_pair(5))

    for i in range(1,7*x1+3,1):
        sscreen.addstr(3*y1,2*x1 - 5 + i,'_',curses.color_pair(1))
        sscreen.addstr(4*y1+1,2*x1 - 5 + i,'_',curses.color_pair(1))
    for i in range(1,y1+2,1):
        sscreen.addstr(3*y1 + i,2*x1 - 5,'|',curses.color_pair(1))
        sscreen.addstr(3*y1 + i,9*x1 - 2,'|',curses.color_pair(1))

    sscreen.addstr(3*y1+1,2*x1 - 3," _____   _   _   _____   ____   ___    _     __     _")
    sscreen.addstr(3*y1+2,2*x1 - 3,"|_   _| | | | | |_   _| |    | | []\\  | |   /++\\   | |")
    sscreen.addstr(3*y1+3,2*x1 - 3,"  | |   | |_| |   | |   | [] | | | \\  | |  / __ \\  | |_")
    sscreen.addstr(3*y1+4,2*x1 - 3,"  |_|   |_____|   |_|   |____| |_|\\_\\ |_| /_/  \\_\\ |___|")

    screen.move(sy-1,sx-1)
    try: 
        c = chr(sscreen.getch())
    except:
        c = c
    if(c == 'a'):
        sscreen.clear()
        sscreen.refresh()
        start = False
        tutorial = True

    sscreen.refresh()

#======================================================================================
#tutorial
while tutorial:
    turns = 1
    screen.nodelay(0)
    curses.resize_term(40,84)
    curses.echo(False)

    if not (y_width == 40 and x_width == 84):
        curses.resize_term(40,84)
        y_width, x_width = screen.getmaxyx()
        y_gap, x_gap = int(y_width/10), int(x_width/10)

    heal_amount = 0
    c = ''
    screen.addstr(2,8,"Start...",curses.A_BOLD)
    screen.addstr(2,x_width - (x_width-20),'HP = %d/%d'%(player.hp,player.max_hp),curses.color_pair(5))
    screen.addstr(2,x_width - (x_width-32),'Dmg = %d'%player.dmg,curses.color_pair(5))
    screen.addstr(y_width - 2, x_width - (x_width - 8),'Lv = %d'%player.lv,curses.color_pair(5))
    screen.addstr(y_width - 2, x_width - (x_width - 20),'Exp to lv up = %d'%(player.exp_to_lv_up - player.exp),curses.color_pair(5))
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #npcs   
    screen.addstr(int(y_width/2) - y_gap,int(x_width/2) - x_gap,'G',curses.color_pair(6))
    if(player.y_pos == int(y_width/2) - y_gap and player.x_pos == int(x_width/2) - x_gap):
        Guide(int(y_width/2) - y_gap,int(x_width/2))

    for i in range(10):
        screen.addstr(5,i + 22,'̅',curses.color_pair(5))
    screen.addstr(4,22,'|',curses.color_pair(5))
    screen.addstr(4,31,'|',curses.color_pair(5))
    screen.addstr(4,24,'MARKET',curses.color_pair(6))

    if player.x_pos >= 22 and player.x_pos <= 31 and player.y_pos >= 4 and player.y_pos <= 5:
        open_market = True
        market_place()
        player.x_pos = 26
        player.y_pos = 6
    
    # Player border
    if player.x_pos <= 6:
        player.x_pos += 1
    if player.y_pos <= 3:
        player.y_pos += 1
    if player.x_pos >= x_width - 6:
        player.x_pos -= 1
    if player.y_pos >= y_width - 4:
        player.y_pos -= 1

    for i in range(4,y_width - 4,1):
        screen.addstr(i,6,'|')
        screen.addstr(i,x_width - 6,'|')

    for i in range(6,x_width - 5,1):
        screen.addstr(3,i,'_')
        screen.addstr(y_width - 4,i,'_')

    
    #player exp n some settings
    if player.exp_to_lv_up - player.exp <= 0:
        print('lv up')
        player.lv += 1
        player.exp -= player.exp_to_lv_up
        player.exp_to_lv_up = 25*(player.lv-1)
        player.dmg += 2
        player.hp += 4
        player.max_hp += 4

    # player movement
    try:
        c = chr(screen.getch())
        turns -= 1
    except:
        c = c

    if c == move_left:
        player.x_pos -= 1
        player_char = '[0'
        c = ' '
    
    elif c == move_down:
        player.y_pos += 1
        player_char = '0!'
        c = ' '
    
    elif c == move_right:
        player.x_pos += 1
        player_char = '0]'
        c = ' '
    
    elif c == move_up:
        player.y_pos -= 1
        player_char = '0^'
        c = ' '
    
    elif c == inventory:
        open_backpack = True
    
    elif c == info:
        open_info = True
        player_info()
    
    elif c == equipment:
        equipment_tab = True
        Equipment()

    elif c == help_key:
        help_on = True
        help_function()

    elif c == quest_key:
        open_quest = True
        Quest()

    if c == quit:
        tutorial = False
        curses.endwin()

    if open_backpack == True:
        bp()

#+=============================================================
    enemy_movement(turns,goblin_gang[an].state,goblin_gang[an].dmg,goblin_gang[an].e_pos,goblin_gang[an].ey_pos,player.x_pos,player.y_pos,player.attack_range)
    enemy_info('Goblin',goblin_gang[an].hp,goblin_gang[an].dmg,goblin_gang[an].state,goblin_gang[an].e_pos,goblin_gang[an].ey_pos) 

    if total_turns % 20 == 0:
        hp_potX = random.randint(10,x_width - 20)
        hp_potY = random.randint(10,y_width - 20)

    #potions n healing
    free_heal(player.x_pos,player.y_pos,player.hp)
    
    player.hp += heal_amount
    heal_amount = 0
    potion_heal_amount = 0
    
    goblin_gang[an].e_pos += enemy_xpos
    goblin_gang[an].ey_pos += enemy_ypos
    
    goblin_gang[an].hp -= player_damage
    player.hp -= enemy_damage

    if player.hp > player.max_hp:
        player.hp = player.max_hp

    #state(alive/dead)
    if goblin_gang[an].hp <= 0:
        goblin_gang[an].state = 'dead'
        player.exp += 6
        money += random.randint(0,goblin.max_money_drop)
        an -= 1
        goblin_gang[an].e_pos,goblin_gang[an].ey_pos = G_positions[an*2 + 2],G_positions[an*2 + 1]
        goblin_gang[an].state = 'alive'
        goblin_gang[an].hp = 4
    elif player.hp <= 0:
        player.state = 'dead'
        screen.clear()
        curses.endwin()
        exit()
        print("== Game Over ==")

    screen.clear()

    if player.state == 'alive':
        screen.addstr(player.y_pos,player.x_pos,player_char,curses.color_pair(4))
    else:
        curses.endwin()

    screen.addstr(hp_potY,hp_potX,'P',curses.color_pair(2))
    screen.addstr(0,0,' ',curses.color_pair(10))
    screen.addstr(goblin_gang[an].ey_pos,goblin_gang[an].e_pos,'G',curses.color_pair(9))
    if(turns == 0):
        total_turns += 1
    
    screen.refresh()

curses.endwin()
