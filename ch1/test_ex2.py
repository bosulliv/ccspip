# -*- coding: utf-8 -*-
""" Unit test Exercise 2 """
from unittest import TestCase
from ex2 import BitSeq

class TestBitSeq(TestCase):
    def test_smoke(self):
        self.assertEqual(0, 0)

    def test_two_nibbles(self):
        """ Nibble aligned """
        val: int = 0xf
        size: int = 4
        seq: BitSeq = BitSeq(size=size, val=val)
        self.assertEqual(seq[0], 15)

    def test_iterate_nibbles(self):
        """ Nibble aligned """
        val: int = 0xf0f0
        size: int = 4
        seq: BitSeq = BitSeq(size=size, val=val)
        ans = [0, 15, 0, 15]
        res = [bits for bits in seq]
        self.assertListEqual(ans, res)

    def test_fraction_nibble(self):
        """ fraction of single nibble """
        val: int = 0x1
        size: int = 4
        seq: BitSeq = BitSeq(size=size, val=val)
        ans = [1]
        res = [bits for bits in seq]
        self.assertListEqual(ans, res)

    def test_fraction_many_nibbles(self):
        """ fraction of mmny nibbles """
        val: int = 0x1fa12
        size: int = 4
        seq: BitSeq = BitSeq(size=size, val=val)
        ans = [2, 1, 10, 15, 1]
        res = [bits for bits in seq]
        self.assertListEqual(ans, res)
