#!/usr/bin/python3
'''class rectangle'''


class Rectangle:
    '''class'''
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        '''getter width'''
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0
        raise ValueError("width must be >= 0")
    self.__width = width
    '''getter heigth'''
    @property
    def height(self):
        return self.__heigth
    @width.setter
    def heigth(self, heigth):
        if type(heigth) is not int:
            raise TypeError("heigth must be an integer")
        elif heigth < 0
        raise ValueError("heigth must be >= 0")
    self.__heigth = heigth
