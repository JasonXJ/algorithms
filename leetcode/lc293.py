class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        rv = []
        for i in range(len(s) - 1):
            if '+' == s[i] == s[i+1]:
                rv.append(s[:i] + '--' + s[i+2:])

        return rv
