#!/usr/bin/python3
def remove_char_at(str, n):
    string = ""
    j = 0
    for k in str:
        if (j != n):
            string = string + k
        j = j + 1
    return(string)
