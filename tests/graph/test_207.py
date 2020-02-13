from unittest import TestCase

from leetcode.graph import lc_207


class Test207(TestCase):
    def test0(self):
        so = lc_207.Solution()
        self.assertEquals(True, so.canFinish(2, [[0, 1]]))
