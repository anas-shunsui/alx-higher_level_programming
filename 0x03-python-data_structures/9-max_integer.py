#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return (None)
    if len(my_list) > 0:
        max = my_list[0]
        for index in range(len(my_list)):
            if my_list[index] > max:
                max = my_list[index]
        return (max)
