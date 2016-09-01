from collections import Counter

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = Counter(s)
        for i, x in enumerate(s):
            if c[x] == 1:
                return i
        return -1

if __name__ == "__main__":
    assert Solution().firstUniqChar('loveleetcode') == 2
