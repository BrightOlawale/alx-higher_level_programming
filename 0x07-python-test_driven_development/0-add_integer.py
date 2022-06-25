#!/usr/bin/python3
"""
    This is a module to add two integers supplied only as
    an integer or as a float.
"""


def add_integer(a, b=98):
    """
        A function  to add two numbers.
    """
    if not isinstance(a, (int,float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int,float)):
        raise TypeError("b must be an integer")
    else:
        a, b = int(a), int(b)
        return a + b
        

print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)
print(type(add_integer(2.0, 1.0)))
# print(add_integer("h", 1))
print(add_integer(-1, -3))
