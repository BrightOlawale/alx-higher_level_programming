#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    vc = len(argv)
    if vc == 1:
        print("{} arguments.".format(0))
    else:
        print("{} arguments:".format((vc-1)))
        for i in range(1, vc):
            print("{}: {}".format((i), argv[i]))

