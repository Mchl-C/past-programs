import socket

T_PORT = 60

TCP_IP = '127.0.0.1'

BUF_SIZE = 1024

k = socket.socket (socket.AF_INET, socket.SOCK_STREAM)

k.connect((TCP_IP, T_PORT))

o = input('Input ur name : ')
k.send(bytes(o,'utf-8'))

l = k.recv(BUF_SIZE).decode()

while True:
    p = input('input message : ')
    MSG = p
    print()
    k.send(bytes(MSG,'utf-8'))

    data = k.recv(BUF_SIZE).decode()
    print(l,' : ',data)

    print()

