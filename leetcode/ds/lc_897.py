from collections import defaultdict


class FreqStack1:

    def __init__(self):
        self.elems = {}
        self.index = 0

    def push(self, x: int) -> None:
        if x in self.elems:
            self.elems[x][0] += 1
            self.elems[x][1].append(self.index)
        else:
            self.elems[x] = [1, [self.index]]
        self.index += 1

    def pop(self) -> int:
        key, max_v, max_idx = 0, 0, 0
        for k, v in self.elems.items():
            if v[0] > max_v or (v[0] == max_v and v[1][-1] > max_idx):
                key, max_v, max_idx = k, v[0], v[1][-1]
        if max_v == 1:
            self.elems.pop(key)
        else:
            self.elems[key][0] -= 1
            self.elems[key][1].pop()
        return key


class FreqStack:

    def __init__(self):
        # 频率字典
        self.freq = defaultdict(int)
        # 元素字典，出现N次的数组
        self.elems = defaultdict(list)
        self.max_freq = 0

    def push(self, x: int) -> None:
        freq = self.freq[x] + 1
        self.freq[x] = freq
        # freq数组中记录该元素
        self.elems[freq].append(x)
        self.max_freq = max(freq, self.max_freq)

    def pop(self) -> int:
        elem = self.elems[self.max_freq].pop()
        self.freq[elem] -= 1
        if len(self.elems[self.max_freq]) == 0:
            self.max_freq -= 1
        return elem
