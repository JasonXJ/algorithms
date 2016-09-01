class Solution(object):
    def combinationSum(self, candidates, target):
        assert target > 0
        rv = []
        counts = [0] * len(candidates)
        candidates = sorted(candidates)

        def append_new_result():
            temp = []
            for count, value in zip(counts, candidates):
                for i in range(count):
                    temp.append(value)
            rv.append(temp)

        def backtrack(pos, remain):
            # print('{} \t {} \t {}'.format(pos, remain, counts))
            candidate = candidates[pos]
            if pos == len(candidates) - 1:  # Last candidate
                a, b = divmod(remain, candidates[pos])
                if b == 0:
                    counts[-1] = a
                    append_new_result()
                return
            counts[pos] = 0
            backtrack(pos+1, remain)  # Do not use current candidate
            while remain >= candidate:  # Use at least one current candidate
                counts[pos] += 1
                remain -= candidate
                backtrack(pos+1, remain)

        backtrack(0, target)
        return rv

print(Solution().combinationSum([2,3,6,7], 7))
