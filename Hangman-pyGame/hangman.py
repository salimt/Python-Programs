# -*- coding: utf-8 -*-
"""
@author: salimt
"""
import sys, random

hangman0 = ([[' ', ' ', ' ', ' ', '+', '-', '-', '-', '+'],
             [' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', '|'],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
             ['=', '=', '=', '=', '=', '=', '=', '=', '=', '=']])


words = 'ant badger bat bear camel cat clam cobra cougar crow dog donkey duck ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()
#words = 'moose moose geeas'.split()

def getRandomWord(wordList):
     # This function returns a random string from the passed list of strings.
     wordIndex = random.randint(0, len(wordList) - 1)
     return wordList[wordIndex]

word = getRandomWord(words)
#print(word)
print('HINT: An Animal')
space = ['_'] * len(word)
print(' '.join(''.join(map(str,w)) for w in space))

# make an iteration with for in
result = "\n".join("".join(map(str,l)) for l in hangman0)
print(result)


def hangman(x):
    #hanging the man step by step
    if x == 'wrong1':
        for i in hangman0:
            hangman0[2][4] = 'O'
    if x == 'wrong2':
        for i in hangman0:
            hangman0[3][4] = '|'
    if x == 'wrong3':
        for i in hangman0:
            hangman0[3][3] = '/'
    if x == 'wrong4':
        for i in hangman0:
            hangman0[3][5] = "\\"
    if x == 'wrong5':
        for i in hangman0:
            hangman0[4][3] = '/'
    if x == 'wrong6':
        print('THE WORD WAS: ' + ' '.join(map(str,word)))
        for i in hangman0:            
            hangman0[4][5] = "\\"
            hangman0[5][1:8:2] = "DEAD"
    checkWord()
    #return print("\n".join("".join(map(str,l)) for l in hangman0))


space = ['_'] * len(word)
def checkWord():
    # check word how many are there and place it in it's place
    #finder = word.find(letter)
    finder = find(word, letter)
    for c in range(len(finder)):
        finderN = finder[c]
        space[finderN] = letter
    print(' '.join(''.join(map(str,w)) for w in space))
        
    hangy = "\n".join("".join(map(str,l)) for l in hangman0)
    print(hangy)

def find(s, ch):
    #find the places of chars in string
    return [i for i, ltr in enumerate(s) if ltr == ch]

x = 0
w = 0
foundOnes = []
while True:
    letter = input('Letter: ')  
    letter = letter.lower()
    while (not letter.isalpha()) or len(letter) != 1:
            letter = input('Letter: ')  
            letter = letter.lower()
    if letter in foundOnes:
        print('You Already Got That One!')
        continue
    elif letter in word:
        #print(letter)
        moreLetters = find(word, letter)
        moreLetters = len(moreLetters)
        checkWord()
        foundOnes.append(letter)
        #print(foundOnes)
        w +=  moreLetters
        if w == len(word):
            print('!! CONGRATZ !!')
            sys.exit()
    elif x == 5:
        hangman('wrong' + str(x+1))
        x += 1
        #print(x, "tr")
        break
    else:
        hangman('wrong' + str(x+1))
        #print(x, "wr")
        x += 1
    
