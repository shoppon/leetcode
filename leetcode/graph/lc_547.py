from typing import List


class Solution:
    def findCircleNum1(self, M: List[List[int]]) -> int:
        n = len(M)
        ans = [-1] * n
        for r, row in enumerate(M):
            r_v = r if ans[r] == -1 else ans[r]
            for c, col in enumerate(row):
                # r和c是朋友
                if col == 1:
                    if ans[c] == -1:
                        # 将c的父节点置为r或者r的父节点
                        ans[c] = r_v
                    else:
                        # 必须先保存下来，否则当c改变时后面的不会再改
                        pre = ans[c]
                        for i in range(n):
                            if ans[i] == pre:
                                ans[i] = r_v
        return len(set(ans))

    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        visited = [0] * n

        def dfs(arr, visited, i):
            for j in range(n):
                if arr[i][j] == 1 and visited[j] == 0:
                    visited[j] = 1
                    dfs(arr, visited, j)

        count = 0
        for i in range(n):
            if visited[i] == 0:
                dfs(M, visited, i)
                count += 1
        return count
