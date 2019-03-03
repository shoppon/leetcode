class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        arr = t
        for alpha in s:
            for idx, c in enumerate(arr):
                if alpha == c:
                    arr = arr[idx + 1:]
                    break
            else:
                return False
        return True
