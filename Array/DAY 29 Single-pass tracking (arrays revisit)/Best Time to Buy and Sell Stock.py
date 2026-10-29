class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice=prices[0]# take the first element
        maxProfit=0 #initialize
        for i in range(1,len(prices)): #from the next element
            if prices[i]<minPrice:
                minPrice= prices[i]# to get the minimum price
            else:
                profit =prices[i]-minPrice #to store the diff of each stocks
                if profit> maxProfit: # is if the profit is greater than maxProfit, it stores it
                    maxProfit = profit
        return maxProfit
