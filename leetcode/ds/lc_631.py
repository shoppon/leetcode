from typing import List
from collections import defaultdict


class Excel:

    def __init__(self, H: int, W: str):
        self.row = H
        self.col = self.s2col(W) + 1
        self.values = [[0] * self.col for _ in range(H)]
        self.deps = defaultdict(list)

    @staticmethod
    def s2col(c):
        return 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(c)

    @staticmethod
    def col2s(c):
        return 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[c]

    @staticmethod
    def key(r: int, c: str):
        # 将坐标生成依赖列表的键
        return str(r) + c

    @staticmethod
    def coords(s):
        # 返回一个key的坐标
        return (int(s[:-1]), s[-1])

    def set(self, r: int, c: str, v: int) -> None:
        origin = self.get(r, c)
        for d in self.deps[str(r)+c]:
            self.set(*self.coords(d), self.get(*self.coords(d)) - origin + v)
        self.values[r-1][self.s2col(c)] = v
        # 将该坐标的依赖清空，但是不是直接依赖的不应该清空
        for v in self.deps.values():
            if self.key(r, c) in v:
                v.remove(self.key(r, c))

    def get(self, r: int, c: str) -> int:
        return self.values[r-1][self.s2col(c)]

    def sum(self, r: int, c: str, strs: List[str]) -> int:
        ret = 0
        for s in strs:
            if ':' not in s:
                # 依赖多次怎么办？？
                ret += self.get(int(s[1:]), s[0])
                self.deps[s[1:]+s[0]].append(str(r)+c)
            else:
                start, end = s.split(':')
                for col in range(self.s2col(start[0]), self.s2col(end[0])+1):
                    for row in range(int(start[1:]), int(end[1:])+1):
                        ret += self.values[row-1][col]
                        self.deps[str(row)+self.col2s(col)].append(str(r)+c)
        self.values[r-1][self.s2col(c)] = ret
        return ret
