#!/usr/bin/python3
"""save to json file"""


import json


def save_to_json_file(my_obj, filename):
    """save to json file"""
    with open(filename, 'w', encoding='UTF-8') as f:
        json_str = json.dumps(my_obj)
        return (f.write(json_str))
