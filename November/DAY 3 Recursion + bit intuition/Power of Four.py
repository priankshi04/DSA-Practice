class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False
        while n%4==0:
            n=n//4
        return n==1
        #TC: O(log4n)
        #SC:O(1)
        
        return (n > 0 and (n & (n - 1)) == 0 and (n & 1431655765) != 0)
    
