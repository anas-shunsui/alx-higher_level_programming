#!/usr/bin/python3
"""pascal triangle"""


def pascal_triangle(n):
    """pascal triangle"""
    list = []
    if n <= 0:
        return ([])
    list = [[1]]
    for i in range(n - 1):
        tmp = [0] + list[-1] + [0]
        row = []
        for j in range(len(list[-1]) + 1):
            row.append(tmp[j] + tmp[j + 1])
        list.append(row)
    return (list)
