from unittest import TestCase
from leetcode.dc import lc_315


class Test315(TestCase):
    def test0(self):
        so = lc_315.Solution()
        ret = so.countSmaller([5, 2, 6, 1])
        self.assertEquals([2, 1, 1, 0], ret)
