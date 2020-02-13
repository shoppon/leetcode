from unittest import TestCase

from leetcode.dp import lc_887


class Test887(TestCase):
    def test0(self):
        so = lc_887.Solution()
        self.assertEquals(4, so.superEggDrop(3, 14))

    def test1(self):
        so = lc_887.Solution()
        self.assertEquals(3, so.superEggDrop(2, 6))

    def test2(self):
        so = lc_887.Solution()
        self.assertEquals(2, so.superEggDrop(2, 3))

    def test3(self):
        so = lc_887.Solution()
        self.assertEquals(5, so.superEggDrop(3, 25))

    def test4(self):
        so = lc_887.Solution()
        self.assertEquals(3, so.superEggDrop(1, 3))

    def test5(self):
        so = lc_887.Solution()
        self.assertEquals(16, so.superEggDrop(4, 2000))

    def test6(self):
        so = lc_887.Solution()
        self.assertEquals(2, so.superEggDrop(3, 2))
