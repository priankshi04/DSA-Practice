class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        # using another variant
        answer = len(nums)
        for i in range(len(nums)):
            answer = answer ^ i
        for i in nums:
            answer = answer ^ i
        return answer
        """
        answer = len(nums) # to take the length of the list
        for i in range(len(nums)): # to traverse each element
            answer = answer^i^nums[i] # using XOR operation
        return answer
