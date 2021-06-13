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

# def exception():
    # cls()
    # if input("Error - Press q to quit or any key to continue: ") != 'q': return True
    # else: exit()

def printboard(state): 
    cls()
    print(('_________________'))
    for r in range(5,-1,-1):
        thisrow = '| '
        for c in range(0,7):
            if state[r][c]   == 1: thisrow += Fore.RED + '◍ ' + Style.RESET_ALL
            elif state[r][c] == 2: thisrow += Fore.YELLOW + '◍ ' + Style.RESET_ALL
            else: thisrow += '○ '
        print((thisrow+ '|'))
    print(('|———————————————|'))
    print(('| 1 2 3 4 5 6 7 |'))
    print(('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾'))


def fill(player,state,column):
    for i in range(0,6):
        if state[i][column-1] == 0: 
            state[i][column-1] = player
            return True
    print("Full column, choose a different one.")
    return False

def checkwin(state):
    for r in range(0,6):
        for c in range(0,7):
            if state[r][c] == 0: continue
            if r < 3:
                if (
                        state[r][c] == state[r+1][c] and
                        state[r][c] == state[r+2][c] and
                        state[r][c] == state[r+3][c]
                    ):
                    return state[r][c]
                if c < 4:
                    if (
                            state[r][c] == state[r+1][c+1] and
                            state[r][c] == state[r+2][c+2] and
                            state[r][c] == state[r+3][c+3]
                        ):
                        return state[r][c]
                if c > 2:
                    if (
                            state[r][c] == state[r+1][c-1] and
                            state[r][c] == state[r+2][c-2] and
                            state[r][c] == state[r+3][c-3]
                        ):
                        return state[r][c]
            if c < 4:
                if (
                        state[r][c] == state[r][c+1] and
                        state[r][c] == state[r][c+2] and
                        state[r][c] == state[r][c+3]
                        ):
                    return state[r][c]
    return 0        
    


def game():
    state = np.zeros((6,7))
    turn = 1
    while True:
        playerstring = {
                1: Fore.RED + 'Player 1' + Style.RESET_ALL,
                2:Fore.YELLOW + 'Player 2' + Style.RESET_ALL
                }
        while True:
            printboard(state)
            print(playerstring[2-turn%2] + '\'s turn.')
            try: c = int(input('Where do you want to place your disc?: '))
            except: continue
            if c > 7 or c<1: continue
            if fill(2-turn%2,state,c):
                break
        win = checkwin(state)
        if win == 1: 
            printboard(state)
            print(Fore.RED + '\nPlayer 1 wins!' + Style.RESET_ALL)
            break
        if win == 2: 
            printboard(state)
            print(Fore.YELLOW + '\nPlayer 2 wins!' + Style.RESET_ALL)
            break
        if turn == 42:
            printboard(state)
            print('\nIt\'s a tie ¯\_(ツ)_/¯')
            break
        turn+=1

if __name__ == '__main__':
    game()
    while True:
        ng = input('\nPlay again? [Y/N]: ')
        if ng.lower() == 'y':
            game()
        if ng.lower() == 'n':
            break
        else:
            continue
