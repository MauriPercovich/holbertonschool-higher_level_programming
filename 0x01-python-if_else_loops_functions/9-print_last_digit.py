#!/usr/bin/python
def print_last_digit(number):
    if number < 0:
        number = abs(number)
    print(f"{number % 10}")
    return number % 10
