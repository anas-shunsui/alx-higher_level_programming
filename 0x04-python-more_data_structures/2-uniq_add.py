#!/usr/bin/python3
def uniq_add(my_list=[]):
    counter = 0
    uniq = set(my_list)
    for i in uniq:
        counter += i
    return (counter)
