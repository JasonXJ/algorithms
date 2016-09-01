class Solution(object):
    def canJump(self, nums):
        reachable = 0
        for i in range(len(nums)):
            if i > reachable:
                return False
            current_reachable = nums[i] + i
            if current_reachable >= reachable:
                reachable = current_reachable

        return True
