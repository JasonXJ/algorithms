class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []

        nums.sort()
        data = []
        for x in nums:
            longest = 0
            for i in range(len(data)):
                if x % nums[i] == 0:
                    if data[i][1] > longest:
                        prev = i
                        longest = data[i][1]
            if longest == 0:
                data.append((None, 1))
            else:
                data.append((prev, longest + 1))

        index = max(range(len(data)), key=lambda x:data[x][1])
        rv = [None] * data[index][1]
        rv_index = len(rv)
        for rv_index in range(len(rv) - 1, -1, -1):
            rv[rv_index] = nums[index]
            index = data[index][0]

        return rv


def test():
    assert Solution().largestDivisibleSubset([1,2,3]) == [1,2]
