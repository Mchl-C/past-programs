import pygame
import socket
import threading

pygame.init()

screen = pygame.display.set_mode((500, 500))
fps = pygame.time.Clock()

px = 0
py = 0

run = True

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP = '192.168.8.147'
port = 60

s.bind((IP,port))
s.listen(2)

c,addr = s.accept()
print('Connected with ',addr)

def click():
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            px, py = pygame.mouse.get_pos()
            print(px,py)

while run:
    pygame.event.pump()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    x = str(px)
    y = str(py)

    a = int(c.recv(1024).decode())
    b = int(c.recv(1024).decode())
    
    c.send(bytes(x,'utf-8'))
    c.send(bytes(y,'utf-8'))
    
    t1 = threading.Thread(target = click)

    t1.start()

    pygame.display.update()
'''
    fps.tick(180)
    y += 1
    screen.fill((240, 240, 240))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                y -= 150

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            x -= 2
        elif event.key == pygame.K_RIGHT:
            x += 2

    if y >= 450:
        y = 450
    if x >= 460:
        x = 460
    elif x <= 20:
        x = 20

    rect = pygame.Rect(x, y, 30, 30)
    pygame.draw.rect(screen, (0, 0, 0), rect)

    pygame.display.update()
'''
