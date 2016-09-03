# An average O(n) solution using partition
from random import randint, random

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        lo = 0
        hi = len(nums) - 1
        target = len(nums) - k

        while True:
            i = j = lo
            # Randomize
            rand_index = randint(lo, hi)
            nums[hi], nums[rand_index] = nums[rand_index], nums[hi]
            x = nums[hi]
            while j < hi:
                # Extra randomize to prevent attack
                if nums[j] < x or (nums[j] == x and random() < 0.5):
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                j += 1
            nums[i], nums[hi] = nums[hi], nums[i]
            if i == target:
                return nums[i]
            elif i > target:
                hi = i - 1
            else:
                lo = i + 1


def test():
    assert Solution().findKthLargest([3,2,1,5,6,4], 2) == 5
    assert Solution().findKthLargest([3,2,1,5,6,4], 6) == 1
    assert Solution().findKthLargest([3,2,1,5,6,4], 1) == 6
    assert Solution().findKthLargest([3,2,1,6,5,6,4], 1) == 6
    assert Solution().findKthLargest([3,2,1,6,5,6,4], 2) == 6
    assert Solution().findKthLargest([3,2,1,6,5,6,4], 3) == 5
