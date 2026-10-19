class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = []
        n = len(nums)
        hashmap = {}
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        for i in hashmap:  # to check which element is duplicated
            if hashmap[i] > 1:
                answer += [i]
        for i in range(1, n + 1):
            if i not in hashmap:  # to check which element is missing
                answer += [i]
        return answer

