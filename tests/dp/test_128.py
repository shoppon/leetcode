from unittest import TestCase

from leetcode.dp import lc_128


class Test128(TestCase):
    def test0(self):
        so = lc_128.Solution()
        self.assertEquals(4, so.longestConsecutive([100, 4, 200, 1, 3, 2]))

    def test1(self):
        so = lc_128.Solution()
        self.assertEquals(3, so.longestConsecutive([100, 4, 200, 0, 3, 2]))

    def test2(self):
        so = lc_128.Solution()
        self.assertEquals(3, so.longestConsecutive([1, 2, 0, 1]))

    def test3(self):
        so = lc_128.Solution()
        self.assertEquals(9, so.longestConsecutive(
            [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
