# -*- coding: utf-8 -*-
"""
Clever iterative solution
Like a two box kernel moving forward one number at a time
"""
def fib5(n: int) -> int:
    """
    Time complexity = O(N-1)
    Space complexity = O(2)
      we just accumulate the two previous numbers
      nifty
    """
    if n == 0:
        return n
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
    return next

if __name__ == '__main__':    
    # Only the memo or iterative make this fast enough to complete
    print(fib5(50))
