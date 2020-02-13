from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        ans = {}

        for n in nums:
            if n in ans:
                continue

            left = ans.get(n-1, 0)
            right = ans.get(n+1, 0)

            ans[n-left] = ans[n] = ans[n+right] = left+right+1

        return max(ans.values())

    def longestConsecutive1(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        ans = {}

        for n in nums:
            if n in ans:
                continue
            else:
                ans[n] = 1
            if n - 1 in ans:
                ans[n] = ans[n] + ans[n-1]
                ans[n-1] = ans[n]
            if n + 1 in ans:
                ans[n] = ans[n] + ans[n+1]
                ans[n+1] = ans[n]

        return max(ans.values())
