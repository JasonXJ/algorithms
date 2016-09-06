class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        assert upper >= lower
        if len(nums) > 0:
            assert nums[0] >= lower
            assert nums[-1] <= upper

        rv = []
        nums_x = [lower - 1] + nums + [upper + 1]
        for i in range(len(nums_x) - 1):
            r = self._missing_range(nums_x[i], nums_x[i+1])
            if r is not None:
                rv.append(r)

        return rv


    def _missing_range(self, num1, num2):
        assert num2 >= num1
        if num1 == num2 or num1 + 1 == num2:
            return None
        if num1 + 2 == num2:
            return str(num1+1)
        return '{}->{}'.format(num1+1, num2-1)


def test():
    assert Solution().findMissingRanges([0,1,3,50,75], 0, 99) == ['2', '4->49', '51->74', '76->99']
    assert Solution().findMissingRanges([], 0, 99) == ['0->99']
    assert Solution().findMissingRanges([], 0, 0) == ['0']
    assert Solution().findMissingRanges([], 0, 0) == ['0']
    assert Solution().findMissingRanges([1,3,5], 0, 6) == ['0','2','4','6']
    assert Solution().findMissingRanges([1,3,5], 1, 5) == ['2','4']
