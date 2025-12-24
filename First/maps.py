import pygame, importing
import threading as t

pygame.init()

scr = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()

# ===============================================================
# Import objects

land = importing.sprite('map_objects','land',1,'png')
land.import_pack(1)

grass = importing.sprite('map_objects','grass',1,'png')
grass.import_pack(1)

platform = importing.sprite('map_objects','platform',1,'png')
platform.import_pack(1)

cliff = importing.sprite('map_objects','cliff',1,'png')
cliff.import_pack(1)

# ===============================================================
# Collision
def collision(obj1,obj2):
    rect_1 = obj1.get_rect()
    rect_2 = obj2.get_rect()
    return pygame.Rect.colliderect(obj1,obj2)
    
# Blit object(map)
def draw_map(x,y):
    x2 = x
    game_map =[
    [
    '''
    000000000000000000000000000000000000000000000000000000000n
    000000000000000000000000000000000000000000000000000000000n
    000000000000000000000000000000000000000000000000000000000n
    00000000000000000000PPPP000000000000000000000000000000000n
    000000000000000000000000000000000000000000000000000000000n
    00000000000000PPPP000000000000000000000000000000000000000n
    000000000000000000000000000000000000000000000000000000000n
    000000000000000000000000000000000000000000000000000000000n
    GGGGGGGGGGGGGGGGGGGGGGG00000GGGGGGGGGGGGGGG00000000000000n
    DDDDDDDDDDDDDDDDDDDDDDD00000DDDDDDDDDDDDDDDC0000000000000n
    DDDDDDDDDDDDDDDDDDDDDDD00000DDDDDDDDDDDDDDDDC000000000000n
    DDDDDDDDDDDDDDDDDDDDDDD00000DDDDDDDDDDDDDDDDDC00000000000n
    DDDDDDDDDDDDDDDDDDDDDDD00000DDDDDDDDDDDDDDDDDDC0000000000n
    DDDDDDDDDDDDDDDDDDDDDDD00000DDDDDDDDDDDDDDDDDDDC000000000n
    '''
    ]
    ]
        
    for char in range(len(game_map[0][0])):
        if(game_map[0][0][char] == 'n'):
            y += 32
            x = x2
        elif(game_map[0][0][char] == 'G'):
            scr.blit(grass.lst[0][0],(x,y))
        elif(game_map[0][0][char] == 'D'):
            scr.blit(land.lst[0][0],(x,y))
        elif(game_map[0][0][char] == 'P'):
            scr.blit(platform.lst[0][0],(x,y))
        elif(game_map[0][0][char] == 'C'):
            scr.blit(cliff.lst[0][0],(x,y))
        x += 32

real_x, real_y = -180,75
run = False
if __name__ == "__main__":
    run = True

while run:
    clock.tick(30)
    #x, y = real_x, real_y
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        real_y += 5
    elif keys[pygame.K_a]:
        real_x -= 5
    elif keys[pygame.K_d]:
        real_x += 5
    elif keys[pygame.K_w]:
        real_y -= 5

    
    draw_map(real_x,real_y)
    #scr.blit(land.lst[0][0],(x,y))
    #test.draw(x,y + 50,0)
    real_x -= 2
    pygame.display.update()
    scr.fill((135,206,235))
