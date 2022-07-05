#!/usr/bin/python3
"""
    Module to compare class instances.
"""


def inherits_from(obj, a_class):
    """"
        Check if the object is an inherited class.
    """
    return issubclass(obj.__class__, a_class) and type(obj) is not a_class
