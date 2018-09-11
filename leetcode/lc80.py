class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        last = None
        c = 0
        for x in nums:
            if x != last:
                c = 1
                last = x
            else:
                c += 1
                if c > 2:
                    continue
            nums[i] = x
            i += 1

        return i
