#!/usr/bin/python3
"""
    This is a module to add two integers supplied only as
    an integer or as a float.
"""


def add_integer(a, b=98):
    """
        A function  to add two numbers.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    else:
        a, b = int(a), int(b)
        return a + b
