from unittest import TestCase
from leetcode.ds import lc_957


class Test957(TestCase):
    def test0(self):
        so = lc_957.Solution()
        ret = so.prisonAfterNDays([0, 1, 0, 1, 1, 0, 0, 1], 7)
        self.assertEquals([0, 0, 1, 1, 0, 0, 0, 0], ret)

    def test1(self):
        so = lc_957.Solution()
        ret = so.prisonAfterNDays([1, 0, 0, 1, 0, 0, 1, 0], 1000000000)
        self.assertEquals([0, 0, 1, 1, 1, 1, 1, 0], ret)
