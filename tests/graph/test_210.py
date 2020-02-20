from unittest import TestCase

from leetcode.graph import lc_210


class Test210(TestCase):
    def test0(self):
        so = lc_210.Solution()
        order = so.findOrder(2, [[1, 0]])
        self.assertEquals([0, 1], order)

    def test1(self):
        so = lc_210.Solution()
        order = so.findOrder(2, [])
        self.assertEquals([0, 1], order)