#sample
import pygame
import threading

pygame.init()

screen = pygame.display.set_mode((500,500))
time = pygame.time.Clock()

x = 250
y = 350

run = True
while  run:
    pygame.event.pump()
    time.tick(180)
    screen.fill((240,240,240))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    def main():
        global x,y 
        rect = pygame.Rect(x,y,30,30)
        pygame.draw.rect(screen,(0,0,0),rect)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 2
            elif event.key == pygame.K_RIGHT:
                x += 2

    t1 = threading.Thread(target = main)
    t1.start()
    t1.join()
    
    pygame.display.update()
