from unittest import TestCase

from leetcode.search import lc_46


class Test46(TestCase):
    def test0(self):
        so = lc_46.Solution()
        ret = so.permute([1, 2, 3])
        self.assertEquals([
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 1, 2],
            [3, 2, 1]
        ], ret)

    def test1(self):
        so = lc_46.Solution()
        ret = so.permute([1, 2, 3, 4])
        self.assertEquals([
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 1, 2],
            [3, 2, 1]
        ], ret)

    def test2(self):
        so = lc_46.Solution()
        ret = so.permute([1])
        self.assertEquals([[1]], ret)
