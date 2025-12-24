import curses
import time
import random

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(50)

    sh, sw = stdscr.getmaxyx()

    # Initialize colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)    # Border color
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)  # Paddle color
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_YELLOW)    # Ball color
    curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)   # Score color
    curses.init_pair(5, curses.COLOR_GREEN, curses.COLOR_GREEN)   # Power-up color

    # Initialize scores and paddle lengths
    score1 = 0
    score2 = 0
    paddle_length1 = 3
    paddle_length2 = 3

    # Power-up variables
    power_up_present = False
    power_up_y, power_up_x = 0, 0

    def draw_power_up():
        stdscr.addch(power_up_y, power_up_x, 'O', curses.color_pair(5))

    while True:
        stdscr.clear()

        # Draw simplified border with colors
        for i in range(1, sh - 1):
            stdscr.addch(i, 0, '|', curses.color_pair(1) | curses.A_BOLD)
            stdscr.addch(i, sw - 1, '|', curses.color_pair(1) | curses.A_BOLD)

        for i in range(1, sw - 1):
            stdscr.addch(0, i, '-', curses.color_pair(1) | curses.A_BOLD)
            stdscr.addch(sh - 1, i, '-', curses.color_pair(1) | curses.A_BOLD)

        stdscr.addch(2, 2, '+', curses.color_pair(1) | curses.A_BOLD)
        stdscr.addch(2, sw - 2, '+', curses.color_pair(1) | curses.A_BOLD)
        stdscr.addch(sh - 2, 2, '+', curses.color_pair(1) | curses.A_BOLD)
        stdscr.addch(sh - 2, sw - 2, '+', curses.color_pair(1) | curses.A_BOLD)

        # Initialize paddles for a new match
        paddle1_y = sh // 2
        paddle2_y = sh // 2

        # Initialize ball away from paddles
        ball_y, ball_x = random.randint(2 * sh // 5, 3 * sh // 5), random.randint(2 * sw // 5, 3 * sw // 5)
        ball_dy, ball_dx = 1, 1  # Set a constant speed for the ball

        match_end_time = time.time() + 2  # 2 seconds delay before the next match

        while True:
            key = stdscr.getch()

            if key == ord('q'):
                break  # End the match if 'q' is pressed

            # Player 1 controls
            if key == ord('w') and paddle1_y > 2:
                paddle1_y -= 2
            elif key == ord('s') and paddle1_y < sh - 3:
                paddle1_y += 2

            # Player 2 controls
            elif key == curses.KEY_UP and paddle2_y > 2:
                paddle2_y -= 2
            elif key == curses.KEY_DOWN and paddle2_y < sh - 3:
                paddle2_y += 2

            ball_y += ball_dy
            ball_x += ball_dx

            # Ball collision with top and bottom walls
            if ball_y == 1 or ball_y == sh - 2:
                ball_dy = -ball_dy

            # Ball collision with paddles
            if ball_x == 2 and paddle1_y - 1 <= ball_y <= paddle1_y + paddle_length1:
                ball_dx = -ball_dx
            elif ball_x == sw - 3 and paddle2_y - 1 <= ball_y <= paddle2_y + paddle_length2:
                ball_dx = -ball_dx

            # Player 2 scores a point
            if ball_x == 1:
                score2 += 1
                break

            # Player 1 scores a point
            elif ball_x == sw - 2:
                score1 += 1
                break

            # Check if a power-up is present
            if power_up_present and ball_x == power_up_x and power_up_y >= paddle1_y and power_up_y <= paddle1_y + paddle_length1:
                # Player 1 catches the power-up
                paddle_length1 += 1
                power_up_present = False

            elif power_up_present and ball_x == power_up_x and power_up_y >= paddle2_y and power_up_y <= paddle2_y + paddle_length2:
                # Player 2 catches the power-up
                paddle_length2 += 1
                power_up_present = False

            # Generate a new power-up randomly
            if not power_up_present and random.random() < 0.01:
                power_up_y, power_up_x = random.randint(1, sh-2), random.randint(1, sw-2)
                power_up_present = True

            stdscr.clear()

            # Draw simplified border with colors
            for i in range(1, sh - 1):
                stdscr.addch(i, 0, '|', curses.color_pair(1) | curses.A_BOLD)
                stdscr.addch(i, sw - 1, '|', curses.color_pair(1) | curses.A_BOLD)

            for i in range(1, sw - 1):
                stdscr.addch(0, i, '-', curses.color_pair(1) | curses.A_BOLD)
                stdscr.addch(sh - 1, i, '-', curses.color_pair(1) | curses.A_BOLD)

            stdscr.addch(2, 2, '+', curses.color_pair(1) | curses.A_BOLD)
            stdscr.addch(2, sw - 2, '+', curses.color_pair(1) | curses.A_BOLD)
            stdscr.addch(sh - 2, 2, '+', curses.color_pair(1) | curses.A_BOLD)
            stdscr.addch(sh - 2, sw - 2, '+', curses.color_pair(1) | curses.A_BOLD)
            
            # Draw paddles with color
            for i in range(paddle_length1):
                stdscr.addch(paddle1_y - i, 2, '|', curses.color_pair(2))

            for i in range(paddle_length2):
                stdscr.addch(paddle2_y - i, sw - 3, '|', curses.color_pair(2))

            # Draw ball with color
            stdscr.addch(ball_y, ball_x, '*', curses.color_pair(3))

            # Draw scores with color
            stdscr.addstr(0, sw // 2 - 5, f"Player 1: {score1}  Player 2: {score2}", curses.color_pair(4))

            # Draw power-up if present
            if power_up_present:
                draw_power_up()

            stdscr.refresh()

        # Check if 'q' was pressed to end the game
        if key == ord('q'):
            break

        # Wait for the 2-second delay before starting the next match
        while time.time() < match_end_time:
            pass

# Run the curses application using curses.wrapper
curses.wrapper(main)
