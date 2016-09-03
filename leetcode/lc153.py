# O(log n)
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        assert len(nums) >= 1
        if len(nums) == 1:
        	return nums[0]
        lo = 0
        hi = len(nums) - 1
        if nums[lo] < nums[hi]:
        	# It is still sorted
        	return nums[lo]

        while hi - lo > 1:
        	m = (lo + hi) // 2
        	if nums[m] < nums[lo]:
        		hi = m
        	else:
        		lo = m

        return nums[hi]


def test():
    assert Solution().findMin([1,2,3,4]) == 1
    assert Solution().findMin([1]) == 1
    assert Solution().findMin([1,2]) == 1
    assert Solution().findMin([2,1]) == 1
    assert Solution().findMin([4,5,6,1,2]) == 1
