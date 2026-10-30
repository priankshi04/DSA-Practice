class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums)==0:
            return 0 # if an empty list
        slow=0
        fast=0 
        while slow<len(nums):
            if nums[slow]!=0:# to replace the non zero element with the zero ones
                temp=nums[slow]
                nums[slow]=nums[fast]
                nums[fast]=temp
                fast+=1
            slow+=1
        
        
