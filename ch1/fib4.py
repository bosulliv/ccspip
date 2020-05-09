# -*- coding: utf-8 -*-
"""
Memoize by decorating with built in function
"""
from functools import lru_cache

@lru_cache(maxsize=None)
def fib4(n: int) -> int:
    """ Decorate with built in function memoiser """
    if n < 2:
        return n
    return fib4(n-2) + fib4(n-1)

if __name__ == '__main__':
    # Only the memo or iterative make this fast enough to complete
    print(fib4(50))
