# An O(n) solution
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices) <= 1:
            return 0

        # ``from_left[i]`` is the highest profit of a *single* transaction when
        # ``prices[:i]`` is considered.
        #
        # ``from_right[i]`` is the highest profit of a *single* transaction when
        # ``prices[i:]`` is considered.
        from_left = [0] * len(prices)
        from_right = [0] * len(prices)

        # Fill `from_left`. Note that ``i == 0`` is skiped (so ``from_left[0]
        # == from_left[1] == 0``). Also, ``i == len(prices) - 1`` is skipped.
        # That is because this would be the trivial case when we only consider
        # have one transaction, and this trivial case is actually already
        # covered by ``from_left[0]`` and ``from_right[0]``.
        min_price = prices[0]
        for i in range(1, len(prices)-1):
            from_left[i+1] = max(prices[i] - min_price, from_left[i])
            if prices[i] < min_price:
                min_price = prices[i]

        # Fill `from_right`. Note that ``i == len(min_price) - 1`` is skipped
        # (so ``from_left[L-1] == 0``).
        max_price = prices[-1]
        for i in range(len(prices)-2, -1, -1):
            from_right[i] = max(max_price - prices[i], from_right[i+1])
            if prices[i] > max_price:
                max_price = prices[i]

        # Return the max profit
        return max(from_left[i] + from_right[i] for i in range(len(prices)))

if __name__ == "__main__":
    f = Solution().maxProfit
    assert f([1,5]) == 4
    assert f([5,1]) == 0
    assert f([]) == 0
    assert f([10]) == 0
    assert f([1,3,2,4,0,6]) == 9
