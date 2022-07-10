#!/usr/bin/python3
"""
Write a function that reads a text file (UTF8) and prints it to stdout.
"""


def write_file(filename="", text=""):
    """
    Writes a text to a file
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
