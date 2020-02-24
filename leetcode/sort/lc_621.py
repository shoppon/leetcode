from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        def op(k):
            return count[k]
        prio = {}
        count = {}
        for k in tasks:
            if k in count:
                count[k] += 1
                prio[k] -= 10000
            else:
                prio[k] = -10000
                count[k] = 1
        seq = []
        while tasks:
            avai = [t for t in tasks if prio[t] < 0]
            if avai:
                min_v = max(avai, key=op)
                prio[min_v] = n
                count[min_v] -= 1
                tasks.remove(min_v)
                seq.append(min_v)
            else:
                seq.append('')

            for k in prio:
                prio[k] -= 1

        return len(seq)
