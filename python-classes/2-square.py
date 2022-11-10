#!/usr/bin/python3
'''Creating a class'''

class Square:
    '''Square class with an attribute'''
    def __init__(self, size=0):
        '''Instance attribute'''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
