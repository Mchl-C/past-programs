# echo-client.py

import socket, threading, time

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
data = s.recv(1024)
s.sendall(b"Thanks for having me")

print(f"Received : {data.decode()}")

def receiver():
    while True:
        try:
            msg = s.recv(1024)
            print(f'{msg}')
        except Exception as e:
            print(e)
            break

while True:
    n = input("message : ")
