class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return []
        rv = []

        def update_rv(start, end):
            if start == end:
                rv.append(str(start))
            else:
                rv.append('{}->{}'.format(start, end))

        current_start = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                update_rv(current_start, nums[i-1])
                current_start = nums[i]
        update_rv(current_start, nums[-1])

        return rv


def test():
    assert Solution().summaryRanges([0,1,2,4,5,7]) == ['0->2', '4->5', '7']
    assert Solution().summaryRanges([0,1,2,4,5,6,7]) == ['0->2', '4->7']
    assert Solution().summaryRanges([0,1,2,3,4,5,6,7]) == ['0->7']
    assert Solution().summaryRanges([]) == []
    assert Solution().summaryRanges([0]) == ['0']
    assert Solution().summaryRanges([0,2]) == ['0','2']
    assert Solution().summaryRanges([0,2,4]) == ['0', '2', '4']
