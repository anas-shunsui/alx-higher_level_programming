#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    item = sorted(list(a_dictionary.items()))
    for i in range(len(item)):
        key, val = item[i]
        print("{}: {}".format(key, val))
