import pygame, math

#========================================================
# Set up
clock = pygame.time.Clock()
pygame.init()

width, height = 500,500
screen = pygame.display.set_mode((width,height))
border = pygame.Rect((20,20, width - 40, height - 40))

#========================================================
#Variables

run = True

x, y = 50, height - 50
margin = 25
ball = pygame.Rect((x,y,30,30))
xspeed, yspeed = 10,12
xbounce_cd = 0
ybounce_cd = 0
points = [[x,y],[x,y]]
n = 1

#========================================================
# Main script

while run:
    screen.fill((255,255,255))

    ball = pygame.Rect((x,y,30,30))
    points[n] = [x,y]
    
    pygame.draw.circle(screen,(0,0,0),(x,y),15)
    pygame.draw.rect(screen, (0,0,0), border, 1)

    pygame.draw.aalines(screen, (0,0,0), False, points)
    
    x += xspeed
    y -= yspeed

    if((y <= margin or y >= height - margin) and ybounce_cd <= 0):
        yspeed *= -1
        ybounce_cd = 10
        points[n] = [x,y]
        points.append([x,y])
        n += 1

    if((x <= margin or x >= width - margin) and xbounce_cd <= 0):
        xspeed *= -1
        xbounce_cd = 10
        points[n] = [x,y]
        points.append([x,y])
        n += 1

    if(ybounce_cd > 0):
        ybounce_cd -= 1
        
    if(xbounce_cd > 0):
        xbounce_cd -= 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
    pygame.display.update()
    clock.tick(60)
