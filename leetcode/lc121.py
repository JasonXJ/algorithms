class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0

        lowest = prices[0]
        max_profit = 0
        for x in prices[1:]:
            if x < lowest:
                lowest = x
            else:
                profit = x - lowest
                if profit > max_profit:
                    max_profit = profit

        return max_profit
