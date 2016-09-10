import math
from collections import deque

# An O(n) solution making use of a deque. This solution is much simpler than
# :class:`SegmentSolution`.
class DequeSolution(object):
    def maxSlidingWindow(self, nums, k):
        if k == 0:
            assert len(nums) == 0
            return []
        if k == 1:
            return nums[:]
        
        # Each element in the deque is (index, value). Also, from left to
        # right, the elements have increasing indexes and decreasing values.
        d = deque()
        def add_to_deque(index):
            # First remove outdated element at the front.
            newest_outdated_index = index - k
            while len(d) and d[0][0] <= newest_outdated_index:
                d.popleft()

            # Remove elements with smaller value at the back
            value = nums[index]
            while len(d) and d[-1][1] <= value:
                d.pop()

            d.append((index, value))


        for i in range(k-1):
            add_to_deque(i)

        rv = []
        for i in range(k - 1, len(nums)):
            add_to_deque(i)
            rv.append(d[0][1])
        
        return rv


# O(n) solution by dividing `nums` into ``ceil(nums / k)`` segments (each
# except the last one has a length of k) and precompute the maximum values
# inside each segment (see the two arrays ``to_right`` and ``to_left``).
class SegmentSolution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == 0:
            assert len(nums) == 0
            return []
        if k == 1:
            return nums[:]
        NINF = float('-inf')

        to_right = [None] * len(nums)
        to_left = [None] * len(nums)
        for segment_start in range(0, len(nums), k):
            segment_max = NINF
            for i in range(segment_start, min(segment_start + k, len(nums))):
                segment_max = max(segment_max, nums[i])
                to_right[i] = segment_max
        # Note that we do not need to set the last segment in `to_left`
        for segment_start in range((int(math.ceil(float(len(nums)) / k)) - 2) * k, -1, -k):
            segment_max = NINF
            for i in range(segment_start + k - 1, segment_start - 1, -1):
                segment_max = max(segment_max, nums[i])
                to_left[i] = segment_max

        rv = []
        segment_start = 0
        while True:
            rv.append(to_right[segment_start + k - 1])
            i = segment_start + 1
            j = segment_start + k
            j_end = min(j + k - 1, len(nums))
            while j < j_end:
                rv.append(max(to_left[i], to_right[j]))
                i += 1
                j += 1
            if j >= len(nums):
                break

            segment_start += k


        return rv


def test():
    for Solution in (DequeSolution, SegmentSolution):
        assert Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]
        assert Solution().maxSlidingWindow([1,3,-1,-3,5,3,6], 3) == [3,3,5,5,6]
        assert Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7,8], 3) == [3,3,5,5,6,7,8]
        assert Solution().maxSlidingWindow([1,3,-1], 3) == [3]
        assert Solution().maxSlidingWindow([1,3,-1], 1) == [1,3,-1]
        assert Solution().maxSlidingWindow([9,10,9,-7,-4,-8,2,-6], 5) == [10, 10, 9, 2]
