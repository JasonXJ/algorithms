class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0
        prices.append(-1)
        buy_price = None
        for i in range(len(prices) - 1):
            if buy_price is None:  # Need to buy
                if prices[i+1] > prices[i]:
                    buy_price = prices[i]
            else:  # Need to sell
                if prices[i+1] < prices[i]:
                    max_profit += prices[i] - buy_price
                    buy_price = None

        return max_profit
