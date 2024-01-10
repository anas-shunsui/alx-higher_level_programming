#!/usr/bin/python3
"""read file"""


def read_file(filename=""):
    """read file"""
    with open(filename, 'r', encoding='UTF-8') as f:
    content = f.read()
    print(content, end="")
