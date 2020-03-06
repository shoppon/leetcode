from unittest import TestCase
from leetcode.strings import lc_567


class Test567(TestCase):
    def test0(self):
        so = lc_567.Solution()
        ret = so.checkInclusion("ab", "eidbaooo")
        self.assertEquals(True, ret)

    def test1(self):
        so = lc_567.Solution()
        ret = so.checkInclusion("ab", "eidbdaooo")
        self.assertEquals(False, ret)

    def test2(self):
        so = lc_567.Solution()
        ret = so.checkInclusion("abcde", "dcbae")
        self.assertEquals(True, ret)

    def test3(self):
        so = lc_567.Solution()
        ret = so.checkInclusion("adc", "dcda")
        self.assertEquals(True, ret)

    def test4(self):
        so = lc_567.Solution()
        ret = so.checkInclusion("trinitrophenylmethylnitramine",
                                "dinitrophenylhydrazinetrinitrophenylmethylnitramine")
        self.assertEquals(True, ret)

    def test5(self):
        so = lc_567.Solution()
        ret = so.checkInclusion("abc",
                                "ccccbbbbaaaa")
        self.assertEquals(False, ret)
