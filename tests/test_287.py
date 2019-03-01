from unittest import TestCase

from leetcode import lc_827


class MyTC(TestCase):
    def test_input1(self):
        s = lc_827.Solution()
        self.assertEquals(2, s.largestIsland([1, 3, 4, 2, 2]))
        self.assertEquals(3, s.largestIsland([3, 1, 3, 4, 2]))
