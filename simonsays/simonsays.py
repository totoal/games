import os
import sys
import time
import numpy as np
from getkey import getkey
from colorama import Fore, Style

if sys.platform == 'win32':
    def cls(): os.system('cls')
elif sys.platform == 'linux':
    def cls(): os.system('clear')
else:
    def cls(): os.system('clear')

def disp_butt(buttons, round):
    cls()
    print('Round ' + str(round))
    print('\n     ' + buttons[0] +
        '\n  ' + buttons[1] + '     ' + buttons[2]
        + '\n     '+ buttons[3])

def input_seq(seq_len):
    sequence = []
    for i in range(seq_len):
        sequence.append(getkey())
        print(' '.join(sequence), end = '\r')
    return sequence

def game(dt, round, seq):
    buttons = ['w', 'a', 'd', 's']
    disp_butt(buttons, round)
    time.sleep(dt)
    for event in seq:
        if event == 0:
            buttons[0] = Style.BRIGHT + Fore.RED + 'W' + Style.RESET_ALL
        if event == 1:
            buttons[1] = Style.BRIGHT + Fore.GREEN + 'A' + Style.RESET_ALL
        if event == 2:
            buttons[2] = Style.BRIGHT + Fore.YELLOW + 'D' + Style.RESET_ALL
        if event == 3:
            buttons[3] = Style.BRIGHT + Fore.BLUE + 'S' + Style.RESET_ALL
        disp_butt(buttons, round)
        time.sleep(dt*2)
        buttons = ['w', 'a', 'd', 's']
        disp_butt(buttons, round)
        time.sleep(dt)
        
    print('Input: ')
    in_seq = np.array(input_seq(len(seq)))
    in_seq[np.where(in_seq == 'w')] = 0
    in_seq[np.where(in_seq == 'a')] = 1
    in_seq[np.where(in_seq == 'd')] = 2
    in_seq[np.where(in_seq == 's')] = 3
    try: in_seq = in_seq.astype(int)
    except: return False

    return np.all(seq == in_seq)

if __name__ == '__main__':
    cls()
    print('Press any key to start')
    getkey()
    while True:
        round = 1
        win = True
        seq = []
        while win == True:
            seq.append(np.random.randint(0,4))
            win = game(0.3, round, seq)
            if win:
                print(Fore.GREEN + '\nNice!' + Style.RESET_ALL)
                time.sleep(1.5)
            round += 1
            if not win: break
        print(Fore.RED + '\nYou lost :(' + Style.RESET_ALL)
        ng = '0'
        while ng != 'y' and ng != 'n':
            ng = input('Play again? y/n ')
        if ng == 'n': break
