from unittest import TestCase

from leetcode.graph import lc_212


class Test212(TestCase):
    def test0(self):
        so = lc_212.Solution()
        ret = so.findWords([
            ['o', 'a', 'a', 'n'],
            ['e', 't', 'a', 'e'],
            ['i', 'h', 'k', 'r'],
            ['i', 'f', 'l', 'v']
        ], ["oath", "pea", "eat", "rain"])
        self.assertEquals([], ret)
