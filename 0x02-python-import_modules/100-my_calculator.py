#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == "__main__":
    if len(argv) < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        ops = ["+", "-", "*", "/"]
        func = [
         (add(int(argv[1]), int(argv[3]))),
         (sub(int(argv[1]), int(argv[3]))),
         (mul(int(argv[1]), int(argv[3]))),
         (div(int(argv[1]), int(argv[3])))]
        if argv[2] not in ops:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        for i in range(len(ops)):
            if argv[2] == ops[i]:
                print("{} + {} = {}".format(argv[1], argv[3], func[i]))
                exit(0)
