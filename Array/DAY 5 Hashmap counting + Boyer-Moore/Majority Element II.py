class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hashmap = {}  # creating a dict
        answer = []  # creating a empty list
        for i in nums:  # to trverse each element
            if i in hashmap:  # if it is already in hashmap
                hashmap[i] += 1  # increment the value
            else:
                hashmap[i] = 1  # create the key and put value as 1
        for i in hashmap:  # to traverse each element in hashmap
            if hashmap[i] > len(nums) // 3:  # if the repition of the elements are greater than [n/3] times
                answer += [i]  # insert that element into answer list
        return answer  # return the list
