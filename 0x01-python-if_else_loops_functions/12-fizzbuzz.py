#!/usr/bin/python3
def fizzbuzz():
    a = "FizzBuzz"
    b = "Fizz"
    c = "Buzz"
    blank = " "
    for i in range(1, 101):
        if i % 15 == 0:
            print("{}".format(a), end='')
        if i % 3 == 0:
            print("{}".format(b), end='')
        if i % 5 == 0:
            print("{}".format(c), end='')
        else:
            print("{}".format(i), end='')
        if i != 101:
            print("{}".format(blank), end='')
