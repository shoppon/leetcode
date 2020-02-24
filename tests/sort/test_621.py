from unittest import TestCase

from leetcode.sort import lc_621


class Test621(TestCase):
    def test0(self):
        so = lc_621.Solution()
        ret = so.leastInterval(
            ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C', 'D', 'D', 'D'], 3)
        self.assertEquals(12, ret)

    def test1(self):
        so = lc_621.Solution()
        ret = so.leastInterval(
            ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C', 'C', 'D', 'D', 'D'], 4)
        self.assertEquals(14, ret)

    def test2(self):
        so = lc_621.Solution()
        ret = so.leastInterval(
            ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2)
        self.assertEquals(16, ret)
