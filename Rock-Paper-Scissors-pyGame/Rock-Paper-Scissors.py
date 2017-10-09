# -*- coding: utf-8 -*-
"""
@author: salimt
"""

import random
from time import sleep


def compHand(userHand):
    compChoise = {'Rock':'✊', 'Paper':'✋', 'Scissors':'✂'}
    compHand = random.choice(list(compChoise.keys()))
    if userHand == compHand:
        print('Thinking...')
        sleep(2)        
        print('AI has got the ' + compChoise.get(compHand))
        print('\x1b[1;31;43m' + 'Tie!' + '\x1b[0m')
    elif (userHand == 'Rock' and compHand == 'Scissors') or\
         (userHand == 'Paper' and compHand == 'Rock') or\
         (userHand == 'Scissors' and compHand == 'Paper'):             
             print('Thinking...')
             sleep(2)
             print('AI has got the ' + compChoise.get(compHand))
             print('\x1b[1;31;42m' + 'You Win!' + '\x1b[0m')
    else:
        print('Thinking...')
        sleep(2)        
        print('AI has got the ' + compChoise.get(compHand))
        print('\x1b[1;37;41m' + 'You Lost!' + '\x1b[0m')
    

def rockPaperScissors():
    user = input('Rock     -> R\nPaper    -> P\nScissors -> S\n>Your Choise: ')
    user = user.lower()
    print()  
    if user == 'r':
        user = 'Rock'
        print('You got the ✊ (Rock)')
        compHand(user)
        rockPaperScissors()
    elif user == 's':
        user = 'Scissors'
        print('You got the ✂ (Scissors)')
        compHand(user)
        rockPaperScissors()
    elif user == 'p':
        user = 'Paper'
        compHand(user)
        print('You got the ✋ (Paper)')
        compHand(user)
        rockPaperScissors()
    elif user == 'e':
        exit
    else:
        print('Invalid input!')
        rockPaperScissors()

if __name__ == '__main__':
    print('Welcome to the Game!' + ' "press e for exit"')
    rockPaperScissors()