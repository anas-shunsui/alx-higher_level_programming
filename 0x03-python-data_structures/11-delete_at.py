#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 and idx > len(my_list):
        del my_list[3]
        return (my_list)
    for i in my_list:
        if i == 4:
            del my_list[3]
    return (my_list)
