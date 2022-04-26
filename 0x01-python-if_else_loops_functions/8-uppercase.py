#!/usr/bin/python3
def uppercase(str):
    x = ""
    for i in str:
        if i >= 'a' and i <= 'z':
            x += chr(ord(i) - 32)
        else:
            x += i
    print("{0}".format(x))
