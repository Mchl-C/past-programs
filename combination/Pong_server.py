import socket
import threading
import curses
import time
import pickle

class GameState:
    def __init__(self):
        self.pos = []
        
        self.score1 = 0
        self.score2 = 0
        self.paddle_length1 = 3
        self.paddle_length2 = 3
        self.ball_y = 0
        self.ball_x = 0
        self.power_up_present = False
        self.power_up_y = 0
        self.power_up_x = 0

def handle_client(client_socket, player_number, game_state, stdscr):
    while True:
        try:
            client_socket.send(str(player_number).encode('utf-8'))
            print("Number sent")
            data = client_socket.recv(1024).decode('utf-8')
            print(data)

            if not data:
                break
            
            stdscr.addstr(8,0, player_number)
            if data == 'down':
                stdscr.addstr(10,0,"Client pressed w")
                game_state.paddle1_y += 2
            elif data == 'up':
                stdscr.addstr(11,0,"Client pressed s")
                game_state.paddle1_y -= 2

            stdscr.refresh()
    
        except Exception as e:
            print(f"Error handling client {player_number}: {e}")
            break

    client_socket.close()

def start_server(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Server - Press 'q' to exit", curses.A_BOLD)
    stdscr.refresh()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 5555))
    server.listen(4)

    player_number = 1
    game_state = GameState()

    while True:
        client, addr = server.accept()
        stdscr.addstr(2, 0, f"Accepted connection from {addr}", curses.A_BOLD)
        stdscr.addstr(4, 0, "player number : " + str(player_number))
        stdscr.refresh()

        game_state.paddle1_y = stdscr.getmaxyx()[0] // 2
        game_state.paddle2_y = stdscr.getmaxyx()[0] // 2

        client_handler = threading.Thread(target=handle_client, args=(client, player_number, game_state, stdscr))
        client_handler.start()

        player_number += 1

if __name__ == "__main__":
    curses.wrapper(start_server)
