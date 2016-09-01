class Solution(object):
    def firstMissingPositive(self, nums):
        # This is a method of O(n) time and O(1) space. However, the `nums` is
        # modified (it is not clear that if it is appropriate).
        
        i = 0
        while i < len(nums):
            current = nums[i]

            if current == i+1:
                i += 1
                continue

            # Out of range. We do not need to consider this kind of numbers.
            # Note that if nums[i] == len(nums), then nums[-1] can store it.
            if current > len(nums) or current <= 0:
                i += 1
                continue

            # If we are here, ``1 <= current <= len(nums)``. Swap
            # `nums[current-1]` with `nums[i]` so that we "mark" the number
            # `current` as "existed".
            nums[i] = nums[current-1]
            nums[current-1] = current

            if nums[i] == current:
                # Depulicate number. Since the value `current` has already been
                # processed, we can skip it by increaing `i`.
                i += 1

        # Scan to see if which value is missing
        for i, x in enumerate(nums, 1):
            if i != x:
                return i
        return len(nums) + 1
