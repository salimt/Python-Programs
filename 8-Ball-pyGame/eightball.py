# -*- coding: utf-8 -*-
"""
@author: salimt
"""

import random
import time
 
list = ["Yes, most definitely!", "The chances are high!", "Not likely!", "May the odds be ever in your favor.",
                        "You got no shot, kid.", "Try it out and see!", "23% of working", "99.9% success rate",
                        "Congratulations, yes!", "Ask a probably question," "Ask again later", "Better not tell you now",
           "Cannot predict now", "Concentrate and ask again", "Don't count on it"
        ]

done = True
while done:
    question = input('Enter your question: ')
    print('>Q: ' + question)
    print('Thinking...')
    time.sleep(3)
    print('>A: ' + random.choice(list))
    print('Would you like to play again? yes/no')
    playAgain = input('> ')
    if playAgain == 'yes' or playAgain == 'y':
        continue
    else:
        print("Well, that's a shame! Next Time...")
        done = False