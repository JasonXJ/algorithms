# O(n^2)
class Solution(object):
    def threeSumSmaller(self, nums, target):
        nums.sort()
        count = 0
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while True:
                while j < k and nums[i] + nums[j] + nums[k] >= target:
                    k -= 1
                if j < k:
                    count += k - j
                    j += 1
                else:
                    break

        return count


# O(n^2)
class Solution2(object):
    def threeSumSmaller(self, nums, target):
        nums.sort()
        triple_count = 0
        for i in range(len(nums)):
            adjusted_target = target - nums[i]
            
            # Count the number of pairs (j, k) such that ``nums[j]+nums[k] <
            # adjusted_target and j < k`` in O(n) time
            j_candidates = 0
            for k in range(len(nums) - 1, 0, -1):
                if k == i:
                    continue
                vk = nums[k]
                while j_candidates < k and nums[j_candidates] + vk < adjusted_target:
                    j_candidates += 1
                if j_candidates > k:
                    j_candidates = k
                # Each time we reach here, there is `j_candidates` candidates
                # for the index j.
                triple_count += j_candidates
                if i < j_candidates:
                    # One of the "j candidates" is i itself, we need to remove
                    # that.
                    triple_count -= 1

        return triple_count // 3


# O(n^2 log n) solution
class SlowerSolution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        from bisect import bisect_left
        sorted_nums = sorted(nums)
        triple_count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                vi = nums[i]
                vj = nums[j]
                vk_upper = target - vi - vj
                triple_count += bisect_left(sorted_nums, vk_upper)
                if vi < vk_upper:
                    triple_count -= 1
                if vj < vk_upper:
                    triple_count -= 1

        return triple_count // 3




def test():
    assert Solution().threeSumSmaller([-2,0,1,3], 2) == 2
    assert Solution().threeSumSmaller([1,2,3], 6) == 0
    assert Solution().threeSumSmaller([1,2,3], 7) == 1
    assert Solution().threeSumSmaller([1,1,3], 6) == 1
    assert Solution().threeSumSmaller([3,1,0,-2], 4) == 3
