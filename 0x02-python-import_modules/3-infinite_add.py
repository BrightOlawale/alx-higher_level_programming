#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    count = 0
    vc = len(argv)
    for k in range(1, vc):
        if vc == 1:
            break
        else:
            count += int(argv[k])

    print("{}".format(count))
