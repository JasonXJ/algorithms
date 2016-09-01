class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = {}
        

class Trie(object):

    def __init__(self):
        self.root = TrieNode()


    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for x in word:
            try:
                node = node.children[x]
            except KeyError:
                new_node = TrieNode()
                node.children[x] = new_node
                node = new_node
        # Mark the end of a word
        node.children[None] = None
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self._nodeSearch(word)
        return node is not None and None in node.children


    def _nodeSearch(self, prefix):
        node = self.root
        for x in prefix:
            node = node.children.get(x)
            if node is None:
                return None
        return node
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        return self._nodeSearch(prefix) is not None
        

# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")

if __name__ == "__main__":
    trie = Trie()
    trie.insert('abc')
    trie.insert('ab')

    assert trie.startsWith('a')
    assert trie.startsWith('abc')
    assert trie.search('abc')
    assert trie.search('ab')
    assert trie.search('a') == False
    assert trie.search('ac') == False
    assert trie.search('bc') == False
