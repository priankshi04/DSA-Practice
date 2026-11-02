class Solution:
    def getNthPentagonalNum(self, n):
        # code here
        # BRUTE FORCE APPROACH
        if n==1:
            return 1
        res=1
        diff=4
        for i in range(2,n+1):
            res=res+diff
            diff=diff+3
        return res
        # OPTIMAL APPROACH
        return (n * (3 * n - 1)) // 2