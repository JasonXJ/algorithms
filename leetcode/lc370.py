class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        X = [0] * (length + 1)
        for si, ei, inc in updates:
            X[si] += inc
            X[ei + 1] -= inc
        rv = [X[0]] + [0] * (length - 1)
        for i in range(1, length):
            rv[i] = rv[i - 1] + X[i]

        return rv
