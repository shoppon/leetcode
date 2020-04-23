from unittest import TestCase
from leetcode.ds import lc_631


class Test631(TestCase):
    def test0(self):
        excel = lc_631.Excel(6, 'D')
        excel.set(4, 'C', 2)
        excel.set(5, 'C', 3)
        self.assertEquals(2, excel.get(4, 'C'))
        self.assertEquals(5, excel.sum(6, 'D', ['A1', 'B2:D5']))
        excel.set(5, 'C', 4)
        self.assertEquals(6, excel.get(6, 'D'))

    def test1(self):
        excel = lc_631.Excel(3, 'C')
        excel.sum(1, 'A', ['A2'])
        excel.set(2, 'A', 1)
        self.assertEquals(1, excel.get(1, 'A'))

    def test2(self):
        excel = lc_631.Excel(5, 'E')
        excel.set(1, 'A', 1)
        excel.sum(2, 'B', ['A1'])
        excel.set(2, 'B', 0)
        excel.set(1, 'A', 5)
        self.assertEquals(0, excel.get(2, 'B'))
