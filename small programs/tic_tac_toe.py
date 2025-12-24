ar = [['1','2','3'],
      ['4','5','6'],
      ['7','8','9']]

run = True

def display():
    for i in range(3):
        for j in range(3):
            print('|' + ar[i][j], end = '')
        print('|')
        print("+-+-+-+")
    print()

def check():
    win = 0
    for i in range(3):
        match = True
        match2 = True
        ch = ar[i][0]
        cr = ar[0][i]
        for j in range(1,3):
            if(ch != ar[i][j]):
                match = False
            if(cr != ar[j][i]):
                match2 = False
        if(match):
            win = 1 if ch == char1 else 2
        if(match2):
            win = 1 if cr == char1 else 2

    if(ar[0][0] == ar[1][1] == ar[2][2] or ar[0][2] == ar[1][1] == ar[2][0]):
        win = 1 if ar[1][1] == char1 else 2
        
    return win
        
def win():
    global run
    cek = check()
    if(cek):
        print(f"Game Ended, Player {cek} wins!")
        run = False
    
print("+=====================+")
print("<---- Tic Tac Toe ---->")
print("+=====================+")

char1 = input("Player 1 choose your symbol[X/O] : ")
char2 = input("Player 2 choose your symbol[X/O] : ")
print('-----------------------')
print()

while run:
    display()
    p1 = int(input(f"Choose an unoccupied position[{char1}]: "))
    c = ar[(p1 - 1)//3][(p1 - 1) % 3]
    while(c == char1 or c == char2):
        print("Invalid move! Try another spot")
        p1 = int(input(f"Choose an unoccupied position[{char1}]: "))
        c = ar[(p1 - 1)//3][(p1 - 1) % 3]
        print()
        
    ar[(p1 - 1)//3][(p1 - 1) % 3] = char1
    win()

    if run:
        display()
        p2 = int(input(f"Choose an unoccupied position[{char2}]: "))
        ar[(p2 - 1)//3][(p2 - 1) % 3] = char2
        c = ar[(p1 - 1)//3][(p1 - 1) % 3]
        while(c == char1 or c == char2):
            print("Invalid move! Try another spot")
            p1 = int(input(f"Choose an unoccupied position[{char1}]: "))
            c = ar[(p1 - 1)//3][(p1 - 1) % 3]
            print()
        
        win()
    
print("Thanks for playing ~")
