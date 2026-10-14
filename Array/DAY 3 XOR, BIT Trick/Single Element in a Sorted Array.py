class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer = 0  # same as single number , used XOR trick
        for i in nums:
            answer = answer ^ i
        return answer
