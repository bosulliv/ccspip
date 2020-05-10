# -*- coding: utf-8 -*-
"""
Exercise 2
----------
You saw how the simple int type can be used to represent a bit string.
* Write an ergonomic wrapper around int that can be used generically as a
  sequence of bits.
* Make it iterable
* ..and implement __getitem__.
* Reimplement CompressedGene using the wrapper

Ideas
-----
Subclassing int is hard - it's an immutable type, so you can't __init__ and
super.__init__. You have to understand and use __new__.

I need to make some movement - even if a method is not right. So I am going to


To help frame this, I'm working backwards. With a bit sequence int type, we
can just append nucleotide bits to the int, treating it like a list.

    def _compress(self, gene: str) -> None:
        # start with 1, the sentinel
        self.bit_string: int = 1
        for nucleotide in gene.upper():
            if nucleotide == "A":
                self.bit_string.append(0b00)
"""
import math

class BitSeq():
    """ Implement int as a sequence of bits """
    def __init__(self, size, val) -> None:
        """ We need to have the value, and the size of the bits in the
        sequence """
        self.size: int = size
        self.val: int = val
        self.bitlen: int = int.bit_length(val)
        self.entries: int = math.ceil(self.bitlen / self.size)
        self.pos: int = 0

    def __getitem__(self, i) -> int:
        """ Allow indexing """
        mask = 2**(self.size) - 1
        item = self.val >> (i*self.size)
        item &= mask
        return item

    def __iter__(self):
        """ build an iterator """
        return self

    def __next__(self) -> int:
        if self.pos < self.entries:
            self.pos += 1
            val = self.__getitem__(self.pos - 1)
            return val
        raise StopIteration

    def __repr__(self) -> str:
        """ print """
        return str(self.val)

if __name__ == '__main__':
    seq: BitSeq = BitSeq(size=4, val=0x12345)

    for pos, val in enumerate(seq):
        print(pos, val)
