import socket, threading

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT))
s.listen(4)
conn, addr = s.accept()
print(conn, addr)
print(f"Connected by {addr}")

conn.sendall(b"Welcome to the server")
data = conn.recv(1024)
print(data.decode())

var = 5
def receiver(conn):
    global var
    conn.send(b'{var}')
    while True:
        try:
            data = conn.recv(1024)
            reply = data.decode('utf-8')
            if not data:
                conn.send("Go away")
                break
            else:
                print("reply : "+ reply)
        except:
            break

    print("Connection closed")
    conn.close()

while True:
    start_new_thread(receiver, (conn))
    
    
    
