from unittest import TestCase
from leetcode.ds import lc_897


class Test897(TestCase):
    def test0(self):
        fs = lc_897.FreqStack()
        fs.push(5)
        fs.push(7)
        fs.push(5)
        fs.push(7)
        fs.push(4)
        fs.push(5)
        self.assertEquals(5, fs.pop())
        self.assertEquals(7, fs.pop())
        self.assertEquals(5, fs.pop())
        self.assertEquals(4, fs.pop())
