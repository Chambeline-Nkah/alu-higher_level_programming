#!/usr/bin/python3
'''Class square which inherits from Rectangle'''


Rectangle = __import__('9-rectangle.py').Rectangle

class Square(Rectangle):
    '''Creating a class square that inherits from Rectangle'''
    def __init__(self, size):
        '''Defining the init function'''
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        '''Defining the area function'''
        return self.__size ** 2
