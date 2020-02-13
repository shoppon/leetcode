from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        left_max = []
        right_max = []

        max_v = float('-inf')
        for h in height:
            max_v = max(h, max_v)
            left_max.append(max_v)

        max_v = float('-inf')
        for i in range(length, 0, -1):
            max_v = max(height[i-1], max_v)
            right_max.insert(0, max_v)

        ans = 0
        for h, l, r in zip(height, left_max, right_max):
            ans += min(l, r) - h

        return ans
