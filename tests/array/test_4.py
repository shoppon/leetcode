from unittest import TestCase

from leetcode.array import lc_4


class Test4(TestCase):
    def test0(self):
        so = lc_4.Solution()
        self.assertEquals(2.5, so.findMedianSortedArrays([1, 3], [2, 3]))

    def test_odd(self):
        so = lc_4.Solution()
        self.assertEquals(2, so.findMedianSortedArrays([1], [2, 3]))

    def test_even(self):
        so = lc_4.Solution()
        self.assertEquals(2.5, so.findMedianSortedArrays([1, 5], [2, 3]))
