import sys
import os
from colorama import Fore, Style
import time
import numpy as np

words = open('listofwords.txt', 'r').read().split('\n')

if sys.platform == 'win32':
    def cls(): os.system('cls')
elif sys.platform == 'linux':
    def cls(): os.system('clear')
else:
    def cls(): os.system('clear')

# def exception():
    # # cls()
    # if input("Error - Press q to quit or any key to continue: ") != 'q': return True
    # else: exit()

uengess = '''
                 |
                 |
    --------------------------
    /           /          /
   /       ---------      /
  /           /          /
 /         -----        /
/           /          /
'''

# 0 is the pole and 1-7 stages
hm_stages = [
'''
|-------
|      |
|
|
|
|
|
|
===========
''',
'''
|-------
|      |
|      O
|
|
|
|
|
===========
''',
'''
|-------
|      |
|      O
|      |
|
|
|
|
===========
''',
'''
|-------
|      |
|      O
|     /|
|      
|
|
|
===========
''',
'''
|-------
|      |
|      O
|     /|\\
|
|
|
|
===========
''',
'''
|-------
|      |
|      O
|     /|\\
|      |
|
|
|
===========
''',
'''
|-------
|      |
|      O
|     /|\\
|      |
|     /
|
|
===========
''',
'''
|-------
|      |
|      O
|     /|\\
|      |
|     / \\
|
|
===========
'''
]
def selection():
    cls()
    i = 0
    while i != 1 and i != 2:
        print('How many players? (1-2):')
        try: i = int(input())
        except: 
            print(Fore.RED + 'ERROR' + Style.RESET_ALL)
            time.sleep(1)
            continue
    return i

def names():
    valid_word = False
    while valid_word == False:
        print('Player 1 name:')
        player1name = input()
        if player1name.isalpha():
                valid_word = True
    valid_word = False
    while valid_word == False:
        print('Player 2 name:')
        player2name = input()
        if player2name == player1name:
            print('Both players cannot have the same name')
            continue
        if player2name.isalpha():
                valid_word = True

    if player1name.upper() == 'PLAYER' or player2name.upper() == 'PLAYER':
        print('Very unoriginal names...')

    players=[player1name.upper(),player2name.upper()]
    if 'JORGE' in players and 'ALBERTO' in players:
        print('FANE OHTANIA MANQUE PIERDA')
        print('')
        print(uengess)
        input()
        if player1name.upper() == 'JORGE':
            player1name = 'Gorgues'
            player2name = 'A el Berto'
        else:
            player2name = 'Gorgues'
            player1name = 'A el Berto'

    
    player1name = Fore.YELLOW + player1name + Style.RESET_ALL
    player2name = Fore.CYAN + player2name + Style.RESET_ALL
    
    return player1name, player2name

def display_score(name1, name2, score1, score2,
        current, rounds):
        scores = name1 + ' ' + str(score1) + '-' + str(score2) + ' ' + name2
        cls()
        print((' SCORE ').center(30, '='))
        print(scores.center(48,' '))
        print(('').center(30,'='))

def update_stage(stage, wordlen, letters, positions, missed, playername):
    cls()
    print(playername)
    print(hm_stages[stage])
    output = list('_' * wordlen)
    
    for i in range(len(letters)):
        for j in range(len(positions[i])):
            output[positions[i][j]] = str(letters[i])
    print(Fore.RED+'\r'+', '.join(missed))
    print(Style.RESET_ALL)
    print(' '.join(output))

def game(playername):
    cls()
    valid_word = False
    while valid_word == False:
    #     print('Enter word:')
    #     word = input().upper()
        word = words[np.random.randint(0,len(words))].upper()
        if word.isalpha():
            valid_word = True
        if not word.isalpha():
            print(Fore.RED+'Enter a valid word with no spaces')
            print(Style.RESET_ALL)
    wordlen = len(word)

    cls()
    
    stage = 0
    positions = []
    letters = []
    missed = []

    print(playername)
    print(hm_stages[0])
    print('_ ' * wordlen)

    while stage < 7:
        update_stage(stage, wordlen, letters, positions, missed, playername)
        print('Letter: ')
        guess = input().upper()
     
        if guess.isalpha() and len(guess) == 1:
            pass
        else:
            print('NOT VALID')
            time.sleep(1)
            continue
        
        if guess in letters or guess in missed:
            print('REPEATED LETTER')
            time.sleep(1)
            continue
     
        pos =[i for i, ltr in enumerate(word) if ltr == guess] 
        if len(pos) == 0:
            stage += 1
            print(stage)
            missed.append(guess)
            continue
        letters.append(guess)
        positions.append(pos)
        
        completion = 0
        
        for item in positions:
            completion += len(item)
        if completion == wordlen:
            break

    if stage  == 7:
        cls()
        print(playername)
        print(hm_stages[-1])
        print( ' '.join(list(word)))
        print(Fore.RED+':-( You lost.')
        print(Style.RESET_ALL)
        input()
        return False
    elif stage >= 0 and stage < 7:
        update_stage(stage, wordlen, letters, positions, missed, playername)
        print(Fore.GREEN+':-D You win.')
        print(Style.RESET_ALL)   
        input()
        return True

if __name__ == '__main__':
    players = selection()
    if players == 1:
        ng = 'y'
        won = 0
        lost = 0
        streak = 0
        while ng != 'n':
            if game(' '):
                won += 1
                streak += 1
            else:
                lost += 1
                streak = 0
            print(Fore.GREEN + 'Guessed: ' + str(won) + '\n'
                + Fore.RED + 'Failed: ' + str(lost) + '\n'
                + Style.RESET_ALL + 'Streak: ' + str(streak))
            ng = '0'
            while ng != 'y' and ng != 'n':
                    ng = input('\nPlay again? y/n: ')
            if ng == 'n':
                exit()
    if players == 2:
        while True:
            name1, name2 = names()
            rounds = 0
            score1  = 0
            score2  = 0
            while rounds < 1:
                try: rounds = int(input('Number of rounds: '))
                except: continue
            current = 1
            display_score(name1, name2, score1, score2, current, rounds)
            print('\n\nRound '+str(current) + '/' + str(rounds) 
                + ' - '+ name1 +'\'s turn.')
            input('\n(Press return)')
            while current <= rounds:
                if game(name1):
                    score1 += 1
                display_score(name1, name2, score1, score2, current, rounds)
                print('\n\nRound '+str(current) + '/' + str(rounds) 
                    + ' - '+ name2 +'\'s turn.')
                input('\n(Press return)')
                if game(name2):
                    score2 += 1
                display_score(name1, name2, score1, score2, current, rounds)
                if current != rounds:
                    print('\n\nRound '+str(current + 1) + '/' + str(rounds) 
                        + ' - '+ name1 +'\'s turn.')
                    input('\n(Press return)')
                current+=1
            
            if score1 > score2:
                print('\nThe winner is '+str(name1)+'!')
            elif score1 < score2:
                print('\nThe winner is '+str(name2)+'!')
            else:
                print('\nIt\'s a tie ¯\_(ツ)_/¯')
            time.sleep(2)
            while ng != 'y' and ng != 'n':
                print('Play again? y/n')
                ng = input()
            if ng == 'n':
                exit()
            if ng == 'y' or ng == '':
                continue
