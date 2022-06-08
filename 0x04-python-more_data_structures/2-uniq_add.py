#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = 0
    garbage = []
    while my_list:
        p = my_list.pop(0)
        if p in my_list:
            garbage.append(p)
        else:
            add += p
    return add
