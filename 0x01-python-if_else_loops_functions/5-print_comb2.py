#!/usr/bin/python3
for i in range(100):
    if i == 99:
        print("{}\n".format(i))
        break
    if i <= 9:
        print("0", end="")
    print("{}".format(i), end=", ")
