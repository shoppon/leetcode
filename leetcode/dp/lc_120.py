from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 上一行最小值
        # TODO(xp) 在原数组修改可以将空间复杂度降为O1
        minimus = [0, 0]
        for row in triangle:
            cur = []
            for i, col in enumerate(row):
                min_v = min(minimus[i], minimus[i+1])
                cur.append(min_v + col)
            cur.append(float('inf'))
            cur.insert(0, float('inf'))
            minimus = cur
        return min(minimus)
