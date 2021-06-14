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

def menu(dic):
    print("\n0 - Close Program")
    for i in range(1,len(dic)+1):
        print(i,"-", dic[i].title())

def selector(i, dic):
    if i == 0: exit()
    return dic[i]

dic = {
    1: 'hangman',
    2: 'tic-tac-toe',
    3: 'connect4',
    4: 'snake'
}

while True:
    cls()
    print(Fore.GREEN + 'WELCOME TO OHTANIA GAMES' + Style.RESET_ALL+'\nWhat do you want to play?')
    menu(dic)
    while True:
        try: choice = int(input())
        except:
            print(Fore.RED + 'Bad selection' + Style.RESET_ALL)
            continue
        if choice > len(dic) or choice < 0: 
            print(Fore.RED + 'Bad selection' + Style.RESET_ALL)
            continue
        break
    if choice == 0:  sys.exit()
    os.chdir(selector(choice,dic))
    print(Fore.GREEN + selector(choice,dic).title() + Style.RESET_ALL)
    time.sleep(1.5)
    exec(open(selector(choice,dic)+'.py').read())
    cls()
    os.chdir('..')
    # ng = input('\nPlay something else? [Y/N]: ')
    # if ng.lower() == 'y':
        # continue
    # if ng.lower() == 'n':
        # exit()
    # else:
        # continue
