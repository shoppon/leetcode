from unittest import TestCase

from leetcode import lc_208


class MyTC(TestCase):
    def test_input1(self):
        obj = lc_208.Trie()
        word = 'word'
        obj.insert(word)
        obj.insert('wold')
        self.assertEquals(True, obj.search(word))
        self.assertEquals(True, obj.startsWith('wo'))
        self.assertEquals(False, obj.startsWith('oll'))
        self.assertEquals(False, obj.search('or'))
