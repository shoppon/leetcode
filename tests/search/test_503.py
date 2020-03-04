from unittest import TestCase
from leetcode.search import lc_503


class Test503(TestCase):
    def test0(self):
        so = lc_503.Solution()
        ret = so.nextGreaterElements([1, 2, 1])
        self.assertEquals([2, -1, 2], ret)

    def test1(self):
        so = lc_503.Solution()
        ret = so.nextGreaterElements([3, 8, 4, 1, 2])
        self.assertEquals([8, -1, 8, 2, 3], ret)
