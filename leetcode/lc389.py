from collections import Counter

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        for c, count in (Counter(t) - Counter(s)).items():
            if count != 0:
                return c
