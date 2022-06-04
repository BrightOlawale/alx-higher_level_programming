#!/usr/bin/python3


def element_at(my_list, idx):
    lc = len(my_list)
    if idx < 0:
        return None
    elif idx > (lc-1):
        return None
    else:
        print("{}".format(my_list[idx]))
