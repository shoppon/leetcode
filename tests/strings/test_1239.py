from unittest import TestCase
from leetcode.strings import lc_1239


class Test1239(TestCase):
    def test0(self):
        so = lc_1239.Solution()
        ret = so.maxLength(["cha", "r", "act", "ers"])
        self.assertEquals(ret, 6)

    def test1(self):
        so = lc_1239.Solution()
        ret = so.maxLength(["abcg", "adx", "bey", "cf"])
        self.assertEquals(ret, 8)

    def test2(self):
        so = lc_1239.Solution()
        ret = so.maxLength(["abcdefghijklmnopqrstuvwxyz"])
        self.assertEquals(ret, 26)
