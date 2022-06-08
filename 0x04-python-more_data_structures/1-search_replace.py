#!/usr/bin/pyhton3
def search_replace(my_list, search, replace):
    newlist = my_list[:]
    for idx, i in enumerate(newlist):
        if i == search:
            newlist[idx] = replace
    return newlist
