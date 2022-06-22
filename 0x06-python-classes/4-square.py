#!/usr/bin/python3
class Square:
    '''Defining a Square'''
    def __init__(self, size=0):
        '''Initialization of instance attributes
            size(int): 0 or positive integer
        '''
        if (isinstance(size, int)) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        '''parsing value to calculate area
            Returns: the area of the square
        '''
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        '''Initialization of instance attributes
            size(int): 0 or positive integer
        '''
        if (isinstance(value, int)) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
