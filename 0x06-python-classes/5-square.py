#!/usr/bin/python3
"""Define a class named Square to represent a square."""


class Square:
    """initialize a Square object"""
    def __init__(self, size=0):
        """Initialize a new Square"""
        self.__size = size

    def area(self):
        area = self.__size ** 2
        return (area)

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        self.__size = value
        if not type(value) is int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                for j in range(self.size):
                    print("{}".format("#"), end="")
                print()
