from unittest import TestCase
from leetcode.dc import lc_878


class Test878(TestCase):
    def test0(self):
        so = lc_878.Solution()
        ret = so.nthMagicalNumber(3, 6, 4)
        self.assertEquals(8, ret)
