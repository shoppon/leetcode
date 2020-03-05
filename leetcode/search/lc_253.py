from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        ans = 0
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        while sorted_intervals:
            first = sorted_intervals.pop(0)
            to_remove = []
            for t in sorted_intervals:
                if t[0] >= first[1]:
                    to_remove.append(t)
                    first = t
            for t in to_remove:
                sorted_intervals.remove(t)
            to_remove = []
            ans += 1
        return ans
