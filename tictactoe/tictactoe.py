import sys
import os
from colorama import Fore, Style
import time
import numpy as np

if sys.platform == 'win32':
    def cls(): os.system('cls')
elif sys.platform == 'linux':
    def cls(): os.system('clear')
else:
    def cls(): os.system('clear')

def exception():
    cls()
    if input("Error - Press q to quit or any key to continue: ") != 'q': return True
    else: exit()

def printboard(state): 
    rows = []
    horizontal='———+———+———'
    for r in range(0,3):
        stringtoprint = ' '
        for i in range(0,3):
            if state[3*r + i] == 0:
                stringtoprint += ' '
            elif state[3*r + i] == 1:
                stringtoprint += 'X'
            elif state[3*r + i] == 2:
                stringtoprint += 'O'
            stringtoprint += ' '
            if i != 2: stringtoprint += '| '
        print(stringtoprint)
        if r != 2: print(horizontal)

def checkwinner(state):
    if not state[0]==0 and state[0] == state[1] and state[0] == state[2]: return state[0]
    if not state[0]==0 and state[0] == state[3] and state[0] == state[6]: return state[0]
    if not state[0]==0 and state[0] == state[4] and state[0] == state[8]: return state[0]
    if not state[1]==0 and state[1] == state[4] and state[1] == state[7]: return state[1]
    if not state[2]==0 and state[2] == state[4] and state[2] == state[6]: return state[2]
    if not state[2]==0 and state[2] == state[5] and state[2] == state[8]: return state[2]
    if not state[3]==0 and state[3] == state[4] and state[3] == state[5]: return state[3]
    if not state[6]==0 and state[6] == state[7] and state[6] == state[8]: return state[6]
    return 0

    
def game():
    state = [0]*9
    turn  = 1 
    while 0 in state:
        player = 2 if turn%2 == 0 else 1 
        i = -1
        while not state[i] == 0 or i==-1:
            cls()  
            printboard(state)
            if i ==-1: print("Player "+str(player)+"'s move")
            else: print("Invalid move")
            try: r = int(input("Row:")) 
            except: 
                if exception(): continue
            try: c = int(input("Column:")) 
            except: 
                if exception(): continue
            if r < 1 or r > 3 or c < 1 or c > 3: 
                print("Invalid move")
                continue
            i = 3*(r-1)+(c-1)
        state[i] = player
        check = checkwinner(state)
        if check != 0:
            print("Player "+str(check)+" wins!")              
            printboard(state)
            break
        turn += 1
    if not 0 in state: 
        print("It's a tie ¯\_(ツ)_/¯") 
        printboard(state)

game()