#!/usr/bin/python3
'''A class Square that defines a square by: (based on 1-square.py)'''


class Square:
    '''Initialization of instance attributes
        size(int): 0 or positive integer
    '''
    def __init__(self, size=0):
        if (isinstance(size, int)) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
