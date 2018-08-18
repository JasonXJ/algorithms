class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if len(nums) == 1:
            return 1 if S == nums[0] or S == -nums[0] else 0

        if nums[0] == 0:
            dp = {0: 2}
        else:
            dp = {nums[0]: 1, -nums[0]: 1}
        for x in nums[1:-1]:
            new_dp = {}
            for y, count in dp.items():
                new_dp[y+x] = new_dp.get(y+x, 0) + count
                new_dp[y-x] = new_dp.get(y-x, 0) + count
            dp = new_dp

        return dp.get(S-nums[-1], 0) + dp.get(S+nums[-1], 0)
