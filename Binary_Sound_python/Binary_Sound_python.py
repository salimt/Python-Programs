# -*- coding: utf-8 -*-
"""
@author: salimt
"""

import winsound
import time

print("Binary Representation of sound")

print("Enter the duration of each note (in ms)?")
print("e.g. 200")
rate = int(input(">"))

#print("Enter a 4-bit binary note")
#print("Or more than one note separated by spaces")


print("Notes:")
print("0000 = no sound")
print("0001 = Low C")
print("0010 = D")
print("0011 = E")
print("0100 = F")
print("0101 = G")
print("0110 = A")
print("0111 = B")
print("1000 = High C")


print("e.g: ")
print("0101 0101 0101 0010 0011 0011 0010 0000 0111 0111 0110 0110 0101")
soundBinary = input(">")

for note in soundBinary.split():

    if note ==   "0000":        #rest
        freq = 37
    elif note == "0001":        #low c
        freq = 262
    elif note == "0010":        #d
        freq = 294
    elif note == "0011":        #e
        freq = 330
    elif note == "0100":        #f
        freq = 349
    elif note == "0101":        #g
        freq = 392
    elif note == "0110":        #a
        freq = 440
    elif note == "0111":        #b
        freq = 494
    elif note == "1000":        #high c
        freq = 523
        
    winsound.Beep(freq, rate)
    print('♫', end=" ")