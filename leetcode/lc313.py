from heapq import heappush, heappop


# An O(kn) solution. Note that the complexity analysis will require aggregation
# analysis. Also see
# https://discuss.leetcode.com/topic/34841/java-three-methods-23ms-36-ms-58ms-with-heap-performance-explained
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        # ``uglies[i]`` will store the i + 1 smallest ugly number
        INF = float('+inf')
        uglies = [0] * n
        uglies[0] = 1
        # ``indexes[i]`` is an index of uglies, such that uglies[indexes[i]] *
        # primes[i] might be the next ugly number.
        indexes = [0] * len(primes)
        # This stores the possibly next ugly number. That is,
        # ``next_uglies_candidates[i] == uglies[indexes[i]] * primes[i]``
        next_uglies_candidates = primes[:]
        for i in range(1, n):
            x = uglies[i] = min(next_uglies_candidates)
            # Update `indexes` and `next_uglies_candidates`
            for j, p in enumerate(primes):
                if next_uglies_candidates[j] == x:
                    indexes[j] += 1
                    next_uglies_candidates[j] = uglies[indexes[j]] * p

        return uglies[-1]


def test():
    primes1 = [2, 7, 13, 19]
    results1 = [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32]
    for n, expected_rv in enumerate(results1, 1):
        assert Solution().nthSuperUglyNumber(n, primes1) == expected_rv


if __name__ == "__main__":
    import timeit
    n = 100000
    primes = [7,19,29,37,41,47,53,59,61,79,83,89,101,103,109,127,131,137,139,157,167,179,181,199,211,229,233,239,241,251]
    print(timeit.timeit('Solution().nthSuperUglyNumber(n, primes)', globals=globals(), number=5))
