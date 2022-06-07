#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    ttable = []
    for elem in my_list:
        if elem % 2 == 0:
            ttable.append(True)
        else:
            ttable.append(False)
    return ttable
