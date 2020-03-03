from unittest import TestCase

from leetcode.dp import lc_120


class Test120(TestCase):
    def test0(self):
        so = lc_120.Solution()
        ret = so.minimumTotal([
            [2],
            [3, 4],
            [6, 5, 7],
            [4, 1, 8, 3]
        ])
        self.assertEquals(11, ret)
