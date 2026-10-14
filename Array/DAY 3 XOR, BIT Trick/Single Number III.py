class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = 0
        for i in nums:
            answer = answer^i
        diff = answer & -answer # here it is negative value of answer that is 2's complement
        # teo get two numbers need to create two variables:
        num1 = 0
        num2 = 0
        for i in nums:
            if i & diff: # using AND operator
                num1 = num1^i # using XOR operator
            else:
                num2 = num2^i
        return [num1, num2]