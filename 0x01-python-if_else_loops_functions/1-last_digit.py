#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > -1 and number < 10:
    print(f"Last digit of {number} is {number}", end=' ')
    digit = number
elif number > 10:
    digit = number % 10
    print(f"Last digit of {number} is {digit}", end=' ')
elif number > -10 and number < 0:
    digit = abs(number)
    print(f"Last digit of {number} is {digit}", end=' ')
elif number < -9:
    digit = abs(number) % 10
    digit = digit * -1
    print(f"Last digit of {number} is {digit}", end=' ')
if digit > 5:
    print("and is greater than 5")
elif digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
