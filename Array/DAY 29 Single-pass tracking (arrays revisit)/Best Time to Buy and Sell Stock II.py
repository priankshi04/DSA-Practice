class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(1, len(prices)):  # we can see that the first buy is the lowest one
            if prices[i] > prices[i - 1]:  # if price is greater than the previous stock
                profit += prices[i] - prices[i - 1]  # store the profit
        return profit
