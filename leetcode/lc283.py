class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = j = 0
        while j < len(nums):
            if nums[j] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
            j += 1
