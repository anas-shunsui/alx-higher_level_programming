#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) > 0:
        int_a1 = tuple_a[0]
    else:
        int_a1 = 0

    if len(tuple_a) > 1:
        int_a2 = tuple_a[1]
    else:
        int_a2 = 0

    if len(tuple_b) > 0:
        int_b1 = tuple_b[0]
    else:
        int_b1 = 0

    if len(tuple_b) > 1:
        int_b2 = tuple_b[1]
    else:
        int_b2 = 0

    return (int_a1 + int_b1, int_a2 + int_b2)