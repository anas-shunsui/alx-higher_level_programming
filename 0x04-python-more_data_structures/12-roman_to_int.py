#!/usr/bin/python3
def roman_to_int(roman_string):
    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000}
    '''if roman_string is not str or None:
        return (0)
    if roman_string is not None:
        return (0)'''
    res = 0
    oldvalue = 0
    for char in reversed(roman_string):
        value = dict[char]
        if value < oldvalue:
            res -= value
        else:
            res += value
        oldvalue = value

    return (res)
