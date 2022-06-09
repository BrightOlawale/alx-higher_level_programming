#!/usr/bin/pthon3
def best_score(a_dictionary):
    count = 0
    maxim = []
    if a_dictionary:
        for key, val in a_dictionary.items():
            if val > count:
                count = val
                maxim.append(key)
    else:
        maxim.append(None)
    return(maxim[-1])
