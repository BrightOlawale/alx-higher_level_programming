#!/usr/bin/python3
"""
    JSON representation of an object (string)
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Saves an object to a json file
    """
    with open(filename, "w", encoding="utf-8") as f:
        return json.dump(my_obj, f)
