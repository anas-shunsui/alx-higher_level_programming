#!/usr/bin/python3
"""Student"""


class Student:
    """Student"""
    def __init__(self, first_name, last_name, age):
        """init"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """json"""
        result = {}
        i = 0
        if attrs is None:
            return (vars(self))
        else:
            for i in attrs:
                if hasattr(self, i):
                    result[i] = getattr(self, i)
            return (result)

    def reload_from_json(self, json):
        """reload"""
        for i, value in json.items():
            if hasattr(self, i):
                setattr(self, i, value)
