from typing import List


class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        ans = [0] * 8

        def next_status(cells):
            for i in range(1, 7):
                if cells[i-1] == cells[i+1]:
                    ans[i] = 1
                else:
                    ans[i] = 0

        for _ in range(N % 14 + 14):
            next_status(cells)
            cells = ans[:]

        return ans
