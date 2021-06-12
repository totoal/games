import sys
import os
from colorama import Fore, Style
import time
import numpy as np

words = open("listofwords.txt", "r").read().split("\n")

if sys.platform == 'win32':
    def cls(): os.system('cls')
elif sys.platform == 'linux':
    def cls(): os.system('clear')
else:
    def cls(): os.system('clear')

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

def update_stage(stage, wordlen, letters, positions, missed):
    cls()
    print(hm_stages[stage])
    output = list('_' * wordlen)
    
    for i in range(len(letters)):
        for j in range(len(positions[i])):
            output[positions[i][j]] = str(letters[i])
    print(Fore.RED+'\r'+', '.join(missed))
    print(Style.RESET_ALL)
    print(' '.join(output))

def game():
    cls()
    # valid_word = False
    # while valid_word == False:
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

    print(hm_stages[0])
    print('_ ' * wordlen)

    while stage < 7:
        update_stage(stage, wordlen, letters, positions, missed)
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
        print(hm_stages[-1])
        print( ' '.join(list(word)))
        print(Fore.RED+':-( You lost.')
        print(Style.RESET_ALL)
    elif stage >= 0 and stage < 7:
        update_stage(stage, wordlen, letters, positions, missed)
        print(Fore.GREEN+':-D You win.')
        print(Style.RESET_ALL)


if __name__ == '__main__':
    game()
    ng = '0'
    while ng != 'n':
        print('Play again? y/n')
        ng = input()

        if ng == 'y':
            game()
        if ng == 'n':
            break
        else:
            continue
