############################
''' UNDER CONSTRUCTION '''
############################

import numpy as np
import os
import sys

if sys.platform == 'win32':
    def cls(): os.system('cls')
elif sys.platform == 'linux':
    def cls(): os.system('clear')
else:
    def cls(): os.system('clear')

def spawn_fruit(board):
    # -1 means fruit
    while True:
        fruit_pos = (
                np.random.randint(0, len(board)),
                np.random.randint(0, len(board))
                )
        if board[fruit_pos] == 0:
            board[fruit_pos] = -1
            break
    return board

def init():
    bdim = 15
    board = np.zeros(bdim**2).reshape((bdim, bdim))
    #Init snake
    board[int(bdim/2), int(bdim/2)] = 1
    board[int(bdim/2) + 1, int(bdim/2)] = 2
    return board

if __name__ == '__main__':
    board = init()
    board = spawn_fruit(board)
    print(board)
