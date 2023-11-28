#!/usr/bin/env python3
def uppercase(str):
    upr = ""
    for i in str:
        if ord(i) <= 122 and ord(i) >= 97:
            upr = chr(ord(i) - 32)
        else:
            upr = i
        print("{}".format(upr), end="")
    print("")
