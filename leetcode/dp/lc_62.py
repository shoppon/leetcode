#coding: utf-8
class Solution:
    def uniquePaths1(self, m: int, n: int) -> int:
        # 自顶向下
        if m == 1 or n == 1:
            return 1
        else:
            return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)

    def uniquePaths(self, m: int, n: int) -> int:
        # 自底向上
        arr = [[1] * m for _ in range(n)]
        for i in range(m-1):
            for j in range(n-1):
                arr[j+1][i+1] = arr[j][i+1] + arr[j+1][i]

        return arr[n-1][m-1]
