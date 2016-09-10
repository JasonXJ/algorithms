class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1):
            if i & 1 == 0:
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
            elif nums[i] < nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
