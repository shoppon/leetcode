from unittest import TestCase
from leetcode.strings import lc_820


class Test820(TestCase):
    def test0(self):
        so = lc_820.Solution()
        ret = so.minimumLengthEncoding(["time", "me", "bell"])
        self.assertEquals(10, ret)
