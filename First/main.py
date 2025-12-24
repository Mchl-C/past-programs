import pygame
import os, sys
import time
import threading as t
import importing, maps

pygame.init()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Functions

'''
def import_pack(name,num,ex):
    global pack_lst;
    pack_lst = []
    for i in range(num):
        form = name + '_' + str(i) + '.' + ex
        img = pygame.image.load(os.path.join("fire",form)).convert_alpha()
        Ix, Iy = img.get_size()
        img = pygame.transform.scale(img,(Ix * 2.5, Iy * 2.5))
        pack_lst.append(img)
        print(pack_lst[i])

def play_animation(lst,posx,posy):
    print("Mx My :",posx,posy)
    for i in range(len(lst)):
        #scr.blit(Image,(x,y))
        scr.blit(lst[i],(posx - 40 ,posy - 40))
        time.sleep(0.04)
        pygame.display.update()
        scr.fill((255,255,255))
'''

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

run = True
scr = pygame.display.set_mode((500,500))

clock = pygame.time.Clock()
#Image = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("Image.jpg").convert(),(260,200)),270)
#Image = pygame.image.load("Dragon.png").convert_alpha()
#Img_x, Img_y = Image.get_size()
#Image = pygame.transform.scale(Image,(Img_x / 2, Img_y / 2))
#Img_x, Img_y = Image.get_size()

sprite = importing.sprite('-','dragon',0,'png')
sprite.import_pack(0.5)
char_rec = sprite.lst[0][0].get_rect()

spell = importing.sprite('fire',"sprite",16,'png')
spell.import_pack(3)

spell_2 = importing.sprite('Ice','ice',12,'png')
spell_2.import_pack(3)

x, y = 100,150
map_x, map_y = -200,75

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main loop
while run:
    clock.tick(60)
    
    maps.draw_map(map_x,map_y)
    sprite.draw(x,y,0,0)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pressed()
            Mx,My = pygame.mouse.get_pos()
            if mouse[0]:
                thread_1 = t.Thread(target = spell.draw,args = (Mx,My,1,4))
                thread_1.start()
            elif mouse[2]:
                thread_1 = t.Thread(target = spell_2.draw,args = (Mx,My,1,7))
                thread_1.start()
            
            #print(t.active_count())
            
            #play_animation(pack_lst,Mx,My)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and char_rec.left + 40 > 0:
        x -= 6
        char_rec.right -= 6
        #print('char_rec.left : ',char_rec.left)
        
    elif keys[pygame.K_s] and char_rec.bottom + 100 + map_y < 500:
        y += 6
        char_rec.bottom += 6
        #print('char_rec.bottom : ',char_rec.bottom)
        
    elif keys[pygame.K_w] and char_rec.top + 100 > 0:
        y -= 6
        char_rec.top -= 6
        #print('char_rec.top : ',char_rec.top)
        
    elif keys[pygame.K_d] and char_rec.right + 40 <= 500:
        x += 6
        char_rec.right += 6
        #print('char_rec.right : ',char_rec.right)

    if char_rec.right + 100 >= 500:
        map_x -= 4
    elif char_rec.left - 50 <= 0:
        map_x += 4

    map_x -= 2
    pygame.display.update()
    scr.fill((200,200,200))
    #scr.fill((135,206,235))
