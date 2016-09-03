from collections import Counter

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        processed_candidates = sorted(Counter(candidates).items())
        rv = []

        def search(start_index, prefix, prefix_sum):
            if prefix_sum == target:
                rv.append(prefix[:])
                return
            if prefix_sum > target:
                return
            if start_index >= len(processed_candidates):
                return
            x, max_count = processed_candidates[start_index]
            if x > target - prefix_sum:
                # End the whole search along the path
                return
            search(start_index+1, prefix, prefix_sum)
            for count in range(max_count):
                prefix.append(x)
                prefix_sum += x
                search(start_index+1, prefix, prefix_sum)
            del prefix[-max_count:]
            prefix_sum -= max_count*x


        search(0, [], 0)
        return rv


def test():
    def sub_test(candidates, target, expected):
        rv = Solution().combinationSum2(candidates, target)
        assert sorted(rv) == sorted(expected)

    
    sub_test([10, 1, 2, 7, 6, 1, 5], 8, [
        [1, 7],
        [1, 2, 5],
        [2, 6],
        [1, 1, 6]
    ])

    sub_test([1,1,2,2,3,4], 13, [[1,1,2,2,3,4]])
    sub_test([1,1,2,2,3,4], 14, [])
    sub_test([1,1,2,2,3,4], 6, [
        [1,1,2,2],
        [1,2,3],
        [1,1,4],
        [2,4],
    ])
