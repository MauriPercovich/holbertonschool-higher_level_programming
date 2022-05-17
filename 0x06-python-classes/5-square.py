#!/usr/bin/python3
'''square class'''


class Square:
    '''init Square, and raising Errors'''


    def __init__(self, size=0):
        self.size = size
    '''getter size'''
    @property
    def size(self):
        return self.__size
    ''' setter size '''
    @size.setter
    def size(self, value):
        '''setting size value'''

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    '''calculate the area of the square'''
    def area(self):
        return self.__size ** 2
    def my_print(self):
        '''prints'''


        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
