import numpy as np
import os
import sys
import time
from colorama import Fore, Style
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
    bdim = 15
    board = np.zeros(bdim**2).reshape((bdim, bdim)).astype(int)
    #Init snake
    slen = 2
    board[int(bdim/2), int(bdim/2)] = 1
    board[int(bdim/2) + 1, int(bdim/2)] = 2
    vi = np.array([-1, 0])
    return board, vi, slen

def turn_snek(v):
    turn = getkey()
    if turn == 'w':
        v_f = [0, -1]
    if turn == 's':
        v_f = [0, 1]
    if turn == 'a':
        v_f = [-1, 0]
    if turn == 'd':
        v_f = [1, 0]
    try: v_f = np.array(v_f)
    except: return v
    
    if v.dot(v_f) == 0: return v_f
    else: return v

def go_snek(board, slen):
    t_frame = 0.3
    last_v = v
    while True:
        this_v = v
        if last_v.dot(this_v) == -1:
            this_v = last_v
        
        head_goto = np.array(np.where(board == 1)).flatten()  # Store where the head should go
        head_goto = head_goto + this_v
        
        if np.any(head_goto < 0) or np.any(head_goto >= len(board)):
            break
        head_goto = tuple(head_goto)
        if board[head_goto] > 0:
            break
        
        board_tmp = np.copy(board)
        for n in range(1, slen+1):  # Move each part to the next position
            board_tmp[np.where(board == n)] += 1
        board = board_tmp
        if board[head_goto] == -1: yummy = True
        else: yummy = False
        
        board[head_goto] = 1 # Place the head
        
        if yummy:
            board = spawn_fruit(board)
            slen += 1
        if not yummy:
            board[np.where(board == slen+1)] = 0 # Remove the tail
        disp_board(board)
        last_v = this_v
        time.sleep(t_frame)
    print(Fore.RED + 'GAME OVER ' + Style.RESET_ALL)
    return

def disp_board(board):
    cls()
    graphics[board ==  0] = ' '
    graphics[board >=  1] = '■'
    graphics[board == -1] = '•'

    print(' ' + '= '*len(board))
    for line in graphics.transpose():
        print('|' + ' '.join(line) + '|')
    print(' ' + '= '*len(board))

if __name__ == '__main__':
    ng = 'init'
    while ng != 'n':
        ng = 'init'
        board, v, slen = init()
        board = spawn_fruit(board)
        graphics = np.copy(board).astype(str)

        thr1 = Thread(target=go_snek, args=(board, slen))
        thr1.start()
        
        while thr1.is_alive():
            v = turn_snek(v)
        while ng != 'y' and ng != 'n':
            ng = input('Play again? y/n\n')
