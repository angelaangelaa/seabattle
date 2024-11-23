
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

        
