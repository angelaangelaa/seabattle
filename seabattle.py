
import os
import random

board_size = 7
empty = "~"  
miss = "O"   
hit = "X"   
sunk = "#"  

board = [[empty] * board_size for _ in range(board_size)]
player_board = [[empty] * board_size for _ in range(board_size)]

ships = []
ship_sizes = [3, 2, 2, 1, 1, 1, 1]

for size in ship_sizes:
    while True:
        direction = random.choice(["H", "V"])
        if direction == "H":
            row, col = random.randint(0, board_size - 1), random.randint(0, board_size - size)
            ship = [(row, col + i) for i in range(size)]
        else:
            row, col = random.randint(0, BOARD_SIZE - size), random.randint(0, BOARD_SIZE - 1)
            ship = [(row + i, col) for i in range(size)]
        if all(0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and board[r][c] == EMPTY for r, c in ship) and \
            all(board[r + dr][c + dc] == EMPTY for r, c in ship for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)] 
                if 0 <= r + dr < BOARD_SIZE and 0 <= c + dc < BOARD_SIZE):
            for r, c in ship:  
                board[r][c] = "S"
            ships.append(ship)  
            break

player_name = input("Please, enter your name: ")

shots = 0
sunk_ships = 0

while sunk_ships < len(ships):
    os.system('cls' if os.name == 'nt' else 'clear')  
    print("   " + " ".join("abcdefg"[:board_size]))
    for i, row in enumerate(player_board):
        print(f"{i + 1:2} " + " ".join(row))
        
    while True:
        shot = input("your shot (e.g., b5): ").lower()
        if len(shot) == 2 and "a" <= shot[0] <= "g" and "1" <= shot[1] <= str(board_size):
            row, col = int(shot[1]) - 1, ord(shot[0]) - 97
            break
        print("invalid input!")

    if player_board[row][col] != empty:
        print("you already shot here!")
        continue

    shots += 1
        if board[row][col] == "s":
            player_board[row][col] = hit
            for ship in ships:
                if all(player_board[r][c] == hit for r, c in ship):
                    for r, c in ship:
                        player_board[r][c] = sunk
                    sunk_ships += 1
                    print("ship sunk!")
                    break
            else:
                print("hit!")
        else:
            player_board[row][col] = miss
            print("miss!")
