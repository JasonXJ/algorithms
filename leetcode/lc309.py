from collections import deque

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0

        # DP solution. DP[i] is the maximum profit we can make if only
        # prices[:i+1] is considered. So, we can generate DP[i] from the
        # previous maximum proft: if we do not make any transaction at day i,
        # then DP[i] = DP[i-1]; otherwise, we sell a stock brought on day j at
        # day i (note that we can easily prove that we should never buy a stock
        # at the last day), so DP[i] = DP[j - 2] + prices[i] - prices[j].
        # Therefore, DP[i] = max(DP[i-1], max_{j<=i-1}(DP[j-2] + prices[i] -
        # prices[j])). Note that we can simplify the second "max": max(DP[j-2]
        # + prices[i] - prices[j]) == max(DP[j-2] -prices[j]) + prices[i]. Note
        # that this simplification is important because there is no "i" inside
        # the "max", so we can use a variable to track the maximum (DP[j-2] -
        # prices[j]) so far, which give us an O(n) time and O(1) space
        # algorithm.

        last_three_dp = deque(maxlen=3)
        last_three_dp.append(0)
        # `alpha` is the "max_{j<=i-1}(DP[j-2] - prices[j])" so far. Initalize
        # it to `-prices[0]` ensure the correctness.
        alpha = -prices[0]
        for i in range(1, len(prices)):
            # Try to update `max_candidate`.
            alpha = max(alpha, last_three_dp[0] - prices[i-1])
            last_three_dp.append(max(last_three_dp[-1], alpha + prices[i]))

        return last_three_dp[-1]


def test():
    assert Solution().maxProfit([1, 2, 3, 0, 2]) == 3
