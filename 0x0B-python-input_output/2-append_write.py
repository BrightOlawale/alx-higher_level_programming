#!/usr/bin/python3
"""
    Write a function that appends a
    text file (UTF8) and prints it to stdout.
"""


def append_write(filename="", text=""):
    """
    Appends text to a file
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
