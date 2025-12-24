import random

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
        global run
        if(self.hp <= 0):
            print("You lost!")
            print("Game Over")
            run = False
            
        if(self.enemy_hp <= 0):
            print("Victory")
            run = False

fight = battle(10,3,'slime',15,1)
fight.show_info()
run = True

while run:
    n = input()
    fight.hit()
    
