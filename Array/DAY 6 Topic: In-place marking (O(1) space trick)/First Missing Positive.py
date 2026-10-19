class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)  # to change all the values to positive
        hashmap = {}
        for i in nums:
            hashmap[i] = 1
        for i in range(1,
                       n + 2):  # as we need to find the positive no so 1 to range upto check the missing value as n+1 would check upto the given array and not the next element if that is the element which is missing
            if i not in hashmap:  # to check if each key is present
                return i
