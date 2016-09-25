# O(n) algorithm.
class Solution(object):
    """ This is an O(n) greedy algorithm. The idea is that whenever we see a
    increasing/descreasing sequence, we select the last element of this
    sequence (i.e. the largest/smallest element of the sequence). For example,
    for an array of ``[1, 2, 3, 4, 3, 5, 4, 3]`, we generate a wiggle array of
    `[1, 4, 3, 5, 3]` (Note that for the first increasing or descreasing
    sequence, the first element is also selected, so we select 1 and 4 from the
    first 4 element ``[1,2,3,4]``). The reason this work is because we cannot
    select more than one value in a increasing/descreasing sequence (except for
    the first sequence); therefore, we select the one most valuable value,
    which is the largest/smallest value.
    
    """
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)

        # Find the first value different from nums[0]
        i = 1
        while i < len(nums):
            if nums[i] != nums[0]:
                break
            i += 1

        if i == len(nums):
            return 1

        rv = 2
        next_smaller = nums[0] < nums[i]
        i += 1
        while i < len(nums):
            if ((next_smaller and nums[i - 1] > nums[i]) or
                    (not next_smaller and nums[i - 1] < nums[i])):
                next_smaller = not next_smaller
                rv += 1
            i += 1

        return rv


def test():
    assert Solution().wiggleMaxLength([1,7,4,9,2,5]) == 6
    assert Solution().wiggleMaxLength([1,3,5,4]) == 3
    assert Solution().wiggleMaxLength([1,1,1,1]) == 1
