class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        
        #BRUTE FORCE 
        if n <=0:
            return False
        while n%2==0:
            n=n//2
        return n==1
        TC:O(log n)
        SC:O(1)
        """
        #optimal Approach 
        return n>0 and(n&(n-1))==0
        TC:O(1)
        SC:O(1)
