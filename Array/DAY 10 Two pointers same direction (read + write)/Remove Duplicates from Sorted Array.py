class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        if len(nums)==0:
            return 0 # if an empty list
        slow=1
        fast=1 
        while slow<len(nums):
            if nums[slow]!=nums[fast-1]:#track the place of last unique element
                nums[fast]=nums[slow] #scans ahead 
                fast+=1
            slow+=1
        return fast
        
