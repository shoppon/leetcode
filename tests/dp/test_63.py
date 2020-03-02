from unittest import TestCase

from leetcode.dp import lc_63


class Test63(TestCase):
    def test0(self):
        so = lc_63.Solution()
        ret = so.uniquePathsWithObstacles([
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ])
        self.assertEquals(2, ret)

    def test1(self):
        so = lc_63.Solution()
        ret = so.uniquePathsWithObstacles([
            [0, 1]
        ])
        self.assertEquals(0, ret)

    def test2(self):
        so = lc_63.Solution()
        ret = so.uniquePathsWithObstacles([
            [1, 0]
        ])
        self.assertEquals(0, ret)
