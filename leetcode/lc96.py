#!/usr/bin/env python3

class Solution(object):
    def numTrees(self, n):
        cache = {0:1, 1:1}
        def _numTrees(n):
            assert n >= 0
            if n in cache:
                return cache[n]
            count = 0
            for i in range(n):
                count += _numTrees(i) * _numTrees(n - i - 1)

            cache[n] = count
            return count
        
        return _numTrees(n)

if __name__ == "__main__":
    print(Solution().numTrees(3))
