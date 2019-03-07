class Trie(object):

    def __init__(self, start=None):
        """
        Initialize your data structure here.
        """
        self.start = start
        self.is_end = False
        self.children = []

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        if len(word) == 0:
            self.is_end = True
            return
        first = word[0]
        last = word[1:]
        for c in self.children:
            if c.start == first:
                c.insert(last)
                break
        else:
            trie = Trie(first)
            trie.insert(last)
            self.children.append(trie)

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        for c in self.children:
            first = word[0]
            last = word[1:]
            if c.start == first:
                if len(last) == 0:
                    return c.is_end
                else:
                    return c.search(last)
        else:
            return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        for c in self.children:
            first = prefix[0]
            last = prefix[1:]
            if c.start == first:
                if len(last) == 0:
                    return True
                else:
                    return c.startsWith(last)
        else:
            return False
