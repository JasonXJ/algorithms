class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def get_val(i):
            if i < 0:
                return 1
            elif i >= len(nums):
                return 1
            return nums[i]

        # memo[(i,j)] is the maximum coins we get if only the range [i, j) is considered.
        memo = {
            (i, i): 0
            for i in range(len(nums) + 1)
        }
        for size in range(1, len(nums) + 1):
            for i in range(len(nums) - size + 1):
                j = i + size
                memo[(i, j)] = max(
                    memo[(i, k)] + memo[(k + 1, j)] + get_val(k)*get_val(i-1)*get_val(j)
                    for k in range(i, j)
                )

        return memo[(0, len(nums))]


def test():
    assert Solution().maxCoins([3, 1, 5, 8]) == 167
