class Solution(object):
    def numDecodings(self, s):
        ways = [None] * len(s)
        ways[0] = 1

        for c in s:
