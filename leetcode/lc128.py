# O(n)
class Solution(object):
    def longestConsecutive(self, nums):
        # ``entry_map[i] = [l,r]`` means that we found a consecutive sequence
        # l, l+1, ..., r and l <= i <= r. Note that to save time, we will only
        # update ``entry_map[i]`` if `i` is the the first or last number in the
        # new sequence, which is OK because at the end we only need to return
        # the global longest length.
        entry_map = {}
        for x in nums:
            if x in entry_map:
                continue
            prev_range = entry_map.get(x-1, None)
            next_range = entry_map.get(x+1, None)
            if prev_range is not None:
                if next_range is not None:
                    # Merge the range
                    entry_map[x] = prev_range
                    prev_range[-1] = next_range[-1]
                else:
                    prev_range[-1] = x
                entry_map[prev_range[-1]] = prev_range
            elif next_range is not None:
                next_range[0] = x
                entry_map[x] = next_range
            else:
                # Both the prev_/next_range is None
                entry_map[x] = [x, x]

        
        max_length = 0
        # Note that ``len(entry_map) <= len(nums)``, so it is still O(n).
        for range_left, range_right in entry_map.values():
            max_length = max(max_length, range_right - range_left + 1)

        return max_length


def test():
    assert Solution().longestConsecutive([1,2,3,4,5]) == 5
    assert Solution().longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
    assert Solution().longestConsecutive([1,2,9,4,5]) == 2
    assert Solution().longestConsecutive([1,2,4,5,3]) == 5
    assert Solution().longestConsecutive([1,2,2,4,5,3]) == 5
