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
                USED XOR Approach :
                answer = len(nums) # to take the length of the list
                for i in range(len(nums)): # to traverse each element
                    answer = answer^i^nums[i] # using XOR operation
                return answer
                """
        # used Hahmap approach 
        n = len(nums)
        hashmap = {}
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        for i in range(0, n + 1):  # to take range upto 4 values as 0-3 , has 4 values
            if i not in hashmap:  # to check if each key is present
                return i