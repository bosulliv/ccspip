# -*- coding: utf-8 -*-

def fib(n: int) -> int:
    # Error - no special case, or stop conditions. Will hit recursion limit
    return fib2(n-2) + fib2(n-1)

if __name__ == '__main__':
    print(fib1(5))
    print(fib1(10))