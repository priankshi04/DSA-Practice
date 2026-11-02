class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        BRUTE
        FORCE
        APPROACH
        if n == 0:
            return 0
        if n == 1 or n == 2 or n == 3:
            return n
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
        #TC: O(2 ^ n)
        #SC: O(n)
        """
        #OPTIMAL APPROACH
        if n == 0:
            return 0
        if n == 1 or n == 2 or n == 3:
            return n
        a = 2
        b = 3
        for i in range(4, n + 1):
            c = a + b
            a = b
            b = c
        return b
        #TC: O(n)
        #SC: O(1)
