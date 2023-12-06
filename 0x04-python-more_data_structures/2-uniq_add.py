#!/usr/bin/python3
def uniq_add(my_list=[]):
    count = 0
    uniq = set(my_list)
    for i in uniq:
        count += i
    return (count)
