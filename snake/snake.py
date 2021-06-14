############################
''' UNDER CONSTRUCTION '''
############################

import numpy as np
import os
import sys
import time
import queue
from threading import Thread
from getkey import getkey

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
    bdim = 5
    board = np.zeros(bdim**2).reshape((bdim, bdim)).astype(int)
    #Init snake
    slen = 2
    board[int(bdim/2), int(bdim/2)] = 1
    board[int(bdim/2) + 1, int(bdim/2)] = 2
    vi = np.array([-1, 0])
    return board, vi, slen

q = queue.Queue()

def go_snek(board, slen):
    t_frame = 0.3
    while True:
        head_goto = np.array(np.where(board == 1)).flatten()  # Store where the head should go
        head_goto = tuple(head_goto + v)
        board_tmp = np.copy(board)
        for n in range(1, slen+1):  # Move each part to the next position
            board_tmp[np.where(board == n)] += 1
        board = board_tmp
        if board[head_goto] == -1: yummy = True
        else: yummy = False

        board[head_goto] = 1 # Place the head

        if yummy:
            board = spawn_fruit(board)
        if not yummy:
            board[np.where(board == slen+1)] = 0 # Remove the tail
        disp_board(board)
        q.put(board)
        time.sleep(t_frame)

def disp_board(board):
    cls()
    print(board.transpose())

def turn_snek(v):
    turn = getkey()
    if turn == 'w':
        v_f = [-1, 0]
    if turn == 's':
        v_f = [1, 0]
    if turn == 'a':
        v_f = [0, 1]
    if turn == 'd':
        v_f = [0, -1]
    v_f = np.array(v_f)

    if v_f.dot(v) == 0: return v_f
    else: return v

if __name__ == '__main__':
    board, v, slen = init()
    board = spawn_fruit(board)
    
    thr1 = Thread(target=go_snek, args=(board, slen))
    thr1.start()

    while True:
        v = turn_snek(v)
