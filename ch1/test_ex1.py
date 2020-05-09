# -*- coding: utf-8 -*-
import unittest
from ex1 import fib, fib_rec
import timeit

class TestEx1(unittest.TestCase):
    """ Test New Fib Solution """
    def test_zero(self):
        """ fib(0) == 0 """
        self.assertEqual(fib(0), 0)

    def test_one(self):
        """ fib(1) == 1 """
        self.assertEqual(fib(1), 1)

    def test_five(self):
        """ Fib(5) = 5 """
        self.assertEqual(fib(5), 5)

    def test_ten(self):
        """ Fib(10) = 55 """
        self.assertEqual(fib(10), 55)

    def test_rec_five(self):
        """ Fib(5) = 5 """
        self.assertEqual(fib_rec(5), 5)

    def test_quicker_than_recursive(self):
        """ Prove my solution is 'mult' times quicker than then
        obvious recursive solution, which has O(2^N)
        """
        mult = 250
        reps = 1000
        res_fib = timeit.timeit("fib_rec(20)",
                                setup="from ex1 import fib_rec",
                                number=reps//mult)
        res = timeit.timeit("fib(20)",
                            setup="from ex1 import fib",
                            number=reps)
        self.assertGreater(res_fib, res)
