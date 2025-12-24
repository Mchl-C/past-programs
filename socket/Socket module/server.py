import socket
        
s = socket.socket()
print('socket created')

s.bind(('localhost',5678))

s.listen(2)
print('waiting for connection')

while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()
    print('connected with',addr)
    print('Name :',name)

    messaging = True
    while messaging:
        #create a list of play options
        t = ["Rock", "Paper", "Scissors"]

        player2 = c.recv(1024).decode()
        
        #set player to False
        start = True

        while start == True:
        #set player to True
            player = input("Rock/Paper/Scissors? ")
            player = player.lower()
            c.send(bytes(player,'utf-8'))

            start = False

            if player2 == None:
                print("waiting for others's choice")
                
            if player == player2:
                print("Tie!")
            elif player2 == "rock":
                if player == "paper":
                    print("You win!", player, "covers", player2)
                else:
                    print("You lose!", player2, "smashes", player)
            elif player2 == "paper":
                if player == "scissors":
                    print("You win!", player, "cut", player2)
                else:
                    print("You lose!", player2, "covers", player)
            elif player2 == "scissors":
                if player == "rock":
                    print("You win", player, "smashes", player2)
                else:
                    print("You lose!", player2, "cut", player)
            else:
                print("That's not a valid play. Check your spelling!")
            #player was set to True, but we want it to be False so the loop continues
        
            player2 = None
            start = True
            player = None
            
    c.close()
