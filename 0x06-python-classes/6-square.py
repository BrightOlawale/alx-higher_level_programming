#!/usr/bin/python3
'''Defining a square'''


class Square:
    '''A class Square that defines a square by: (based on 5-square.py)'''


class Square:
    '''Defining a Square'''
    def __init__(self, size=0, position=(0, 0)):
        '''Initialization of instance attributes
            size(int): 0 or positive integer
        '''
        self.__size = size
        self.__position = position

    def area(self):
        '''parsing value to calculate area
            Returns: the area of the square
        '''
        return self.__size * self.__size

    def my_print(self):
        '''
            that prints "#" the shape of square size
        '''
        if self.__size == 0:
            print()
        else:
            for col in range(self.__size):
                print("{}{}".format("_"*self.__position[0],"#"*self.__size), end="")
                print()

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
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            if not isinstance(value[0], int) or not isinstance(value[1], int):
                if value[0]>= 0 and value[1]>=0:
                    raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
