class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []

        if a == 0:
            if b == 0:
                return [c] * len(nums)
            elif b > 0:
                return [b*x+c for x in nums]
            else:  # b < 0
                return [b*x+c for x in reversed(nums)]
        else:
            mid = - float(b) / 2 / a
            l = 0
            r = len(nums) - 1
            rv = [None] * len(nums)
            if a > 0:
                index = len(nums) - 1
                index_delta = -1
            else:
                index = 0
                index_delta = 1
            while l <= r:
                if abs(mid - nums[l]) <= abs(mid - nums[r]):
                    x = nums[r]
                    r -= 1
                else:
                    x = nums[l]
                    l += 1
                rv[index] = a*x*x + b*x + c
                index += index_delta

        return rv


def test():
    def check(nums, a, b, c):
        assert (Solution().sortTransformedArray(nums, a, b, c) ==
                sorted([a*x*x + b*x + c for x in nums]))

    check([-4, -2, 2, 4], 1, 3, 5)
    check([-4, -2, 2, 4], -1, 3, 5)
    check([-4, -2, 2, 4], 0, 3, 5)
    check([-4, -2, 2, 4], 0, 0, 5)
    check([], 0, 0, 5)
    check([5], 0, 0, 5)
    check([5], 1, 3, 5)
    check([5], -1, 3, 5)
