class ValidWordAbbr(object):
    DUPLICATE = object()

    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.table = {}
        for s in dictionary:
            key = self._to_tuple(s)
            value = self.table.get(key)
            if value is None:
                self.table[key] = s
            elif value is not self.DUPLICATE and value != s:
                # More than one string has the same abbreviation
                self.table[key] = self.DUPLICATE
        

    @staticmethod
    def _to_tuple(s):
        if s == '':
            return (None, None, 0)
        return (s[0], s[-1], len(s))


    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        value = self.table.get(self._to_tuple(word))
        if value is None:
            return True
        if value is not self.DUPLICATE and value == word:
            return True
        return False


# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")

def test1():
    o = ValidWordAbbr(['hello'])
    assert o.isUnique('hello')
    assert o.isUnique('')
    assert o.isUnique('habco') == False
    assert o.isUnique('helllo')
    
def test2():
    o = ValidWordAbbr(['', 'ab','aab', 'bab', 'bcb', 'abcd', 'abcd'])
    assert o.isUnique('')
    assert o.isUnique('ab')
    assert o.isUnique('aab')
    assert o.isUnique('abb') == False
    assert o.isUnique('bab') == False
    assert o.isUnique('bcb') == False
    assert o.isUnique('bdb') == False
    assert o.isUnique('abcd')
