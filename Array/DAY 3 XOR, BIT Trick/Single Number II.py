class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one = 0
        two = 0
        for i in nums:
            one = (one ^ i) & ~two # 0 XOR 2= 2 and -0 = 2 , similary the increment occurs and result in final value
            two = (two ^ i) & ~one # now 0 xor 2 = 2 and -2 = 0
        return one