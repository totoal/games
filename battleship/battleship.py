import os
import sys
import time
import random
import numpy as np
from getkey import getkey
from colorama import Fore, Style

if sys.platform == 'win32':
    def cls(): os.system('cls')
elif sys.platform == 'linux':
    def cls(): os.system('clear')
else:
    def cls(): os.system('clear')

global dic 
dic = {50: 'Carrier', 40: 'Battleship', 30: 'Cruiser', 21: 'Destroyer', 22: 'Destroyer', 11:'Submarine', 12: 'Submarine'}

def showBoard(vector, player): #player is a bool, which is true if the board being displayed is the human's
    print('  1  2  3  4  5  6  7  8  9  10')
    for i in range(1,11):
        toprint = chr(i+64)+' '
        for j in range(1,11):
            if vector[i][j] in list(dic.keys()) and not player:    #ship, undiscovered
                toprint+= Fore.BLACK  + '■  ' + Style.RESET_ALL
            elif vector[i][j] in list(dic.keys()) and player:      #ship, untouched
                toprint+= Fore.WHITE  + '■  ' + Style.RESET_ALL
            elif vector[i][j] in [-i for i in list(dic.keys())]:   #ship, hit
                toprint+= Fore.RED    + '■  ' + Style.RESET_ALL
            elif vector[i][j] == 1 and not player:                 #water, undiscovered
                toprint+= Fore.BLACK  + '■  ' + Style.RESET_ALL
            elif vector[i][j] == 1 and player:                     #water, untouched
                toprint+= Fore.CYAN   + '■  ' + Style.RESET_ALL 
            elif vector[i][j] == -1:                               #water, hit
                toprint+= Fore.BLUE   + '■  ' + Style.RESET_ALL
        print(toprint)

def hit(vec,letter,number):
    i = ord(letter) - 64
    j = number
    if vec[i][j] > 0:
        vec[i][j] *= -1        
        if vec[i][j] == -1:
            cls()
            print(Fore.BLUE + 'Miss' + Style.RESET_ALL)
        else:
            cls()
            print(Fore.RED + 'Hit!' + Style.RESET_ALL)
            if not checkRemain(vec, -1* vec[i][j]):
                if checkWin(vec):
                    return True, vec, True
        return True, vec, False
    return False, vec, False

def checkRemain(vec, key):
    if not key in vec: 
        print(Fore.BLUE + Style.BRIGHT +  str(dic[key]) +' was sunk!' + Style.RESET_ALL)
        return False
    return True

def checkWin(vec):
    for key in dic.keys():
        if key in vec: return False
    return True

def playerTurn(vec):
    flag = False
    while not flag:
        cls()
        showBoard(vec, False)
        print('It\'s your turn!')
        letter = input('What row (letter)?: ').upper()
        number = int(input('What column (number)?: '))
        flag, vec, winstate = hit(vec,letter,number)
        if flag == False: print('Invalid move, try again: ')
    
    print('Computer\'s board')
    showBoard(vec, False)
    input()
    return vec, winstate

def cpuTurn(vec):
    flag = False
    while not flag:
        cls()
        letter = chr(random.randint(1,10)+64)
        number = random.randint(1,10)
        flag, vec, winstate = hit(vec, letter, number)
    
    print('I attacked ', letter, number)
    print('Your board: ')
    showBoard(vec, True)
    input() 
    return vec, winstate

def checkEmpty(vector, length, direction, row, column):
    #0 = south, 1 = east
    if direction == 0:
        for i in range(column-1,column+1):
            for j in range(row-1, row+length+1):
                if not vector[j][i] == 1:
                    return False
    else:
        for i in range(row-1,row+1):
            for j in range(column-1, column+length+1):
                if not vector[i][j] == 1:
                    return False
    return True

def placeShip(vector, key, direction, row, column):
    #0 = south, 1 = east
    length = int(key/10)
    if direction == 0:
        for i in range(row, row+length):
            vector[i][column] = key
    else:
        for i in range(column, column+length):
            vector[row][i] = key
            
    return vector

def initCpu():
    cpu = np.ones((12,12))

    for key in dic.keys():
        length = int(key/10)
        empty = False
        while empty == False:
            dir = random.randint(0,1) #0 = south, 1 = east
            if dir == 0:
                letter = random.randint(1,10-length)
                number = random.randint(1,10)
            else: 
                letter = random.randint(1,10)
                number = random.randint(1,10-length)   

            if checkEmpty(cpu, length, dir, letter, number):
                cpu = placeShip(cpu, key, dir, letter, number)
                print('Placed ', dic[key])
                empty = True
    return cpu


def initPlayer():
    player = np.ones((12,12))
    for key in dic.keys():
        length = int(key/10)
        flag = False
        valid = False
        while flag == False and valid == False:
            cls()
            showBoard(player, True)
            print('Where do you to place', dic[key], '(length ', str(length)+')?: ')
            letter = ord(input('Row (Letter): ').upper())-64
            number = int(input('Column (Number): '))
            if not length == 1:
                dir    = int(input('Direction (0 = Vertical, 1 = Horizontal): '))
            else: dir = 0
            if letter in np.arange(1,11) and number in np.arange(1,11): valid = True
            if (letter > 11-length and dir == 0) or (number > 11-length and dir == 1): valid = False
            if valid == True:
                if checkEmpty(player, length, dir, letter, number):
                    player = placeShip(player, key, dir, letter, number)
                    print('Placed ', dic[key])
                    flag = True
                else: 
                    print('Invalid position - There must be at least 1 space between ships.')
                    valid = False
                    time.sleep(1.5)
            else: 
                print('Invalid position.')
                time.sleep(1)
    return player


def game():
    cpu        = initCpu()
    player     = initPlayer()
    winplayer  = False
    wincpu     = False
    while True:
        print('Computer\'s board:')
        showBoard(cpu, False)
        print()
        print('Your board:')
        showBoard(player, True)
        cpu, winplayer = playerTurn(cpu)
        if winplayer == True:
            print('You win!')
            break
        player, wincpu = cpuTurn(player)
        if wincpu == True:
            print('Computer wins!')
            break

game()