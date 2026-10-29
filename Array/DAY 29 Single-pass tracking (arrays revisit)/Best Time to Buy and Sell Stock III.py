class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # should be atmost two transaction
        buy1=float("inf") # store infinite values
        buy2=float("inf")
        profit1=0
        profit2=0
        for price in prices: # for each price
            if price < buy1: # if it is less than buy , then buy should store the price value
                buy1=price
            if price-buy1>profit1:# to store the max profit for first buy and sell
                profit1=price-buy1
            if price-profit1<buy2: # to  get the second  buy
                buy2=price-profit1
            if price-buy2>profit2:# to store the max total profit upto second buy
                profit2=price-buy2 #combined profit of both transaction
        return profit2