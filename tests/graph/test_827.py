from unittest import TestCase
from leetcode.graph import lc_827


class Test827(TestCase):
    def test0(self):
        so = lc_827.Solution()
        ret = so.largestIsland([[1, 0], [0, 1]])
        self.assertEquals(3, ret)

    def test1(self):
        so = lc_827.Solution()
        ret = so.largestIsland([[1, 1], [0, 1]])
        self.assertEquals(4, ret)

    def test2(self):
        so = lc_827.Solution()
        ret = so.largestIsland([[1, 1], [1, 1]])
        self.assertEquals(4, ret)