import pygame, sys, time, random, math
import threading as t

pygame.init()

scr_w, scr_h = 720,560
scr = pygame.display.set_mode((scr_w,scr_h))
pygame.display.set_caption("Road to 2023")
clock = pygame.time.Clock()
level = 3
#----------------------------------------------------------------------------
# Player
Hp = 10
level = 1
total_exp = (40 * (level)) ** 0.8
exp = 0
attack = 2
    
#----------------------------------------------------------------------------
def re(obj,size,angle):
    ox, oy = obj.get_size()
    obj = pygame.transform.scale(obj, (ox*size, oy*size))
    obj = pygame.transform.rotate(obj, angle)
    return obj

def write(word,ws,xpos,ypos):
    alp = []
    alpb = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+-x,'
    for i in range(len(alpb)):
        alphabet = pygame.image.load("alphabets\\"+ alpb[i] + '.png')
        ax, ay = alphabet.get_size()
        alphabet = re(alphabet,ws,0)
        alp.append(alphabet)

    for a in word.upper():
        for i in range(len(alpb)):
            ax, ay = alp[i].get_size()
            if(a == alpb[i]):
                scr.blit(alp[i],(xpos,ypos))
                xpos += ax + (ax/4)
            elif(a == ' '):
                xpos += ax/45

def swap_color(img, old_c, new_c):
    img_copy = pygame.Surface(img.get_size())
    img_copy.fill(new_c)
    img.set_colorkey(old_c)
    img_copy.blit(img,(0,0))
    return img_copy

def text_box(text,posx,posy,width,height):
    txt_box = pygame.Surface((width,height))
    txt_box.fill((100,100,100))
    scr.blit(txt_box,(posx,posy))
    write(text,3,posx + 10,posy + 8)

    
'''
def timer():
    global times_up
    time.sleep(3)
    if times_up == False:
        print("Times up")
        times_up = True
'''

def start_menu():
    start_button = [scr_w / 3,scr_h/2,250,80] #xpos, ypos, width, height
    menu = True

    while menu:
        scr.fill((0,0,0))

        rect = pygame.Surface((start_button[2],start_button[3]))
        outline = pygame.Surface((start_button[2] + 10, start_button[3] + 8))

        rect.fill((75,122,71))
        outline.fill((180,120,60))

        scr.blit(outline,(start_button[0] - 5, start_button[1] - 4))
        scr.blit(rect,(start_button[0],start_button[1]))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx,my = pygame.mouse.get_pos()
                if(mx >= start_button[0] and mx <= (start_button[0] + start_button[2]) and my >= start_button[1] and my <= (start_button[1] + start_button[3])):
                    menu = False
                    lay = True
                    layout()

        write("road to 2023",6,scr_w/21,scr_h/6)
        write("Start", 4, start_button[0] + 20,start_button[1] + 15)
            
        pygame.display.update()

def layout():
    global level
    points = [225,350,475,600]
    pindex = 0
    knight = pygame.image.load("char\\knight.png")
    knight = re(knight,8,0)

    point = pygame.image.load("assets\\point.png")
    point = re(point,3,0)
    pcolor = [['#39063a',(76,7,77),(94,11,96),(131,21,133)],
              [(34,11,96),(26,7,77),(20,6,58),(22,21,133)],
              [(6,58,29),(7,77,20),(26,96,11),(100,133,21)],
              [(14,91,86),(151,144,25),(192,183,26),(230,218,18)]
              ]
    px, py = point.get_size()
    
    lay = True
    while lay:
        scr.fill((0,0,0))
        
        for color in range(len(pcolor[pindex - 1])):
            #print('color #%i : %s %s'%(color,pcolor[0][color],pcolor[pindex - 1][color]))
            #print(pcolor[pindex - 1][color])
            swap_color(point,pcolor[0][color],pcolor[pindex - 1][color])
            point.set_colorkey((0,0,0))
            
        scr.blit(knight, (175,scr_h / 1.5))
        scr.blit(point, (points[pindex % 5],scr_h / 2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx,my = pygame.mouse.get_pos()
                if(mx >= points[pindex] and mx <= (points[pindex] + px) and my >= scr_h / 2 and my <= ((scr_h/2) + py)):
                    lay = False
                    level = pindex + 1
                    choose_level()
                
        pygame.display.update()

def choose_level():
    print(level)
    if level == 1:
        level_3()
    elif level == 2:
        level_2()
    elif level == 3:
        level_3()
    elif level == 4:
        level_4()

def level_1():
    global level, Hp
    # viruses
    print("Level 1")

    x,y = scr_w / 2, scr_h / 2
    player_x, player_y = 20,20
    speed = 300

    enemies_amount = 8
    enemies_killed = 0
    
    first = True
    direction = 'right'
    
    enemies = pygame.sprite.Group()
    for i in range(8):
        enemies.add(Enemy(random.randint(10,500), random.randint(10,400)))

    start_time = time.time()
    
    while first:
        dt = time.time() - start_time
        start_time = time.time()
        spd = speed * dt
        
        scr.fill("#507963")

        write(("Hp : " + str(Hp)), 2, 25,25)
        player = Player(player_x,player_y,x,y)
        scr.blit(player.player,(x,y))
        #player_rect = player.get_rect()
        if direction == 'right':
            pygame.draw.polygon(scr, (255,255,255), ((x + player_x,y - 2),(x + player_x,y + 8),(x + player_x*4,y + 3)))
            spear = Weapon((x + player_x),(y-2),(x + player_x*4),(y+3))
        elif direction == 'left':
            pygame.draw.polygon(scr, (255,255,255), ((x,y - 2),(x,y + 8),(x - player_x * 3,y + 3)))
            spear = Weapon((x),(y-2),(x - player_x*3),(y+3))
        elif direction == 'up':
            pygame.draw.polygon(scr, (255,255,255), ((x - 4,y),(x + 4,y),(x,y - player_y * 3)))
            spear = Weapon((x - 4),(y),(x + 4),(y - player_y * 3))
        elif direction == 'down':
            pygame.draw.polygon(scr, (255,255,255), ((x - 4,y + player_y),(x + 4,y + player_y),(x,y + player_y*4)))
            spear = Weapon((x - 4),(y + player_y),(x + 4),(y + player_y * 3))
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        enemies.update(x,y,dt)
        enemies.draw(scr)
        
        collided_enemies = pygame.sprite.spritecollide(spear, enemies, True)
        collided_player = pygame.sprite.spritecollide(player, enemies, False)
        if(collided_player):
            Hp -= 1
        
        if collided_enemies:
            enemies_killed += 1
            #print("Collision detected!")
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            y += spd
            direction = 'down'
            
        elif keys[pygame.K_a]:
            x -= spd
            direction = 'left'
            
        elif keys[pygame.K_d]:
            x += spd
            direction = 'right'
            
        elif keys[pygame.K_w]:
            y -= spd
            direction = 'up'

        elif keys[pygame.K_q]:
            first = False
            level = '3'
            level_3()

        if(enemies_killed >= enemies_amount):
            first = False
            level_3()
            
        pygame.display.update()
        

def level_2():
    print("Level 2")


def level_3():
    global level
    # Baldi math question
    print("Level 3")
    third = True
    times_up = False

    ans = 0
    score = 0
    tik = 0
    input_string = ''
    total_prob = 0

    num1 = random.randint(0,100)
    num2 = random.randint(0,100)
    operation = random.choice([' - ',' + ',' * '])
    
    while third:
        clock.tick(60)
        scr.fill((0,0,0))

        if(total_prob >= 40):
            third = False
            level = 4
            choose_level()
            
        if(operation == ' - '):
            ans = num1 - num2
        elif operation == ' + ':
            ans = num1 + num2
        else:
            ans = num1 * num2

        write("Third point : Math",4,50,50)
        write(("Score " + str(score)),1.5,450,200)
        write(("Total problems " + str(total_prob)),1.5,450,150)
        write("Problem : ",2.5,50,150)
        write((str(num1) + operation + str(num2)),2,50,200)       
        write("Your answer",2.5,50,250)
        
        text_box(input_string,50,300,250,50)
            
        if tik >= 60:
            print("tik")
            tik = 0
            num1 = random.randint(0,100)
            num2 = random.randint(0,100)
            operation = random.choice([' - ',' + ',' x '])
            total_prob += 1
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # Check for numeric keys
                if event.key == pygame.K_0:
                    input_string += "0"
                elif event.key == pygame.K_1:
                    input_string += "1"
                elif event.key == pygame.K_2:
                    input_string += "2"
                elif event.key == pygame.K_3:
                    input_string += "3"
                elif event.key == pygame.K_4:
                    input_string += "4"
                elif event.key == pygame.K_5:
                    input_string += "5"
                elif event.key == pygame.K_6:
                    input_string += "6"
                elif event.key == pygame.K_7:
                    input_string += "7"
                elif event.key == pygame.K_8:
                    input_string += "8"
                elif event.key == pygame.K_9:
                    input_string += "9"
                elif event.key == pygame.K_MINUS:
                    input_string += '-'
                # Check for the backspace key
                elif event.key == pygame.K_BACKSPACE:
                    input_string = input_string[:-1]
                elif event.key == pygame.K_RETURN:
                    num1 = random.randint(0,100)
                    num2 = random.randint(0,100)
                    operation = random.choice([' - ',' + ',' x '])

                    print(input_string)
                    if(input_string == str(ans)):
                        print("correct")
                        score += 1
                    else:
                        print("wrong")
                    total_prob += 1

        tik += 1
        pygame.display.update()
def level_4():
    print("Level 4")

# --------------------------------------------------------------------
# Classes
#Player
class Player(pygame.sprite.Sprite):
    def __init__(self,player_x,player_y,x,y):
        self.player = pygame.Surface((player_x, player_y))
        self.player.fill((255,255,255))
        self.rect = self.player.get_rect()
        self.rect.x = x
        self.rect.y = y

class Weapon(pygame.sprite.Sprite):
    def __init__(self,start_x,start_y,end_x,end_y):
        self.weapon = pygame.Surface((abs(int(end_x - start_x)),abs(int(end_y - start_y))))
        self.rect = self.weapon.get_rect()
        self.rect.x = end_x
        self.rect.y = end_y
        
# Enemies
class Enemy(pygame.sprite.Sprite):
    def __init__(self, ex, ey):
        super().__init__()
        self.image = pygame.image.load("assets\\bug.png")

        #print(f"ey, y : {1} {2}".format(ey,y))
        #print("min :",(ey-y))
        #print(f"ex, x : {1} {2}".format(ex,x))
        #print("min :",(ex-x))        

        self.image = re(self.image, 4,0)
        self.rect = self.image.get_rect()
        print(self.rect)
        self.rect.x = ex
        self.rect.y = ey
        self.speed = 50
        #self.x, self.y = x,y
        self.cx, self.cy = ex, ey

    def update(self,x,y,dt):
        #print(self.rect.x,self.rect.y)
        if(self.cx - x == 0):
            x += 1
            
        #degree = math.degrees(math.atan2((y-self.cy),(x-self.cx)))
        #print(degree)
        #print()
        #self.image = pygame.transform.rotate(self.image, 210)

        speed = self.speed*dt
        if(self.rect.x < x):
            self.cx += speed
        else:
            self.cx -= speed

        if(self.rect.y > y):
            self.cy -= speed
        else:
            self.cy += speed

        self.rect.x = int(self.cx)
        self.rect.y = int(self.cy)

        '''
        if self.rect.x >= scr_w:
            self.rect.x = 0
            
        if self.rect.y >= scr_h:
            self.rect.y = 0
        '''

start_menu()   
#layout()
#level_1()
