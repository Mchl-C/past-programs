import pygame,os,time
import threading as t

pygame.init()

scr = pygame.display.set_mode((500,500))

class sprite:
    def __init__(self,directory,file_name,total_sprite,existence):
        self.name = file_name
        self.num  = total_sprite
        self.ex   = existence
        self.dr   = directory
        self.lst  = []
        
    def import_pack(self,size_multiplier):
        global var_name
        var_name = []
        if(self.dr == '-'):
            img = pygame.image.load((self.name+'.'+self.ex)).convert_alpha()
            Ix, Iy = img.get_size()
            img = pygame.transform.scale(img,(Ix * size_multiplier, Iy * size_multiplier))
            var_name.append(img)
            print(var_name)
            self.lst.append(var_name)

        else:
            if(self.num <= 1):
                form = self.name + '.' + self.ex
                img = pygame.image.load(os.path.join(self.dr,form)).convert_alpha()
                Ix, Iy = img.get_size()
                img = pygame.transform.scale(img,(Ix * size_multiplier, Iy * size_multiplier))
                var_name.append(img)
                self.lst.append(var_name)
            else:
                for i in range(self.num):
                    form = self.name + '_' + str(i) + '.' + self.ex
                    img = pygame.image.load(os.path.join(self.dr,form)).convert_alpha()
                    Ix, Iy = img.get_size()
                    img = pygame.transform.scale(img,(Ix * size_multiplier, Iy * size_multiplier))
                    var_name.append(img)
                    self.lst.append(var_name)

    def show(self):
        print(self.lst[0])
        #for i in range(len(self.lst)):
        #    for x in range(len(self.lst[i])):
        #        print(self.lst[i][x])

    def draw(self,posx,posy,ca,delay):
        #clock = pygame.time.Clock()
        #clock.tick(60)
        #def play_animation(lst,posx,posy):
        #print("Mx My :",posx,posy)
        #print(self.lst)
        #print(len(self.lst[ca]))
        for i in range(len(self.lst[ca])):
            #scr.blit(Image,(x,y))
            size_x,size_y = self.lst[ca][i].get_size()
            scr.blit(self.lst[ca][i],(posx - (size_x/3),posy - (size_y/3)))
            #pygame.time.delay(delay) #Delay usually 0.04
            time.sleep((delay)/100)
            pygame.display.update()
            #scr.fill((255,255,255))

if __name__ == '__main__':
    p = sprite('-',"dragon",1,'png')
    p.import_pack(1)
    p.show()
    p.draw(100,100,0,0)

    sp = sprite('fire',"sprite",16,'png')
    sp.import_pack(1)
    sp.show()
    sp.draw(100,100,0,4)

