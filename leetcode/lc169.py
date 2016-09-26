from collections import Counter

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = Counter(nums)
        target = len(nums) // 2
        for x, c in counter.items():
            if c > target:
                return x
