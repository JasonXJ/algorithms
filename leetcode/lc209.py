# O(n) time, O(1) space solution
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        min_length = len(nums) + 1
        current_sum = 0
        for r in range(len(nums)):
            current_sum += nums[r]
            if current_sum >= s:
                while current_sum - nums[l] >= s:
                    current_sum -= nums[l]
                    l += 1
                length = r - l + 1
                if length < min_length:
                    min_length = length

        if min_length > len(nums):
            return 0
        return min_length


if __name__ == "__main__":
    assert Solution().minSubArrayLen(7, [2,3,1,2,4,3]) == 2
    assert Solution().minSubArrayLen(7, [2,3,1,7,4,3]) == 1
    assert Solution().minSubArrayLen(100, [2,3,1,7,4,3]) == 0
