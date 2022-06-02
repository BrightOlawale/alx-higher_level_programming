#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    vc = len(argv)
    if vc <= 2:
        if vc == 1:
            print("{} argument.".format(0))
        else:
            print("{} argument:".format((vc-1)))
            print("{}: {}".format((vc-1), argv[vc-1]))
    else:
        print("{} arguments:".format((vc-1)))
        for i in range(1, vc):
            print("{}: {}".format((i), argv[i]))
