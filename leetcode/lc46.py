class Solution(object):
    def permute(self, nums):
        rv = []
        def inner(current_pos):
            if current_pos == len(nums):
                rv.append(nums[:])
                return
            for i in range(current_pos, len(nums)):
                nums[current_pos], nums[i] = nums[i], nums[current_pos]
                inner(current_pos+1)
                nums[current_pos], nums[i] = nums[i], nums[current_pos]
        
        inner(0)
        return rv
