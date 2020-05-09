# -*- coding: utf-8 -*-

""" Exercise 2
Write a wrapper around int that can be used generically as a sequence of bits.
Reimplement CompressedGene using the wrapper

So in this case int will already understand the number of bits in each chunk,
and we can build __get_item__ to provide these chunks in order.
"""

