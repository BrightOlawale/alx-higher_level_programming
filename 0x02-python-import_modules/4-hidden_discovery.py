#!/usr/bin/python3
import hidden_4 as hd

if __name__ == "__main__":
    for j in dir(hd):
        if "__" not in j:
            print(j)

