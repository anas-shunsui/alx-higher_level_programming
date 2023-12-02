#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    #for i in range(len(my_list) - 1, -1, -1):
        #print("{:d}".format(my_list[i]))
    x = my_list[::-1]
    for i in x:
        print("{:d}".format(i))