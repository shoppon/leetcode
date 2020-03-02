from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid[0]), len(obstacleGrid)

        arr = [[0] * m for _ in range(n)]
        for i in range(m):
            if obstacleGrid[0][i] == 0:
                arr[0][i] = 1
            else:
                break
        for j in range(n):
            if obstacleGrid[j][0] == 0:
                arr[j][0] = 1
            else:
                break
        for i in range(m-1):
            for j in range(n-1):
                if obstacleGrid[j+1][i+1] == 0:
                    arr[j+1][i+1] = arr[j][i+1] + arr[j+1][i]
                else:
                    arr[j+1][i+1] = 0

        return arr[n-1][m-1]
