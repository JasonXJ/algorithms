class Solution(object):
    def searchInsert(self, nums, target):
        l = 0
        h = len(nums) - 1
        while h >= l:
            m = (h + l) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                h = m - 1
            else:
                l = m + 1
        return l
