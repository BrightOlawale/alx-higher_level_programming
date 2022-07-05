#!/usr/bin/python3
"""
    Module to pass a list in a class
"""


class MyList(list):
    """
        A class MyList that inherits from list
    """
    def print_sorted(self):
        """
            Function that prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
