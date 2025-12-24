import socket

c = socket.socket()

c.connect(('localhost',5678))
print('enter ur name')
name = input()

c.send(bytes(name,'utf-8'))
w = input('Type [play] to start the game ')
w.lower()
if w == 'play':
    start = True
else:
    print('Ok see you again')

while True:
    while start == True:
    #set player to True
        player2 = input('Rock/Paper/Scissors? ')
        player2 = player2.lower()
        c.send(bytes(player2,'utf-8'))

        player = c.recv(1024).decode()
        start = False

        if player == None:
            print("waiting for other person's choice")
        
        if player == player2:
            print("Tie!")
        elif player == "rock":
            if player2 == "paper":
                print("You win!", player, "covers", player2)
            else:
                print("You lose!", player2, "smashes", player)
        elif player == "paper":
            if player2 == "scissors":
                print("You win!", player2, "cut", player)
            else:
                print("You lose!", player, "covers", player2)
        elif player == "scissors":
            if player2 == "rock":
                print("You win", player2 ,"smashes", player)
            else:
                print("You lose!", player, "cut", player2)
        else:
            print("That's not a valid play. Check your spelling!")
            
        player = None
        player2 = None
        start = True
