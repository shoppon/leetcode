from unittest import TestCase

from leetcode.graph import lc_753


class Test753(TestCase):
    def test0(self):
        so = lc_753.Solution()
        ret = so.crackSafe(3, 3)
        self.assertEquals('', ret)

    def test1(self):
        so = lc_753.Solution()
        so.permutations(3, ['a', 'b', 'c'])
