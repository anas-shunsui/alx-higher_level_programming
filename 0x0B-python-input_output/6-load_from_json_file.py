#!/usr/bin/python3
"""load from json file"""


import json


def load_from_json_file(filename):
    """load from json file"""
    with open(filename, 'r', encoding='UTF-8') as f:
        json_str = json.load(f)
        return (json_str)
