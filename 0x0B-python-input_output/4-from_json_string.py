#!/usr/bin/python3
"""from json string"""


import json


def from_json_string(my_str):
    """from json string"""
    json_str = json.loads(my_str)
    return (json_str)
