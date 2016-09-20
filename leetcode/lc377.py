class Solution(object):
    def combinationSum4(self, nums, target):
        ways = [1] + [0] * target
        for x in range(1, target + 1):
            s = 0
            for n in nums:
                x2 = x - n
                if x2 >= 0:
                    s += ways[x2]
            ways[x] = s
        
        return ways[target]


# This get stackoverflow on leet code
class RecursiveSolution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = {}

        def ways(target):
            if target == 0:
                return 1
            elif target < 0:
                return 0
            try:
                return dp[target]
            except KeyError:
                pass
            count = sum(ways(target - x) for x in nums)
            dp[target] = count
            return count

        return ways(target)


def test():
    assert Solution().combinationSum4([1,2,3], 4) == 7
    assert Solution().combinationSum4([3,33,333], 10000) == 0
