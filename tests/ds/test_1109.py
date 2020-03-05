from unittest import TestCase
from leetcode.ds import lc_1109


class Test1109(TestCase):
    def test0(self):
        so = lc_1109.Solution()
        ret = so.corpFlightBookings([[1, 2, 10], [2, 3, 20], [2, 5, 25]], 5)
        self.assertEquals([10, 55, 45, 25, 25], ret)
