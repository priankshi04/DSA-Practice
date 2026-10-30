class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        slow=0
        fast=len(nums)-1
        while slow<fast:
            if nums[slow]%2==0:# if divisible by 2 keep at front
                slow+=1 # increment the pointer
            elif nums[fast]%2!=0: # if not divisible by 2 keep at back
                fast-=1 # decrement the pointer
            else:# otherwise swap the first and last elements 
                temp=nums[slow]
                nums[slow]=nums[fast]
                nums[fast]=temp
                fast-=1
                slow+=1
        return nums
