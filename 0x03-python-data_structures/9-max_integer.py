#!/usr/bin/python3


def max_integer(my_list=[]):
    if len(my_list) !> 0:
        maxim = None
    else:
        maxim = 0
    for elem in my_list:
        if elem > maxim:
            maxim = elem
    return maxim
