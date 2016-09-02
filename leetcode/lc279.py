class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if int(n**0.5)**2 == n:
            return 1
        visited = [False] * n
        seeds = [i*i for i in range(1, int(n**0.5) + 1)]
        for x in seeds:
            visited[x] = True
        current_level = 1
        current_level_indexes = seeds
        while True:
            next_level_indexes = []
            for i in current_level_indexes:
                for s in seeds:
                    ii = i + s
                    if ii == n:
                        return current_level + 1
                    if ii < n and not visited[ii]:
                        visited[ii] = True
                        next_level_indexes.append(ii)
                current_level_indexes = next_level_indexes
            current_level += 1


if __name__ == "__main__":
    import timeit
    assert Solution().numSquares(1834) == 3
    assert Solution().numSquares(12) == 3
    assert Solution().numSquares(13) == 2
    assert Solution().numSquares(1) == 1
    assert Solution().numSquares(16) == 1
    # print(timeit.timeit('Solution().numSquares(1834)', globals=globals(), number=100))
    # print(timeit.timeit('OldSolution().numSquares(1834)', globals=globals(), number=100))
