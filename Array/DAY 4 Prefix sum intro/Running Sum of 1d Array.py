class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer=0
        p=[] # to return another list
        for i in range(len(nums)): # to access each element
            answer+=nums[i] # for each elemnet add up with the next
            p+=[answer] # add the value to the list p
        return p # return the list 
