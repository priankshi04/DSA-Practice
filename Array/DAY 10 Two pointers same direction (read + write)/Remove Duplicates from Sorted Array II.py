class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0 # if an empty list
        slow=2 # same as before just the max repeat is 2 so, upto index 1 all element will either be unique or  atmost repeat twice
        fast=2
        while slow<len(nums):
            if nums[slow]!=nums[fast-2]:#track the place of last unique element
                nums[fast]=nums[slow] #scans ahead
                fast+=1
            slow+=1
        return fast