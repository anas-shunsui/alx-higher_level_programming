#!/usr/bin/python3
"""to json string"""


import json


def to_json_string(my_obj):
    """to json string"""
    json_str = json.dumps(my_obj)
    return (json_str)
