from unittest import TestCase
from leetcode.dp import lc_62


class Test62(TestCase):
    def test0(self):
        so = lc_62.Solution()
        ret = so.uniquePaths(3, 2)
        self.assertEquals(3, ret)
