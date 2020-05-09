# -*- coding: utf-8 -*-
""" Write another function returns element n of fibonacci sequence
    - Use a technique of your own design
    - Write unit tests that evaluate its correctness
    - Write unit tests that compare its performance to tuple swap method
"""
from copy import copy

def fib(item: int) -> int:
    if item < 2:
        return item
    else:
        first: int = 0
        second: int = 1
        for pos in range(2, item+1):
            temp: int = copy(second)
            second = first + second
            first = temp
        return second

def fib_rec(item: int) -> int:
    if item < 2:
        return item
    else:
        return fib_rec(item - 2) + fib_rec(item - 1)
