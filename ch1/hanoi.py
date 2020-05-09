# -*- coding: utf-8 -*-
from typing import TypeVar, Generic, List
T = TypeVar('T')

class Stack(Generic[T]):

    def __init__(self) -> None:
        self._container: List[T] = []

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()

    def __repr__(self) -> str:
        return repr(self._container)

def hanoi(begin: Stack[int],
          end: Stack[int],
          temp: Stack[int],
          n: int) -> None:
    """
    Parameters
    ----------
    begin : Stack[int]
        Starting stack
    end : Stack[int]
        End stack
    temp : Stack[int]
        Middle stack
    n : int
        Number of wrings

    Returns
    -------
    None
        The passed stacks are changed in place

    Algorithm
    ---------
    There is a recursive algorithm to solve the tower of hanoi.
    You repeat this algorithm until there is only one disk left
    on the start tower, which you can move straight to the end
    tower:
        * Move the upper n-1 discs from tower begin to tower temp,
          using end as the in-between.
        * Move the single disk left on tower begin, to tower end.
        * Move the n-1 disks from tower temp to tower end using
          begin as the in-between.
    """
    if n == 1:
        end.push(begin.pop())
    else:
        # Move the n-1 disks from begin to temp using end to jump
        hanoi(begin, temp, end, n-1)
        # Move the top disk from begin to end
        hanoi(begin, end, temp, 1)
        # Move the n-1 discs left on temp to end using begin to jump
        hanoi(temp, end, begin, n-1)

if __name__ == "__main__":
    num_discs: int = 3
    tower_a: Stack[int] = Stack()
    tower_b: Stack[int] = Stack()
    tower_c: Stack[int] = Stack()
    for i in range(1, num_discs+1):
        tower_a.push(i)

    hanoi(tower_a, tower_c, tower_b, num_discs)
    print(tower_a)
    print(tower_b)
    print(tower_c)