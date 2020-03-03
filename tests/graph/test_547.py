from unittest import TestCase
from leetcode.graph import lc_547


class Test547(TestCase):
    def test0(self):
        so = lc_547.Solution()
        ret = so.findCircleNum([[1, 1, 0],
                                [1, 1, 1],
                                [0, 1, 1]])
        self.assertEquals(1, ret)

    def test1(self):
        so = lc_547.Solution()
        ret = so.findCircleNum([[1, 1, 0],
                                [1, 1, 0],
                                [0, 0, 1]])
        self.assertEquals(2, ret)

    def test2(self):
        so = lc_547.Solution()
        ret = so.findCircleNum(
            [[1, 0, 0, 1],
             [0, 1, 1, 0],
             [0, 1, 1, 1],
             [1, 0, 1, 1]])
        self.assertEquals(1, ret)

    def test3(self):
        so = lc_547.Solution()
        ret = so.findCircleNum(
            [[1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
             [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
             [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
             [1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
             [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
             [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
             [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
             [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
             [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
             [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
             [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1]])
        self.assertEquals(1, ret)
