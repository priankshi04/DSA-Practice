class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        hashmap = {}  # created a hashmap with all the values in the array
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        answer = []  # empty array
        for i in range(1, n + 1):  # taken upto the length of array
            if i not in hashmap:  # if the no not present in the hashmap
                answer.append(i)
        return answer
