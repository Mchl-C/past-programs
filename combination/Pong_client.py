import socket
import curses
import threading
import pickle

x, y = 2, 10
HOST = '127.0.0.1'
PORT = 5555

c = ''
def movement(stdscr, client):
    while True:
        try:
            num = client.recv(1024).decode('utf-8')
            stdscr.addstr(3,0,"Client num : " + str(num))
        
            key = stdscr.getch()
            if key == ord('q'):
                break

            if key == curses.KEY_UP or key == ord('w'):
                c = 'up'
            elif key == curses.KEY_DOWN or key == ord('s'):
                c = 'down'
            else:
                c = ''

            print("C :",c)
            client.send(str(c).encode('utf-8'))
                
            stdscr.addstr(0, 0, f"Player pos: {x}, {y}", curses.A_BOLD)
            stdscr.refresh()
            
        except Exception as e:
            print(f"Error handling client : {e}")
            break
        
def start_client(stdscr):
    print("start")
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(50)
    
    stdscr.clear()
    stdscr.addstr(0, 0, "Client - Press 'q' to exit", curses.A_BOLD)
    stdscr.refresh()

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

                
    sh, sw = stdscr.getmaxyx()
    paddle1_y = sh / 2
    paddle2_y = sh / 2

    while True:
        try:
            stdscr.clear()
            #print("Triggered")
            control = threading.Thread(target = movement, args = (stdscr, client))
            control.start()
                
            stdscr.refresh()

        except Exception as e:
            print(f"Error in client: {e}")
            break

    client.close()

if __name__ == "__main__":
    curses.wrapper(start_client)
