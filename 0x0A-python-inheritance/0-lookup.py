#!/usr/bin/python3
"""
    Module to lookup the object in the current namespace.
"""


def lookup(obj):
    """
        Lookup the object in the current namespace.
    """
    return dir(obj)
