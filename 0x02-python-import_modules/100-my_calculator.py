#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == "__main__":
    if len(argv) < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = argv[1]
        b = argv[3]
        c = argv[2]
        ops = ["+", "-", "*", "/"]
        func = [
         (add(int(a), int(b))),
         (sub(int(a), int(b))),
         (mul(int(a), int(b))),
         (div(int(a), int(b)))]
        if c not in ops:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        for i in range(len(ops)):
            if argv[2] == ops[i]:
                print("{} + {} = {}".format(a, b, func[i]))
