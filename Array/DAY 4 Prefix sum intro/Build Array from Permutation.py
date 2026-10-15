class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []  # empty list
        for i in range(0, len(nums)):  # to traverse each element
            ans += [nums[nums[i]]]  # to append each element
        return ans  # to return the result
