from unittest import TestCase

from leetcode.math import lc_41


class Test41(TestCase):
    def test_input1(self):
        s = lc_41.Solution()
        self.assertEquals(3, s.firstMissingPositive([1, 2, 0]))
        self.assertEquals(1, s.firstMissingPositive([3, 4, -1, -1]))
