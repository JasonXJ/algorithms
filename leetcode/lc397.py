# The post pasted after provides an interesting view and solution for this
# problem.
# https://discuss.leetcode.com/topic/58334/a-couple-of-java-solutions-with-explanations

class Solution(object):
    """ Recursive. The idea is that if the current number is even, we always
    choose to divide it by 2 instead of +1 or -1. The reason is that divide it
    by two can bring it closer to 1 sooner and it also bring the number closer
    to the nearest power of two sooner. """
    def integerReplacement(self, n):
        memo = {1:0}

        def steps(n):
            try:
                return memo[n]
            except KeyError:
                pass
            if n & 1 == 0:
                # Even number, we always divide it by 2
                rv = 1 + steps(n // 2)
            else:
                rv = 1 + min(steps(n + 1), steps(n - 1))
            memo[n] = rv
            return rv
        

        return steps(n)


# BFS. Too slow.
class Solution2(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        # BFS
        if n == 1:
            return 0
        visited = {0, 1}
        current_numbers = [1]
        next_numbers = []
        next_distance = 1
        while True:
            for x in current_numbers:
                candidates = (x-1, x+1, 2*x)
                for c in candidates:
                    if c in visited:
                        continue
                    if c == n:
                        return next_distance
                    visited.add(c)
                    next_numbers.append(c)
            current_numbers, next_numbers = next_numbers, []
            next_distance += 1



def test():
    assert Solution().integerReplacement(8) == 3
    assert Solution().integerReplacement(15) == 5
    assert Solution().integerReplacement(1) == 0
    assert Solution().integerReplacement(1234) == 14
    assert Solution().integerReplacement(100) == 8
