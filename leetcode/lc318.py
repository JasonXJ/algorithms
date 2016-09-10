class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # First convert each word to an integer. Two words do not share common
        # letters iff ``bits1 & bits2 == 0``
        bit_lst = []
        ord_a = ord('a')
        for w in words:
            bits = 0
            for x in w:
                bits |= (1 << (ord(x) - ord_a))
            bit_lst.append(bits)

        maximum = 0
        for i in range(len(bit_lst)):
            for j in range(i + 1, len(bit_lst)):
                if bit_lst[i] & bit_lst[j] == 0:
                    maximum = max(maximum, len(words[i]) * len(words[j]))

        return maximum


def test():
    assert Solution().maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]) == 16
    assert Solution().maxProduct(["a", "ab", "abc", "d", "cd", "bcd", "abcd"]) == 4
    assert Solution().maxProduct(["a", "aa", "aaa", "aaaa"]) == 0
