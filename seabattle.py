
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
