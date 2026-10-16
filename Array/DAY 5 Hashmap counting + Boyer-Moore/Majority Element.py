class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashmap={}
        for i in nums:
                if i in hashmap:
                    hashmap[i]+=1 # to add the no of value the given element is repeating 
                else:
                    hashmap[i]=1 # to add the value to the dictionary
            
        for i in hashmap:
                if hashmap[i]>len(nums)//2: # to check if the given element repition is greater than the length of the num
                    return i
