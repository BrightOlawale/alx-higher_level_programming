#!/usr/bin/python3

if __name__ = "__main__":
    def print_reversed_list_integer(my_list=[]):
        rev = my_list[::-1]
        for i in rev:
            print("{}".format(i))
