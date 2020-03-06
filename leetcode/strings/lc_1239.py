from typing import List


class Solution:
    def maxLength1(self, arr: List[str]) -> int:
        n = len(arr)
        ans = float('-inf')
        for i in range(2**n):
            cur = ""
            for j in range(n):
                if i & 2**j:
                    cur += arr[j]
                if len(cur) > 26:
                    break
            if len(cur) == len(set(cur)):
                ans = max(ans, len(cur))

        return ans

    def maxLength(self, arr: List[str]) -> int:
        def dfs(i, cur):
            if i >= len(arr):
                return len(cur)
            # 未重复，可以添加
            if len(cur + arr[i]) == len(set(cur+arr[i])):
                return max(dfs(i+1, cur), dfs(i+1, cur+arr[i]))
            else:
                return dfs(i+1, cur)

        return dfs(0, '')
