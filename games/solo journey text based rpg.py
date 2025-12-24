import random, time, math

#-----------------------------------------------------------#
# Variables
name = input("Enter your name : ")
text_delay = 0.0

max_hp = 10
hp = 10
dmg = 2

#-----------------------------------------------------------#
# Dialogues
opening_texts = [
    ["[ You found yourself walking up to a weird place ]"],
    ["( My head hurts, ugh where is this )"],
    ["[ You take a look around you... ]"],
    ["[ You are surrounded by some wounded people, wearing ragged clothes with bandages here and there]"],
    ["[ Confused and not knowing what to do, you know you have to ask, hesitantly you let out a small voice ]"],
    [f"{name} : Um... Hello, where is this? who are you?"],
    ["[ One of the group members walk toward you, with a somewhat glad face he answered]"],
    ["??? : Greeting hero, I am once a royal advisor, responsible for managing magic department and royal court"],
    ["Sinirio : You can call me Sinirio (smiling at you)"],
    ["Sinirio : We are currently in the last remaining fortress of this kingdom, the last line of defense"],
    [f"{name} : Sorry, I.. I don't get it, but why am I here?"],
    ["Sinirio : You are being summoned as a hero to save our kingdom from the demons. I am trully sorry for having to summon you."],
    ["Sinirio : You are our last hope, please save us..."],
    [f"{name} : Wait, I can't, I want to return!"],
    ["Sinirio : I am sorry, but you can't return until you defeat the final boss which can only be summoned after you defeat 3 bosses"],
    [f"{name} : ..."],
    ["[ *BRUK BRUK BRUK ]"],
    ["Sinirio : It seems like we run out of time, best of luck hero"]
    ]

#-----------------------------------------------------------#
# Options
options = [
    ['1. Forward'],
    ['2. Open backpack'],
    ['3. Information'],
    ['4. Quit']
    ]
    

#-----------------------------------------------------------#
# Functions

def d(amt):
    time.sleep(amt)

def loading_animation(time):
    print("Loading", end = '')
    for i in range(5):
        print('.', end = '')
        d(time/5)

#-----------------------------------------------------------#
# Class
class backpack():
    def __init__(self, size, items):
        self.size = size
        self.items = [items]

    def add(self, item):
        if(len(self.items) < self.size):
            self.items.append(item)
        else:
            print("Backpack full")

    def drop(self, num):
        if(len(self.items) > 0 and num <= self.items):
            self.items.pop(num - 1)
        else:
            print("Invalid")

    def show(self):
        for num in range(len(self.items)):
            print(str(num + 1) + '.', self.items[num])

class slime:
    def __init__(self, level):
        base_hp = 10
        base_dmg = 2
        self.hp = round(base_hp + (math.log10((level * base_hp) ** 2) * base_hp + level)) - base_hp
        self.dmg = round(base_dmg + (math.log10((level * base_dmg) ** 2) * base_dmg + level)) - base_dmg

    def show_info(self):
        print("HP :", self.hp)
        print("Dmg :",self.dmg)
    
#class player:

    
class battle:
    def __init__(self, hp, dmg, enemy, enemy_hp, enemy_dmg):
        self.hp = hp
        self.dmg = dmg
        self.enemy = enemy
        self.enemy_hp = enemy_hp
        self.enemy_dmg = enemy_dmg
        
    def show_info(self):
        print('[ You encountered an enemy! ]')
        print(
        f'''
+---------------+
    [ Hero ]
Hp     : {self.hp}
Dmg    : {self.dmg}

+---------------+
        ''')
        print()
        print(f' {"VS":>8}')
        print()
        print(
        f'''
+---------------+
    [ {self.enemy} ]
Hp     : {self.enemy_hp}
Dmg    : {self.enemy_dmg}

+---------------+
        ''')

    def hit(self):
        hero_dmg = self.dmg + round(random.random() * self.dmg)
        enemy_dmg = self.enemy_dmg + round(random.random() * self.enemy_dmg)

        print("Hero deals %i damage"%hero_dmg)
        print("Enemy deals %i damage"%enemy_dmg)

        self.hp -= enemy_dmg
        self.enemy_hp -= hero_dmg

        print("Hero Hp  : %i"%self.hp)
        print("Enemy Hp : %i"%self.enemy_hp)
        self.check()

    def check(self):
        global on_battle
        if(self.hp <= 0):
            print("You lost!")
            print("Game Over")
            run = False
            
        if(self.enemy_hp <= 0):
            print("Victory")
            run = False

        
#-----------------------------------------------------------#
# Set up
bp = backpack(10,'potion')

#-----------------------------------------------------------#
# Main

print("<|--==========-------------[ <        > ]-------------==========--|>")
print(
'''
 **** **** *    ****      ***** **** *   * ****  **    * ***** *   *
 *    *  * *    *  *        *   *  * *   * *   * * *   * *      * *
 **** *  * *    *  *        *   *  * *   * ****  *  *  * *****   *
    * *  * *    *  *        *   *  * *   * *   * *   * * *       *
 **** **** **** ****      ***   **** ***** *   * *    ** *****   *
''')
print("<|--==========-------------[ <        > ]-------------==========--|>")
print(" " * 20,"[| A journey awaiting you! |]")

print()
print("Type 'start' to start your game : ", end = '')
_ = input()

print()
loading_animation(3)
print("\n\n")
for i in opening_texts:
    print(i[0])
    print()
    d(text_delay)




