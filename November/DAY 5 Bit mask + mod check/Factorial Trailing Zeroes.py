class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # BRUTE FORCE APPROACH
        if n == 0 : # BASE CASE
            return 0
        fact=1
        for i in range(1,n+1):
            fact= fact*i # RECURSIVE CASE TO GET THE FACTORIAL
        count=0
        while fact%10 == 0 and fact>0: # TO COUNT THE NO OF ZEROS
            count+=1
            fact = fact//10
        return count
        #TC:O(N) , O(LOG(N!)(base 10))
        #SC:O(nlogn)
        # OPTIMAL AAPROACH

        count = 0
        while n >= 5:  # as 5 factorial produces 1 zeros , so at dividing the no with 5 will result in the no of zeros upto 5 factorial , and the remainder will be below 5
            n = n // 5
            count += n
        return count
        #TC: O(logn(base5))
        #SC: O(1)