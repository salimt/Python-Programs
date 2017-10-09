# -*- coding: utf-8 -*-
"""
@author: salimt
"""

"""
(0,0) | (0,1) | (0,2)
---------------------
(1,0) | (1,1) | (1,2)
---------------------
(2,0) | (2,1) | (2,2)
"""

import sys
import random
import time

board  = [["_", "_", "_"], 
          ["_", "_", "_"], 
          ["_", "_", "_"]]
board2 = [["1", "2", "3"], 
          ["4", "5", "6"], 
          ["7", "8", "9"]]
taken  = []

gams = input('Single Player or Two Players? (s/t) \n>')

def turn(board, board2, pos1):
    for i in range(len(board2)):
        for n in range(len(board2[i])):
            if board2[i][n] == str(pos1):
                board2[i][n] = a
                board[i][n] = a
    for i in board:
        print("|".join(i))
    return board, board2, pos1


def player(board, board2, pos1):
    if gams == 't':
        if pos1 not in taken:
            taken.append(pos1)
            board, board2, pos1 = turn(board, board2, pos1)
            return board, board2, taken
    else:       
        sampo = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]       
        #pos1 = "".join(random.sample(["1", "2", "3", "4", "5", "6", "7", "8", "9"], 1))
        sampo = list(set(sampo) - set(taken))        
        pos1 = "".join(random.choice(sampo))        
        if pos1 not in taken:
            print()
            print('Thinking...')
            time.sleep(2)
            print("AI made it's move: " + pos1)
            #print()
            taken.append(pos1)
            board, board2, pos1 = turn(board, board2, pos1)
            return board, board2, taken


    
def wingame(board2, pos1):
    for i in range(3):    
        if "XXX" == str("".join(board2[i][0:3])) or "XXX" ==(board2[0][i] + board2[1][i] + board2[2][i]) or (
                board2[0][0] + board2[1][1] + board2[2][2]) == "XXX" or (
                board2[0][2] + board2[1][1] + board2[2][0]) == "XXX":
            print('\x1b[7;37;46m' + ' victory for X ' + '\x1b[0m')
            #print("victory for X")
            sys.exit()
            
    for i in range(3):  
        if "OOO" == str("".join(board2[i][0:3])) or "OOO" ==(board2[0][i] + board2[1][i] + board2[2][i]) or (
                board2[0][0] + board2[1][1] + board2[2][2]) == "OOO" or (
                board2[0][2] + board2[1][1] + board2[2][0]) == "OOO":
            print('\x1b[7;37;46m' + ' victory for O ' + '\x1b[0m')
            #print("victory for O")
            sys.exit()    


print('HINT')
print('1|2|3\n\
4|5|6\n\
7|8|9')


game = True
move = 0
while game:
    if gams == 't':
        a = 'X'
        pos1 = input('>P1: ')
        if pos1 not in taken:
            move += 1       
        player(board,board2,pos1)
        wingame(board2, pos1)
        print(move)     
        if move == 9:
            print('nobody wins')
            game = False
            sys.exit()
    
        a = 'O'
        pos1 = input('>P2: ')
        if pos1 not in taken:
            move += 1
        player(board,board2,pos1)
        wingame(board2, pos1)
        
    else:
        a = 'X'
        p1 = True
        while p1:
            pos1 = input('>P1: ')
            board, board2, pos1 = turn(board, board2, pos1)
            if not pos1 in taken:
                taken.append(pos1)
                p1 = False
        if pos1 not in taken:
            move += 1        
        #board, board2, pos1 = turn(board, board2, pos1)
        wingame(board2, pos1)
        move += 1
        if move == 9:
            print('\x1b[7;36;47 m' + ' nobody wins! ' + '\x1b[0m')
            #print('nobody wins')
            game = False
            sys.exit()
        a = 'O'
        player(board,board2,pos1)
        wingame(board2, pos1)
        move += 1 
        #print(move)     