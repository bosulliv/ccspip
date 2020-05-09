#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Iterate via a generator
"""
from typing import Generator

def fib6(n: int) -> Generator[int, None, None]:
    """
    Time complexity = O(N-1)
    Space complexity = O(2)
     we just accumulate the two previous numbers
     nifty
     """
    yield 0
    if n > 0:
        yield 1
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
        yield next

if __name__ == '__main__':
    for i in fib6(50):
        print(i)
