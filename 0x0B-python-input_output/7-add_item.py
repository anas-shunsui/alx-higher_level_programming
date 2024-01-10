#!/usr/bin/python3
"""add item"""
import sys
import os.path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv[1:]
f = "add_item.json"

if os.path.exists(f):
    list = load_from_json_file(f)
else:
    list = []

list += args

save_to_json_file(list, f)
