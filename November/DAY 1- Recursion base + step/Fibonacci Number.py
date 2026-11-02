class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        # brute force approach 
        if n== 0:
            return 0 # base case
        if n == 1:
            return 1 # base case
        return self.fib(n-1)+ self.fib(n-2) # recursive case
        #TC: O(2^n)
        #SC:O(n)
      
        # optimal approach 
        if n<=1:
            return n
        a=0
        b=1
        for i in range(2,n+1): # recursive case 
            c =a+b
            a=b
            b=c
        return b
        #TC:O(n)
        #SC:O(1)
