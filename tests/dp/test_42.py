from unittest import TestCase

from leetcode.dp import lc_42


class Test42(TestCase):
    def test0(self):
        so = lc_42.Solution()
        self.assertEquals(6, so.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

    def test1(self):
        so = lc_42.Solution()
        self.assertEquals(1, so.trap([4, 2, 3]))
