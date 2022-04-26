#!/usr/bin/python3
letter = 97
while (letter < 123):
    if letter != 113 and letter != 101:
        print("{0}".format(chr(letter)), end="")
    letter = letter + 1
