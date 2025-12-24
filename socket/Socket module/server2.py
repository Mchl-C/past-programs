import pygame,sys
import socket
import threading
from socket import gethostbyname, gethostname

pygame.init()
screen = pygame.display.set_mode((500,500))
fps = pygame.time.Clock()

s = socket.socket()
server = socket.gethostbyname(gethostname())
s.bind((server,5050))
s.listen(2)

x = 300
y = 400
a = 200
b = 400

run = True
while run:
    pygame.event.pump()
    screen.fill((140,80,50))
    fps.tick(180)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    def connect():
        global x,y
        global a,b
        
        c, addr = s.accept()
        print('connected with',addr,c)

        c.send(bytes(str(x),'utf-8'))
        c.send(bytes(str(y),'utf-8'))

        a = c.recv(2048).decode()
        b = c.recv(2048).decode()
        a = int(a)
        b = int(b)

    def main():
        global x,y
        global a,b

        rect1 = pygame.Rect(a,b,30,30)
        rect2 = pygame.Rect(x,y,30,30)
        pygame.draw.rect(screen,(140,255,80),rect1)
        pygame.draw.rect(screen,(120,100,255),rect2)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 2
            elif event.key == pygame.K_RIGHT:
                x += 2

    t1 = threading.Thread(target = connect)
    t2 = threading.Thread(target = main)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    
    pygame.display.update()
