#!/usr/bin/python3


def multiple_returns(sentence):
    length = 0
    for i in sentence:
        length += 1
    if length > 0:
        first = sentence[0]
    else:
        first = None
    return (length, first)
