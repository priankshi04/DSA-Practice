class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        n = len(prices)
        answer = [0] * n
        for i in range(n):
            discount = False

            for j in range(i + 1, n):  # checks with the elements to the right
                if prices[j] <= prices[i]:  # if the prices is less than the price
                    answer[i] = prices[i] - prices[j]  # discount is applied to the element
                    discount = True
                    break
            if discount == False:  # if not discount is applied
                answer[i] = prices[i]
        return answer
