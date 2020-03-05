from unittest import TestCase
from leetcode.search import lc_253


class Test253(TestCase):
    def test0(self):
        so = lc_253.Solution()
        ret = so.minMeetingRooms([[0, 30], [5, 10], [15, 20]])
        self.assertEquals(2, ret)

    def test1(self):
        so = lc_253.Solution()
        ret = so.minMeetingRooms([[7, 10], [2, 4]])
        self.assertEquals(1, ret)

    def test2(self):
        so = lc_253.Solution()
        ret = so.minMeetingRooms([[15, 16], [10, 15], [16, 25]])
        self.assertEquals(1, ret)
