class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i in range(len(nums)):
            need = target - nums[i]
            if need in hashmap:
                return [hashmap[need], i]
            else:
                hashmap[nums[i]] = i

