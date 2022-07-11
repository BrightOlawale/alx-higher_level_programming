#!/usr/bin/python3
"""

"""


import json


def load_from_json_file(filename):
    """
    Returns an object represented by a JSON string
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
