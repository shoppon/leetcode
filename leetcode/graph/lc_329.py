# coding: utf-8
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 0:
            return 0
        self.x_len = len(matrix[0])
        self.y_len = len(matrix)
        lookup = [[0] * self.x_len for _ in range(self.y_len)]
        for x in range(self.x_len):
            for y in range(self.y_len):
                self.dfs1(matrix, lookup, (x, y))
        return max(map(max, lookup))

    def dfs(self, matrix, lookup, start):
        """深度搜索非递归实现

        Arguments:
            matrix {list} -- [description]
            lookup {[type]} -- 深度矩阵
            start {[type]} -- 起点
        """
        stack = [start]
        cur = start
        lookup[start[1]][start[0]] = max(lookup[start[1]][start[0]], 1)
        while stack:
            cur = stack.pop()
            value = matrix[cur[1]][cur[0]]
            left = (cur[0]-1, cur[1])
            right = (cur[0]+1, cur[1])
            up = (cur[0], cur[1]-1)
            down = (cur[0], cur[1]+1)
            for p in (left, right, up, down):
                if 0 <= p[0] < self.x_len and 0 <= p[1] < self.y_len and matrix[p[1]][p[0]] < value:
                    # why
                    lookup[p[1]][p[0]] = max(
                        lookup[cur[1]][cur[0]]+1, lookup[p[1]][p[0]])
                    stack.append(p)

    def dfs1(self, matrix, lookup, start):
        if lookup[start[1]][start[0]]:
            return lookup[start[1]][start[0]]
        value = matrix[start[1]][start[0]]
        res = 1
        left = (start[0]-1, start[1])
        right = (start[0]+1, start[1])
        up = (start[0], start[1]-1)
        down = (start[0], start[1]+1)
        for p in (left, right, up, down):
            if 0 <= p[0] < self.x_len and 0 <= p[1] < self.y_len and matrix[p[1]][p[0]] < value:
                res = max(res, 1+self.dfs1(matrix, lookup, p))
        lookup[start[1]][start[0]] = max(res, lookup[start[1]][start[0]])
        return lookup[start[1]][start[0]]
