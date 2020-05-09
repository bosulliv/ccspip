# -*- coding: utf-8 -*-

def fib2(n: int) -> int:
    # Classic recursive solution
    # Terrible time complexity = O(2^N)
    if n < 2:
        return n
    return fib2(n-2) + fib2(n-1)

if __name__ == '__main__':
    print(fib2(5))
    print(fib2(10))