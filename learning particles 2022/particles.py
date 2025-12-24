#!/usr/bin/python3.4
# Setup Python ----------------------------------------------- #
import pygame, sys, random, time, threading as t

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((500, 500),0,32)

# a particle is...
# a thing that exists at a location
# typically moves around
# typically changes over time
# and typically disappears after a certain amount of time

# [loc, velocity, timer]
particles = []

def draw_particles(mx,my):
    clock = pygame.time.Clock()
    timer = 0
    start_time = time.time()
    while int(timer - start_time) < 0.1:
        timer = time.time()
        particles.append([[mx, my], [random.randint(-3,3), random.randint(-4,2)], random.randint(4, 6)])

        for particle in particles:
            particle[0][0] += particle[1][0]
            particle[0][1] += particle[1][1]
            particle[2] -= 0.1
            particle[1][1] += 0.1
            pygame.draw.circle(screen, (200,100,50), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
            if particle[2] <= 0:
                particles.remove(particle)
        pygame.display.update()
        clock.tick(60)

color = (200,100,50)
# Loop ------------------------------------------------------- #
while True:
    
    # Background --------------------------------------------- #
    screen.fill((0,0,0))
    mx, my = pygame.mouse.get_pos()

    particles.append([[mx, my], [random.randint(-3,3), random.randint(-4,2)], random.randint(4, 6)])
    
    for particle in particles:
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        particle[2] -= 0.1
        particle[1][1] += 0.1
        pygame.draw.circle(screen, (color), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
        if particle[2] <= 0:
            particles.remove(particle)
            
    # Buttons ------------------------------------------------ #
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x_pos, y_pos = pygame.mouse.get_pos()
            thread_1 = t.Thread(target = draw_particles,args = (x_pos,y_pos))
            thread_1.start()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_p]:
        color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        
    # Update ------------------------------------------------- #
    pygame.display.update()
    mainClock.tick(60)
