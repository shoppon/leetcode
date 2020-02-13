from unittest import TestCase
from leetcode.strings import lc_140


class Test140(TestCase):
    def test_normal(self):
        s = "catsanddog"
        wordDict = ["cat", "cats", "and", "sand", "dog"]
        so = lc_140.Solution()
        ret = so.wordBreak(s, wordDict)
        self.assertEquals([
            "cat sand dog",
            "cats and dog",
        ], ret)
