class Solution(object):
    def jump(self, nums):
        # Greedy. O(n) time and O(1) space
        if len(nums) <= 1:
            return 0
        # Positions [i, j) have a jumps of ``next_jumps-1`` and positions [j,
        # k) have a jumps of ``next_jumps``
        i = 0
        j = k = 1
        next_jumps = 1
        while k < len(nums):
            if i < j:
                reach = nums[i] + i + 1
                if reach > k:
                    k = reach
                i += 1
            else:
                j = k
                next_jumps += 1

        return next_jumps


    def jump2(self, nums):
        if len(nums) <= 1:
            return 0

        import heapq
        heappop = heapq.heappop
        heappush = heapq.heappush

        can_reach = [nums[i]+i for i in range(len(nums))]
        min_jumps_heap = [(0, 0)]  # (jumps, index)
        i = 1
        end = len(nums) - 1
        while True:
            while True:
                jumps, index = min_jumps_heap[0]
                if can_reach[index] < i:
                    heappop(min_jumps_heap)
                else:
                    if i == end:
                        return jumps + 1
                    else:
                        heappush(min_jumps_heap, (jumps + 1, i))
                        break
            i += 1

    def jump1(self, nums):
        all_min_steps = [None]*len(nums)
        all_min_steps[0] = 0
        for i in range(1, len(nums)):
            min_steps = float('inf')
            for j in range(i):
                if i-j <= nums[j] and all_min_steps[j] < min_steps:
                    min_steps = all_min_steps[j]
            all_min_steps[i] = min_steps + 1

        return all_min_steps[-1]

def test():
    f = Solution().jump
    assert f([2,3,1,1,4]) == 2
    
