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
        return 'tie'
    elif (userHand == 'Rock' and compHand == 'Scissors') or\
         (userHand == 'Paper' and compHand == 'Rock') or\
         (userHand == 'Scissors' and compHand == 'Paper'):             
             print('Thinking...')
             sleep(2)
             print('AI has got the ' + compChoise.get(compHand))
             print('\x1b[1;31;42m' + 'You Win!' + '\x1b[0m')
             return True
    else:
        print('Thinking...')
        sleep(2)        
        print('AI has got the ' + compChoise.get(compHand))
        print('\x1b[1;37;41m' + 'You Lost!' + '\x1b[0m')
        return False
    

def rockPaperScissors():
    userP = 0
    compP = 0
    while True:
        print('User: ' + str(userP) + ' Computer: ' + str(compP))
        print()
        user = input('Rock     -> R\nPaper    -> P\nScissors -> S\n>Your Choise: ')        
        user = user.lower()
        print()  
        if user == 'r':
            user = 'Rock'
            print('You got the ✊ (Rock)')
            #compHand(user)
            a = compHand(user)
            if a == 'tie':
                pass
            elif a:
                userP += 1
            else:
                compP += 1
            continue
        elif user == 's':
            user = 'Scissors'
            print('You got the ✂ (Scissors)')
            #compHand(user)
            a = compHand(user)
            if a == 'tie':
                pass
            elif a:
                userP += 1
            else:
                compP += 1
            continue
        elif user == 'p':
            user = 'Paper'
            print('You got the ✋ (Paper)')
            #compHand(user)
            a = compHand(user)
            if a == 'tie':
                pass
            elif a:
                userP += 1
            else:
                compP += 1
            continue
        elif user == 'e':
            break
        elif user == 'reset':
            compP = 0
            userP = 0
        else:
            print('Invalid input!')
            continue
        
        
if __name__ == '__main__':
    print('Welcome to the Game!\n' +\
          ' "press e for exit" or "type `reset` to reset scores"')
    rockPaperScissors()