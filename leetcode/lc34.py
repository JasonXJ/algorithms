class Solution(object):
    def searchRange(self, nums, target):
        # Binary search for the higher boundary.
        l = 0
        r = len(nums)
        while l < r:
            m = (l+r)//2
            if nums[m] <= target:
                l = m + 1
            else:
                r = m
        # assert l == r
        # Now, we know that `nums[:l-1]` are <= target and `nums[l:]` are >
        # target.
        if l == 0 or nums[l-1] != target:
            return [-1, -1]
        higher_boundary = l - 1

        # Lower boundary
        l = 0
        r = len(nums)
        while l < r:
            m = (l+r)//2
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        # assert l == r
        # Now, we know that `nums[:l-1]` are < target and `nums[l:]` are >=
        # target.
        lower_boundary = l

        return [lower_boundary, higher_boundary]

def test():
    f = Solution().searchRange
    assert f([], 5) == [-1, -1]
    assert f([1, 2, 5, 6, 7], 5) == [2, 2]
    assert f([1, 2, 5, 5, 6, 7], 5) == [2, 3]
    assert f([5, 6, 7], 5) == [0, 0]
    assert f([5, 5, 6, 7], 5) == [0, 1]
    assert f([1, 2, 5], 5) == [2, 2]
    assert f([1, 2, 5, 5], 5) == [2, 3]
    assert f([2, 2], 3) == [-1, -1]
