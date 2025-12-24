x = 1
y = 1
run = True

while run:
    print(
'''
1. Maju
2. Mundur
3. Atas
4. Bawah
5. Show position
5. Quit
''')
    n = int(input("Masukan pilihan: "))

    if(n == 1):
        print('maju')
        if(n < 8):
            x += 2
    elif(n == 2):
        print('mundur')
        if(n > 0):
            x -= 2
    elif(n == 3):
        print('atas')
        if(n > 0):
            y -= 2
    elif(n == 4):
        print('bawah')
        if(n < 8):
            y += 2
    elif(n == 5):
        pass
    else:
        print('quit')
        run = False
        break

    print('Your current position is %i, %i'%(x, y))
    for row in range(8):
        for col in range(8):
            if(row == y-1 and col == x-1):
                print('P', end = ' ')
            else:
                print('.', end = ' ')
        print()
                        

    print()
    
