#!/usr/bin/python3
'''main'''


def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        while i < x:
            print(f"{my_list[cont]}", end="")
            i += 1
    except IndexError:
        pass
    print("")
    return i
