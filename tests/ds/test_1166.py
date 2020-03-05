from unittest import TestCase

from leetcode.ds import lc_1166


class Test1166(TestCase):
    def test0(self):
        fs = lc_1166.FileSystem()
        fs.createPath("/lee", 1)
        self.assertEquals(1, fs.get("/lee"))
        self.assertEquals(False, fs.createPath("/lee", 2))
        fs.createPath("/lee/code", 1)
        self.assertEquals(False, fs.createPath("/lee/code", 2))

    def test1(self):
        fs = lc_1166.FileSystem()
        fs.createPath("/lee", 1)
        fs.createPath("/lee/code", 1)
        fs.createPath("/lee/code/lee", 1)
        fs.createPath("/lee/code/lee/code", 4)
        self.assertEquals(4, fs.get("/lee/code/lee/code"))

    def test2(self):
        fs = lc_1166.FileSystem()
        self.assertEquals(False, fs.createPath("/lee/code", 1))
