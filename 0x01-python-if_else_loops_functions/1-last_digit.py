#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
dig = number % 10
if dig > 5:
    print(f"Last digit of {number} is {dig} and is greater than 5\n")
elif dig == 0:
    print(f"Last digit of {number} is {dig} and is 0\n")
else:
    print(f"Last digit of {number} is {-dig} and is less than 6 and not 0\n")
