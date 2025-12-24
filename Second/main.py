import pygame, os, sys
import time, threading as t

pygame.init()
scr = pygame.display.set_mode((720,560))

# ------------------------------------------------------------------------------------
# Snowman
snowman_animation = []
snowman_index = 0
snowman_x, snowman_y = 100,300
for i in range(12):
    img = pygame.image.load("snowman/" + 'snowman_' + str(i) + '.png').convert_alpha()
    Ix, Iy = img.get_size()
    img = pygame.transform.scale(img,(Ix * 2, Iy * 2))
    snowman_animation.append(img)

# --------------------------------------------------------------------------------------

run = True
clock = pygame.time.Clock()
previous_time = time.time()

font = pygame.font.SysFont('timesnewroman', 48,True)
text = font.render("Merry Christmas",True,(0,200,80),(20,40,128))
text_rect = text.get_rect()
text_rect.center = (720/2,560/2)
    
while run:
    clock.tick(60)
    scr.fill((200,200,200))

    dt = time.time() - previous_time
    previous_time = time.time()
    
    all_sprite = pygame.sprite.Group()
    all_sprite.draw(scr)

    scr.blit(snowman_animation[int(snowman_index) % len(snowman_animation)],(snowman_x,snowman_y))
    snowman_index += 12 * dt

    scr.blit(text,text_rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        snowman_x -= 3
    elif keys[pygame.K_d]:
        snowman_x += 3
        
    pygame.display.update()
    
