import random, curses
from curses.textpad import Textbox, rectangle

#======================================================================================
# Classes

#player
class player:
    x_pos = 1
    y_pos = 2
    hp = 8
    max_hp = 80
    dmg = 2
    exp = 0
    lv = 1
    exp_to_lv_up = 10
    state = 'alive'

# Goblin
class goblin:
    e_pos = 15
    ey_pos = 12
    e_turn = 1
    hp = 4
    dmg = 1
    state = 'alive'
#======================================================================================
# Variables

run = True
player_char = '0'
screen = curses.initscr()
y_width,x_width = screen.getmaxyx()

goblin_gang = []
G_amount = 10
an = G_amount-1
G_positions = []
total_turns = 0

hp_pot_used = False
hp_potX = 20
hp_potY = 20
potion_heal_amount = 0

open_backpack = False
backpack = ["Health pot"]
description = {
    'Health pot' : "Health potion will heal 3/4 of your hp and might \
\t\t\t\t\t  save you when you're low on hp."
    }
money = 0

#colors
curses.start_color()
curses.use_default_colors()
curses.init_pair(1,156,0)
curses.init_pair(2,curses.COLOR_RED,0)
curses.init_pair(3,curses.COLOR_WHITE,0)
curses.init_pair(4,180,0)
curses.init_pair(5,curses.COLOR_YELLOW,0)
curses.init_pair(6,curses.COLOR_GREEN,0)

for i in range(G_amount):
    goblin_gang.append(goblin)
    goblin.ey_pos = random.randint(8,35)
    goblin.e_pos = random.randint(8,35)
    G_positions.append(goblin.ey_pos)
    G_positions.append(goblin.e_pos)
    print('goblin %d x_pos : '%i,goblin_gang[i].ey_pos,'  y_pos : ', goblin_gang[i].e_pos)

#======================================================================================
# functions

def use_hp_pot(hp_pot_use):
    global potion_heal_amount, hp_pot_used
    if hp_pot_use:
        print('Hp pot used')
        hp_pot_heal_amount = int(3/4*player.max_hp)
        potion_heal_amount = hp_pot_heal_amount
        hp_pot_used = False

        for i in range(len(backpack)):
            if backpack[i] == 'Health pot':
                backpack.remove(backpack[i])
                screen.refresh()
                
def free_heal(player_xpos,player_ypos,player_hp):
    global hp_potX,hp_potY,heal_amount
    
    if hp_potX == player_xpos and hp_potY == player_ypos:
        heal_amount = 3
        hp_potX,hp_potY = 0,0
        print('free heal used')

def bp():
    global open_backpack, backpack, money, hp_pot_used
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
            screen.addstr(y_width - 10,i + 5,'_', curses.color_pair(3))

        screen.addstr(7,18,"Money : %d"%money,curses.color_pair(3))
            
        for i in range(len(backpack)):
            screen.addstr(i+10,18,str(i+1) + '. ',curses.color_pair(3))
            screen.addstr(i+10,20,backpack[i],curses.color_pair(3))
            
        screen.addstr(1,17,"/================================================\\",curses.color_pair(3))
        screen.addstr(2,16,"/       ||                            ||           \\",curses.color_pair(3))
        screen.addstr(3,15,"/        ||                            ||            \\",curses.color_pair(3))
        screen.addstr(4,14,"/         ||                            ||             \\",curses.color_pair(3))
        screen.addstr(3,int(x_width/2) - 8,"B A C K P A C K",curses.color_pair(1))

        screen.addstr(0,int(x_width/2) - 16,'Click the item num for info...')

        screen.refresh()
        
        c = screen.getch()
        if chr(c) == 'b':
            open_backpack = False
        elif chr(c) == '1':
            screen.addstr(35,17,'Description',curses.color_pair(3))
            screen.addstr(37,17,description[backpack[0]],curses.color_pair(3))
            screen.addstr(0,int(x_width/2) - 16,'Click the item num again to use...',curses.color_pair(5))
            c = screen.getch()
            if chr(c) == ' ':
                screen.clear()
            elif chr(c) == '1':
                hp_pot_used = True
                
        else:
            open_backpack = True
    
def enemy_movement(turn,state,enemy_dmg,enemy_Xpos,enemy_Ypos,x_pos,y_pos):
    global enemy_xpos, enemy_ypos
    global enemy_damage, player_damage
    
    enemy_xpos,enemy_ypos = 0,0
    enemy_damage, player_damage = 0,0
    
    if enemy_Xpos > x_pos + 1:
        enemy_xpos -= 1
        turn = 0
    if enemy_Xpos < x_pos - 1:
        enemy_xpos += 1
        turn = 0
    if turn == 1:
        if enemy_Ypos > y_pos + 1:
            enemy_ypos -= 1
        if enemy_Ypos < y_pos - 1:
            enemy_ypos += 1
        if (enemy_Ypos >= y_pos - 1 and enemy_Ypos <= y_pos + 1 and state == 'alive'
            and enemy_Xpos >= x_pos - 1 and enemy_Xpos <= x_pos + 1):
            enemy_damage = enemy_dmg
            player_damage = player.dmg
            
def enemy_info(enemy_type,enemy_hp,enemy_dmg,enemy_state,enemy_xpos,enemy_ypos):
    lenght = len(enemy_type)
    if enemy_state == 'alive':
        if (enemy_xpos - player.x_pos >= -5 and enemy_xpos - player.x_pos <= 5
            and enemy_ypos - player.y_pos >= -5 and enemy_ypos - player.y_pos <= 5): 
            screen.addstr(0,x_width - (x_width - 40),'[%s]'%enemy_type,curses.color_pair(6))
            screen.addstr(0,x_width - (x_width - (57 - lenght)),'Hp : %s'%enemy_hp,curses.color_pair(6))
            screen.addstr(0,x_width - (x_width - (65 - lenght)),'Dmg : %s'%enemy_dmg,curses.color_pair(6))

def market(X_cord,Y_cord):
    if X_cord >= 18 and X_cord <= 27 and Y_cord >= 2 and Y_cord <= 3:
        player.y_pos += 1
        
#======================================================================================
while run:
    screen.addstr(0,4,"Start...",curses.A_BOLD)
    screen.addstr(0,x_width - (x_width-15),'HP = %d/%d'%(player.hp,player.max_hp),curses.color_pair(5))
    screen.addstr(0,x_width - (x_width-28),'Dmg = %d'%player.dmg,curses.color_pair(5))
    screen.addstr(y_width - 3, x_width - (x_width - 5),'Lv = %d'%player.lv,curses.color_pair(5))
    screen.addstr(y_width - 3, x_width - (x_width - 15),'Exp to lv up = %d'%(player.exp_to_lv_up - player.exp),curses.color_pair(5))
    
    enemy_movement(1,goblin_gang[an].state,goblin_gang[an].dmg,goblin_gang[an].e_pos,goblin_gang[an].ey_pos,player.x_pos,player.y_pos)
    enemy_info('Goblin',goblin_gang[an].hp,goblin_gang[an].dmg,goblin_gang[an].state,goblin_gang[an].e_pos,goblin_gang[an].ey_pos)
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #npcs
    for i in range(10):
        screen.addstr(3,i + 18,'̅',curses.color_pair(5))
    screen.addstr(2,18,'|',curses.color_pair(5))
    screen.addstr(2,27,'|',curses.color_pair(5))
    screen.addstr(2,20,'MARKET',curses.color_pair(6))
    market(player.x_pos,player.y_pos)
    
    # Player border
    if player.x_pos <= 1:
        player.x_pos += 1
    if player.y_pos <= 1:
        player.y_pos += 1
    if player.x_pos >= x_width - 11:
        player.x_pos -= 1
    if player.y_pos >= y_width - 5:
        player.y_pos -= 1

    for i in range(y_width - 5 ):
        screen.addstr(i,0,'|')
        screen.addstr(i,x_width - 10,'|')

    for i in range(x_width - 9):
        screen.addstr(1,i,'_')
        screen.addstr(y_width - 5,i,'_')
    
    #player exp n some settings
    if player.exp_to_lv_up - player.exp <= 0:
        print('lv up')
        player.exp_to_lv_up = 25*(player.lv-1)
        player.lv += 1
        player.exp = 0
        player.dmg += 2
        player.hp += 4
        player.max_hp += 4
        
    goblin_gang[an].e_pos += enemy_xpos
    goblin_gang[an].ey_pos += enemy_ypos
    
    goblin_gang[an].hp -= player_damage
    player.hp -= enemy_damage

    # player movement
    c = screen.getch()
    if chr(c) == 'a':
        player.x_pos -= 1
        player_char = '[0'
        c = ' '
    elif chr(c) == 's':
        player.y_pos += 1
        player_char = '0!'
        c = ' '
    elif chr(c) == 'd':
        player.x_pos += 1
        player_char = '0]'
        c = ' '
    elif chr(c) == 'w':
        player.y_pos -= 1
        player_char = '0^'
        c = ' '
    elif chr(c) == 'b':
        open_backpack = True
        
    if c == 'q':
        curses.endwin()

    if open_backpack == True:
        bp()
#+=============================================================
    if total_turns % 20 == 0:
        hp_potX = random.randint(10,x_width - 20)
        hp_potY = random.randint(10,y_width - 20)

    #potions n healing
    use_hp_pot(hp_pot_used)
    heal_amount = potion_heal_amount
    free_heal(player.x_pos,player.y_pos,player.hp)
    
    player.hp += heal_amount
    heal_amount = 0
    potion_heal_amount = 0
    
    if player.hp > player.max_hp:
        player.hp = player.max_hp

    #state(alive/dead)
    if goblin_gang[an].hp <= 0:
        goblin_gang[an].state = 'dead'
        player.exp += 6
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
    screen.addstr(goblin_gang[an].ey_pos,goblin_gang[an].e_pos,'G',curses.color_pair(6))
    total_turns += 1
    
    screen.refresh()

curses.endwin()
