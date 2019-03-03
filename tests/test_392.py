from unittest import TestCase

from leetcode import lc_392


class MyTC(TestCase):
    def test_input1(self):
        s = lc_392.Solution()
        self.assertEquals(True, s.isSubsequence('abc', 'ahbgc'))
        self.assertEquals(False, s.isSubsequence('leeeeetcode', 'yyyyyletcodeyyyy'))
