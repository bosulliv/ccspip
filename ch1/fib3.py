# -*- coding: utf-8 -*-
"""
Use a dictionary to remember past results
"""

from typing import Dict
memo: Dict[int, int] = {0: 0, 1: 1}


def fib3(n: int) -> int:
    """ Memoisation removes repeated recursion calls for known results """
    if n not in memo:
        memo[n] = fib3(n-2) + fib3(n-1)
    return memo[n]

if __name__ == '__main__':
    print(fib3(5))
    print(fib3(10))
