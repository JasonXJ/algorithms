import random
from bisect import bisect_left

class Solution:

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.cum_weight = w[:]
        c = self.cum_weight[0]
        for i in range(1, len(self.cum_weight)):
            c += self.cum_weight[i]
            self.cum_weight[i] = c
        

    def pickIndex(self):
        """
        :rtype: int
        """
        return bisect_left(self.cum_weight, random.randrange(1, self.cum_weight[-1]+1))


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
