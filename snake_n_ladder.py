import random

print("Snake and Ladder")

snakes = []
ladders = []
pos = 0

c1 = []
c2 = []

for i in range(8):
    d1 = [random.randint(10,98),random.randint(4,25)]
    if(d1 not in c1):
        c1.append(d1[0])
        snakes.append(d1)

for i in range(8):
    d2 = [random.randint(10,84),random.randint(4,25)]
    if(d2 not in c1 and d2 not in c2):
        c2.append(d2[0])
        ladders.append(d2)
        
print(snakes)
print(ladders)

players = ['[]','||']
pos = [0,0]
run = True

while run:
    for i in range(len(players)):
        print("Roll for player",i + 1,'[y] : ',end = '')
        n = input()
        dice = random.randint(1,6)
        print(dice, pos[i])
        pos[i] += dice
    
    for i in range(100):
        snake = False
        ladder = False
        ever = False
        ever2 = False
        
        for x in range(8):
            if(snakes[x][0] == i):
                snake = True
                for z in range(len(players)):
                    if(pos[z] == i + 1):
                        pos[z] -= snakes[x][1]

                    if(pos[z] == i+1):
                        print(players[z] + '!')
                    else:
                        if(not ever):
                            if(i % 10 == 9):
                                print(str(i + 1) + ' !')
                            else:
                                print('! ' + str(i + 1) + ' ! ',end='')
                            ever = True

            elif(ladders[x][0] == i):
                ladder = True
                for z in range(len(players)):
                    if(pos[z] == i + 1):
                        pos[z] += ladders[x][1]

                    if(pos[z] == i + 1):
                            print(players[z] + '+')
                    else:
                        if(not ever2):
                            if(i % 10 == 9):
                                print(str(i + 1) + ' +')                    
                            else:
                                print('+ ' + str(i + 1) + ' + ',end='')                            
                            ever2 = True

        ever3 = False
        if(i % 10 == 9 and not snake and not ladder):
            for z in range(len(players)):
                if(pos[z] == i + 1):
                    print(players[z] + ' |')
                    ever3 = True
                else:
                    if(not ever3):
                        print(i + 1,'|')
                        ever3 = True
                        
        elif(i < 10 and not snake and not ladder):
            for z in range(len(players)):
                if(pos[z] == i + 1):
                    print('| ' + players[z],end = ' | ')
                    ever3 = True
                else:
                    if(not ever3):
                        print('| ' + str(i + 1),end = '  | ')
                        ever3 = True
        else:
            if(not snake and not ladder):
                for z in range(len(players)):
                    if(pos[z] == i + 1):
                        print('| ' + players[z],end = " | ")
                        ever3 = True
                    else:
                        if(not ever3):
                            print('| ' + str(i + 1),end = " | ")
                            ever3 = True
