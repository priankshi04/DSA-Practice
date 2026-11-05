class Solution(object):
    def sumBase(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        #BRUTE FORCE APPROACH
        dig=""
        while n>0:
            rem=n%k
            dig=str(rem) + dig
            n=n//k
        total=0
        for i in dig:
            total+=int(i)
        return total
        #TC:O(LOGkn)
        #SC:O(LOGkn)

        # OPTIMAL APPROACH
        total = 0
        while n > 0:
            rem = n % k
            total += rem
            n = n // k
        return total
        #TC: O(LOGkn)
        #SC: O(1)
