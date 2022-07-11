#!/usr/bin/python3
"""script to add all arguments to a list"""

from fileinput import filename
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
try:
    my_list = load_from_json_file('add_item.json')
except FileNotFoundError:
    my_list = []

filename = sys.argv[1:]
my_list.extend(filename)
save_to_json_file(my_list, 'add_item.json')
