class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        total =0
        for i in range(k):
            total+=nums[i] # to add upto before the k value 

        maxSum=total
        for i in range(k,len(nums)): #to slide the window
            total = total - nums[i-k]+nums[i] # to remove the first elemnt, and add the new one
            if total>maxSum:
                maxSum=total
        return maxSum/float(k)
        
