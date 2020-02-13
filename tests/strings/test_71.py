from unittest import TestCase

from leetcode import lc_71


class MyTC(TestCase):
    def test0(self):
        s = lc_71.Solution()
        self.assertEquals(3, s.simplifyPath(''))
