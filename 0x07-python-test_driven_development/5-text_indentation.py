#!/usr/bin/python3
"""
    A Text indentation module
"""


def text_indentation(text):
    """
        A function that prints a text with 2 new
        lines after each of these characters: ., ? and :
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    if len(text) == 0:
        return
    else:
        idx = 0
        for i in range(len(text) - 1):
            if text[i] == '.' or text[i] == '?' or text[i] == ':':
                print(text[idx:i+1].strip(), end="\n\n")
                idx = i+1
        print(text[idx:i+2].strip(), end="")
