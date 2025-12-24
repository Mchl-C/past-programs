def check_winner():
    # Check rows and columns
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2] != ' ':
            return 1 if grid[i][0] == sym_1 else 2
        if grid[0][i] == grid[1][i] == grid[2][i] != ' ':
            return 1 if grid[0][i] == sym_1 else 2
    
    # Check diagonals
    if (grid[0][0] == grid[1][1] == grid[2][2] != ' ') or \
       (grid[0][2] == grid[1][1] == grid[2][0] != ' '):
        return 1 if grid[1][1] == sym_1 else 2
    
    return 0

grid = [[' ',' ',' '],
        [' ',' ',' '],
        [' ',' ',' ']]

turn = False
sym_1 = input("Player 1 choose a single char as symbol: ").strip()
sym_2 = input("Player 2 choose a single char as symbol: ").strip()
win = 0
moves = 0

while True:
    # Print the board
    for row in range(3):
        print('|', end='')
        for col in range(3):
            print(grid[row][col], end='|')
        print()
        print('-' * 7)
        
    # Check for a winner or draw
    win = check_winner()
    if win:
        print(f"Winner is: Player {win}")
        break
    if moves == 9:
        print("It's a draw!")
        break
    
    # Player input
    player = 2 if turn else 1
    n = int(input(f"Player {player} pick a pos[1-9]: "))
    r = (n-1) // 3
    c = (n-1) % 3
    
    if grid[r][c] != ' ':
        print("Invalid move")
    else:
        grid[r][c] = sym_2 if turn else sym_1
        moves += 1
        turn = not turn
