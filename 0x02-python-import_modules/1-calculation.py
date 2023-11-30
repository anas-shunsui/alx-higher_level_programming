#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import div, add, mul, sub
    a = 10
    b = 5
    result_1 = a + b
    result_2 = a - b
    result_3 = a * b
    result_4 = int(a / b)

print("{} + {} = {}".format(a, b, result_1))
print("{} - {} = {}".format(a, b, result_2))
print("{} * {} = {}".format(a, b, result_3))
print("{} / {} = {}".format(a, b, result_4))
