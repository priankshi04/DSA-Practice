#Back-end complete function Template for Python 3

class Solution:
    def minCostClimbingStairs(self, cost):
        #Write your code here
        """n=len(cost)
        def solve(i):
            if i>=n:
                return 0
            one=solve(i+1)
            two=solve(i+2)
            return cost[i] + min(one, two)
        return min(solve(0), solve(1))
#tc:O(2^n)
#sc:O(n)"""
        n = len(cost)
        a=0
        b=0
        for i in range(n-1,-1,-1):
            c=cost[i]+ min(a,b)
            b=a
            a=c
        return min(a,b)
#tc:O(n)
#sc:O(1)