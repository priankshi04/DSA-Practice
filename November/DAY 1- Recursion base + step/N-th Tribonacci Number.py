class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        #BRUTE FORCE APPROACH
        if n==0:
            return 0
        if n==1  or n==2:
            return 1
        return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
        """
        #TC:O(3^N)
        #SC:O(N)
        #OPTIMAL APPROACH
        if n==0:
            return 0
        if n==1  or n==2:
            return 1
        a=0
        b=1
        c=1
        for i in range(3,n+1):
            d=a+b+c
            a=b
            b=c
            c=d
        return c
        #TC: O(N)
        #SC: O(1)