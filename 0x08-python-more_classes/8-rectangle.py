#!/usr/bin/python3
'''class "rectangle" '''


class Rectangle:
    '''rectangle'''


    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height
        self.print_symbol = Rectangle.print_symbol
    '''getter width'''
    @property
    def width(self):
        return self.__width
    ''' setter width '''
    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
    '''getter height'''
    @property
    def height(self):
        return self.__height
    ''' setter size '''
    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
    '''calculation'''
    def area(self):
        return self.__width * self.__height
    '''calculation'''
    def perimeter(self):
        if self.__height is 0 or self.__width is 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
    '''print the rectangle'''
    def __str__(self):
        if self.__height is 0 or self.__width is 0:
            return ""
        pic = (str(self.print_symbol) * self.__width + "\n") * self.__height
        return pic[:-1:]
    '''return the Rectangle'''
    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)
    '''delete a Rectangle'''
    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
    '''staticmethod to compare Rectangles'''
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
