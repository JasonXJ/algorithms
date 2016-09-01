class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {}
        for i, x in enumerate(nums):
            try:
                nums_dict[x].append(i)
            except KeyError:
                nums_dict[x] = [i]
        for num, indices in nums_dict.items():
            new_target = target - num
            # XXX Trick: there is always exact one solution
            if new_target == num:
                return indices
            indices2 = nums_dict.get(target-num)
            if indices2 is not None:
                return indices[0], indices2[0]

print(Solution().twoSum([-3,4,3,90], 0))
