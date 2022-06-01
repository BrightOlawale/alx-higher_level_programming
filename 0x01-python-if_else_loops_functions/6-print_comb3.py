#!/usr/bin/python3
for i in range(10):
    for k in range(i, 10):
        if i == k:
            continue
        if i < 8:
            print("{}{}".format(i, k), end=", ")
        else:
            print("{}{}\n".format(i, k))
