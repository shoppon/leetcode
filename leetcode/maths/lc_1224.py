# coding: utf-8
from typing import List
from collections import defaultdict


class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        def jduge(freq, count):
            freq_set = set(freq.values())
            if 0 in freq_set:
                freq_set.remove(0)
            value_count = len(freq_set)
            if value_count >= 3:
                return False
            elif value_count == 2:
                # 多的只有一个
                min_v = min(freq_set)
                max_v = max(freq_set)
                if count[min_v] == 1 and min_v == 1:
                    return True
                return count[max_v] == 1 and max_v - min_v == 1
            else:
                f = freq_set.pop()
                return f == 1 or len(freq) == 1

        freqs = defaultdict(int)
        count = defaultdict(int)
        for n in nums:
            freqs[n] += 1
            count[freqs[n]] += 1
            count[freqs[n] - 1] -= 1
        while nums:
            if jduge(freqs, count):
                return len(nums)
            top = nums.pop()
            count[freqs[top]] -= 1
            freqs[top] -= 1
            count[freqs[top]] += 1

        return 0
