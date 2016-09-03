class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # [-2] [-2,0] [-2,0,-2] [1,0]
        assert len(nums) >= 1
        start = 0
        max_prod = float('-inf')
        for i, x in enumerate(nums):
            if x == 0:
                if i > start:
                    max_prod = max(self.maxProductNoZero(nums[start:i]), max_prod)
                start = i + 1
        if start < len(nums):
            max_prod = max(self.maxProductNoZero(nums[start:]), max_prod)
        if start != 0:
            # At least one zero is in `nums`
            max_prod = max(max_prod, 0)

        return max_prod


    def prod(self, nums):
        rv = 1
        for x in nums:
            rv *= x
        return rv


    def maxProductNoZero(self, nums):
        assert len(nums) >= 1
        if len(nums) == 1:
            return nums[0]
        negative_count = 0
        left_negative_index = None
        right_negative_index = None
        for i, x in enumerate(nums):
            if x < 0:
                negative_count += 1
                if left_negative_index is None:
                    left_negative_index = i
                right_negative_index = i
        if negative_count & 0x1 == 0:
            return self.prod(nums)
        max_prod = float('-inf')
        if left_negative_index < len(nums) - 1:
            max_prod = max(max_prod, self.prod(nums[left_negative_index+1:]))
        if right_negative_index > 0:
            max_prod = max(max_prod, self.prod(nums[:right_negative_index]))

        return max_prod


if __name__ == "__main__":
    assert Solution().maxProduct([3,-1,4]) == 4
    assert Solution().maxProduct([-2]) == -2
    assert Solution().maxProduct([0]) == 0
    assert Solution().maxProduct([-2,0]) == 0
    assert Solution().maxProduct([-2,0,-2]) == 0
    assert Solution().maxProduct([1,0]) == 1
    assert Solution().maxProduct([1,2,3,0,3,4]) == 12
    assert Solution().maxProduct([1,2,3]) == 6
    assert Solution().maxProduct([-4,-3]) == 12
