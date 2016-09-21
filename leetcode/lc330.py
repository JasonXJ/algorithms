# TODO: Prove the correctness of greedy patching the smallest unformable
# number.
# O(log n) solution (``len(nums)`` is ignored).
class Solution(object):
    def minPatches(self, nums, n):
        patch = 0
        next_unformable = 1
        nums_index = 0
        while next_unformable <= n:
            # Invariant: Upon here, 1) `next_unformable` is exactly 1 larger than
            # the sum of all numbers in nums[:nums_index] and all the patched
            # numbers; 2) Numbers in nums[:nums_index] and all the patched
            # numbers can form any number between 1 (inclusive) and
            # `next_unformable` (exclusive). Also note that the patched numbers
            # are not explicitly stored.

            if nums_index < len(nums) and next_unformable >= nums[nums_index]:
                next_member = nums[nums_index]
                nums_index += 1
            else:
                # We will need to patch the current value of `next_unformable`
                next_member = next_unformable
                patch += 1

            # Since 1 ~ `next_unformable` - 1 are formable, add the
            # `next_member` allows us to form any number between 1 ~
            # `next_unformable` + `next_member` - 1. 
            next_unformable += next_member

        return patch


# O(n^2) solution (``len(nums)`` is ignored). This version should also be
# correct, but it cannot due with large input.
class Solution2(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0
        def init():
            can_form = [True] + [False] * n
            self.can_form_count = 0
            
            def init_fill(nums_start_index=0, current=0):
                if current > n:
                    return
                if nums_start_index >= len(nums):
                    if not can_form[current]:
                        can_form[current] = True
                        self.can_form_count += 1
                else:
                    init_fill(nums_start_index + 1, current)
                    init_fill(nums_start_index + 1, current + nums[nums_start_index])

            init_fill()
            return can_form, self.can_form_count


        can_form, can_form_count = init()
        if can_form_count == n:
            return 0
        patch_count = 0
        for i in range(1, n+1):
            assert can_form_count < n
            if can_form[i] == False:
                # Patch number `i`

                patch_count += 1
                # Note that must from right to left, otherwise we might be
                # using `i` multiple time.
                for j in range(n - i, -1, -1):
                    if can_form[j] and not can_form[i + j]:
                        can_form[i + j] = True
                        can_form_count += 1
                if can_form_count == n:
                    break

        assert can_form_count == n
        return patch_count


def test():
    assert Solution().minPatches([1, 3], 6) == 1
    assert Solution().minPatches([1, 5, 10], 20) == 2
    assert Solution().minPatches([1, 2, 2], 5) == 0
    assert Solution().minPatches([], 1) == 1
    assert Solution().minPatches([1,2,31,33], 2147483647) == 28
