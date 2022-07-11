#!/usr/bin/python3
"""
    script to add all arguments to a list
"""


import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = sys.argv[1:]
try:
    new_file = load_from_json_file("add_item.json")
    new_file.append(filename)
    save_to_json_file(new_file, "add_item.json")

except FileNotFoundError:
    save_to_json_file(filename, "add_item.json")
