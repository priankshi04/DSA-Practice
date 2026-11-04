class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #BRUTE FORCE
        if n <=0:
            return False
        while n%3==0:
            n=n//3
        return n==1
        TC: O(log3n)
        sc:O(1)
        
        # OPTIMAL APPROACH
        return n > 0 and 1162261467 % n == 0  # Checks whether n divides the largest 32-bit power of three
        TC: O(1)
        SC: 0(1)
