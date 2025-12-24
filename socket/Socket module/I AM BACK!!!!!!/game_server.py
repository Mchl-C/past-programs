import socket
T_PORT = 60

TCP_IP = '127.0.0.1'

BUF_SIZE = 30

k = socket.socket (socket.AF_INET, socket.SOCK_STREAM)

k.bind((TCP_IP, T_PORT))

k.listen(1)

con, addr = k.accept()
print ('Connection Address is: ' , addr)

o = con.recv(BUF_SIZE).decode()

l = input('Input ur name : ')
con.send(bytes(l,'utf-8'))

while True :
    data = con.recv(BUF_SIZE).decode()

    print (o," : ", data)
    print()

    p = input('Input Message : ')
    print()
    con.send(bytes(p,'utf-8'))

