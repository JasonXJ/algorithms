from collections import Counter

class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return sum(cc & 1 for c, cc in Counter(s).items()) <= 1


def test():
    assert Solution().canPermutePalindrome('')
    assert Solution().canPermutePalindrome('a')
    assert Solution().canPermutePalindrome('aaa')
    assert Solution().canPermutePalindrome('code') == False
    assert Solution().canPermutePalindrome('aab')
    assert Solution().canPermutePalindrome('carerac')
