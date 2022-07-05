#!/usr/bin/python3
"""
    Module to compare class instances.
"""


def is_kind_of_class(obj, a_class):
    """
        Check if the object is of the same class or inherited class.
    """
    return isinstance(obj, a_class)
