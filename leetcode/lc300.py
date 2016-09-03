from bisect import bisect_left

# See https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest_lst = [float('-inf')] + [float('+inf')]*(len(nums))
        global_longest = 0

        for x in nums:
            local_longest = bisect_left(longest_lst, x, 0, global_longest + 1)
            if x < longest_lst[local_longest]:
                longest_lst[local_longest] = x
            if local_longest > global_longest:
                global_longest = local_longest

        return global_longest


if __name__ == "__main__":
    print(Solution().lengthOfLIS([2,2]))
    print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18, 101]))
