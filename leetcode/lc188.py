class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k <= 0 or len(prices) <= 1:
            return 0

        # There is at most ``len(prices)//2`` ascending slope. This is for
        # defeating large k attack.
        if k >= len(prices)//2:
            rv = 0
            for i in range(1, len(prices)):
                different = prices[i] - prices[i-1]
                if different > 0:
                    rv += different
            return rv

        # ``profit[i][t]`` is the max profit if `i` transactions are made for
        # ``prices[:t+1]``. Note that since the first row and the first column
        # should be zero, so they are already set to proper values.
        profit = [[0]*len(prices) for _ in range(k+1)]

        # profit[i][t] = max(profit[i][t-1],
        #                    max(prices[t] - prices[tt] + profit[i-1][tt-1]
        #                        for tt in range(t))
        #                   )
        #              = max(profit[i][t-1],
        #                    prices[t] + max(profit[i-1][tt-1] - prices[tt]
        #                                    for tt in range(t))
        #                   )
        for i in range(1, k + 1):
            local_max = -prices[0]
            for t in range(1, len(prices)):
                profit[i][t] = max(
                    profit[i][t-1],
                    prices[t] + local_max
                )
                local_max = max(local_max, profit[i-1][t-1] - prices[t])

        return profit[k][len(prices)-1]
