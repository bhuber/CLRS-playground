#!/usr/bin/python

from f_2_3_mergesort import insertionsort, mergesort
from unittest import TestCase
import random


class TestInsertionSort(TestCase):
    def test_sorted(self):
        self.assertListEqual(range(1, 10), insertionsort(range(1, 10)))

    def test_reversed(self):
        self.assertListEqual(range(1, 10), insertionsort(range(9, 0, -1)))

    def test_random(self):
        l = range(1, 10)
        random.shuffle(l)
        self.assertListEqual(range(1, 10), insertionsort(l))

    def test_empty(self):
        self.assertListEqual([], insertionsort([]))

    def test_singular(self):
        self.assertListEqual([0], insertionsort([0]))

    def test_start(self):
        self.assertListEqual(range(1, 10), insertionsort(range(1, 10), 4))
        l = range(9, 0, -1)
        expected = [9, 8, 7, 1, 2, 3, 4, 5, 6]
        self.assertListEqual(expected, insertionsort(l, 3))

    def test_end(self):
        l = range(9, 0, -1)
        expected = [9, 8, 7, 3, 4, 5, 6, 2, 1]
        self.assertListEqual(expected, insertionsort(l, 3, 7))


class TestMergeSort(TestCase):
    def test_sorted(self):
        self.assertListEqual(range(1, 100), mergesort(range(1, 100)))

    def test_reversed(self):
        self.assertListEqual(range(1, 100), mergesort(range(99, 0, -1)))

    def test_random(self):
        l = range(1, 100)
        random.shuffle(l)
        self.assertListEqual(range(1, 100), mergesort(l))

    def test_empty(self):
        self.assertListEqual([], mergesort([]))

    def test_singular(self):
        self.assertListEqual([0], mergesort([0]))
