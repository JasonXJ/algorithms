# The hint recommends to use a trie. However, using a trie does not necessarily
# improve the efficiency.
class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.trie = {}
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.trie
        for x in word:
            node = node.setdefault(x, {})
        node[None] = None
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self._search(word, 0, self.trie)


    def _search(self, word, start_index, node):
        for i in range(start_index, len(word)):
            if word[i] == '.':
                for child in node.values():
                    if child is not None and self._search(word, i + 1, child):
                        return True
                return False
            else:
                node = node.get(word[i])
                if node is None:
                    return False
        return None in node


def test():
    wd = WordDictionary()
    wd.addWord('bad')
    wd.addWord('dad')
    wd.addWord('mad')
    wd.addWord('mak')
    assert not wd.search('pad')
    assert wd.search('bad')
    assert wd.search('.ad')
    assert wd.search('b..')
    assert wd.search('.a.')
    assert not wd.search('p..')
    assert wd.search('mad')
    assert wd.search('mak')
    assert not wd.search('makf')
    assert not wd.search('ma')
