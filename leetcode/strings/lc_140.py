from typing import List


class Solution:
    def wordBreak1(self, s: str, wordDict: List[str]) -> List[str]:
        pass

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        wordDict = set(wordDict)
        # mem = dict()
        # return self._wordBreak(s, wordDict, mem)
        result = []
        self._wordBreak0(s, "", wordDict, result)
        return result

    def _wordBreak0(self, s, st, wordDict, result):
        if not s:
            result.append(st.rstrip())

        for i in range(len(s)+1):
            if s[:i] in wordDict:
                self._wordBreak0(s[i:], st+str(s[:i]) + " ", wordDict, result)

    def _wordBreak(self, s, wordDict, mem):
        if s in mem:
            return mem[s]

        res = list()
        if not s:
            res.append("")
            return res

        for i in range(len(s)+1):
            if s[:i] in wordDict:
                sublist = self._wordBreak(s[i:], wordDict, mem)
                for it in sublist:
                    res.append(str(s[:i]) + ('' if not it else ' ') + it)

        mem[s] = res
        return res
