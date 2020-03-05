from unittest import TestCase
from leetcode.maths import lc_1224


class Test1224(TestCase):
    def test0(self):
        so = lc_1224.Solution()
        ret = so.maxEqualFreq([2, 2, 1, 1, 5, 3, 3, 5])
        self.assertEquals(7, ret)

    def test1(self):
        so = lc_1224.Solution()
        ret = so.maxEqualFreq([1, 1, 1, 2, 2, 2])
        self.assertEquals(5, ret)

    def test2(self):
        so = lc_1224.Solution()
        ret = so.maxEqualFreq([10, 2, 8, 9, 3, 8, 1, 5, 2, 3, 7, 6])
        self.assertEquals(8, ret)

    def test3(self):
        so = lc_1224.Solution()
        ret = so.maxEqualFreq([1, 1])
        self.assertEquals(2, ret)
