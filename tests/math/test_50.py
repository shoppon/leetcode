from unittest import TestCase
from leetcode import lc_50

class Test50(TestCase):
    def test0(self):
        so = lc_50.Solution()
        self.assertEquals(8, so.myPow(2,3))

    def test_neg(self):
        so = lc_50.Solution()
        self.assertEquals(8, so.myPow(2,-3))

    def test1(self):
        so = lc_50.Solution()
        self.assertEquals(9.261, so.myPow(2.1,3))