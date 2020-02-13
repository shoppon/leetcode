class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        index = 0
        for alpha in s:
            for idx, c in enumerate(t[index:]):
                if alpha == c:
                    index += idx + 1
                    break
            else:
                return False
        return True
