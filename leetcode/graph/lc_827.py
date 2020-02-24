from typing import List


class Solution(object):
    def largestIsland(self, grid):
        def dfs(grid, x, y):
            for d in directs:
                tmp_x, tmp_y = x+d[0], y+d[1]
                if tmp_x < 0 or tmp_x >= x_len or tmp_y < 0 or tmp_y >= y_len:
                    continue
                # 不连通
                if grid[tmp_y][tmp_x] == 0:
                    continue
                # 遍历过不再遍历
                if area[tmp_y][tmp_x] > 0:
                    continue
                area_size[area_num] += 1
                area[tmp_y][tmp_x] = area_num
                dfs(grid, tmp_x, tmp_y)

        if len(grid) == 0:
            return 0
        directs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        x_len = len(grid[0])
        y_len = len(grid)
        # 记录每个点所在区域
        # -1表示未遍历过
        # 0表示不在岛屿上
        area = [[-1] * x_len for _ in range(y_len)]
        area_num = 1
        area_size = {}
        for y, row in enumerate(grid):
            for x, col in enumerate(row):
                if area[y][x] >= 0:
                    continue
                if col == 0:
                    area[y][x] = 0
                else:
                    area_size[area_num] = 1
                    area[y][x] = area_num
                    dfs(grid, x, y)
                    area_num += 1

        # 将每一个0变成1,将上下左右4个区域连接起来
        max_size = float('-inf')
        for y, row in enumerate(grid):
            for x, col in enumerate(row):
                if col == 0:
                    added = []
                    cur_size = 1
                    for d in directs:
                        tmp_x, tmp_y = x+d[0], y+d[1]
                        if tmp_x < 0 or tmp_x >= x_len or tmp_y < 0 or tmp_y >= y_len:
                            continue
                        area_num = area[tmp_y][tmp_x]
                        if area_num > 0 and area_num not in added:
                            cur_size += area_size[area_num]
                            added.append(area_num)
                    max_size = max(max_size, cur_size)
                else:
                    continue

        if max_size == float('-inf'):
            return x_len * y_len
        else:
            return max_size
