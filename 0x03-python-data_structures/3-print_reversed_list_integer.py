#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    lc = len(my_list) - 1
    while lc <= 0:
        print("{}".format(my_list[lc]))
        lc -= 1
