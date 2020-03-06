from collections import defaultdict


class Solution:
    def checkInclusion1(self, s1: str, s2: str) -> bool:
        freq = defaultdict(int)
        queue = defaultdict(list)
        for s in s1:
            freq[s] += 1
        used = [0] * len(s2)
        s1_len = len(s1)
        count = s1_len
        for i, s in enumerate(s2):
            # 出队的加回来
            pre = i-s1_len
            if pre >= 0 and used[pre] == 1:
                freq[s2[pre]] += 1
                count += 1
                used[pre] = 0
                queue[s2[pre]].pop(0)
            if freq[s] == 0 and queue[s]:
                queue[s].append(i)
                pre = queue[s].pop(0)
                used[pre] = 0
                used[i] = 1
            if freq[s] > 0:
                freq[s] -= 1
                count -= 1
                used[i] = 1
                queue[s].append(i)

            if count == 0:
                return True

        return False

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        freq1 = {}
        freq2 = {}
        for s in ('abcdefghijklmnopqrstuvwxyz'):
            freq1[s], freq2[s] = 0, 0
        for _s1, _s2 in zip(s1, s2):
            freq1[_s1] += 1
            freq2[_s2] += 1
        if freq1 == freq2:
            return True
        s1_len = len(s1)
        for i in range(s1_len, len(s2)):
            freq2[s2[i]] += 1
            freq2[s2[i-s1_len]] -= 1
            if freq1 == freq2:
                return True
        return False
