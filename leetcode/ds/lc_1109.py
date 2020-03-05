from typing import List
from collections import defaultdict


class Solution:
    def corpFlightBookings1(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0] * n
        for s, e, v in bookings:
            for i in range(s, e+1):
                ans[i-1] += v
        return ans

    def corpFlightBookings2(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0] * n
        cache = defaultdict(int)
        for s, e, v in bookings:
            cache[(s, e)] += v
        for k, v in cache.items():
            for i in range(k[0], k[1]+1):
                ans[i-1] += v
        return ans

    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0] * n
        for s, e, v in bookings:
            ans[s-1] += v
            if e < n:
                ans[e] -= v
        for i in range(1, n):
            ans[i] = ans[i] + ans[i-1]
        return ans
