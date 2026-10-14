class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        # using Hahmap
        hashmap = {}
        for i in nums :
            if i in hashmap:
                hashmap[i]+=1 #if already present it would increment the value 
                
            else:
                hashmap[i]=1 # to create a key value pair with value = 1
        for key,value in hashmap.items():# to check in the dictonary if the value is 1 or not
            if value ==1: #where value=1
                return key #to return the key 
        """
        answer = 0 #initializing a variable
        for i in nums : # to traverse each element
            answer = answer^i # to increment the value using XOR approach where if the no is repeated it gets decreased from incremented value 
        return answer # single number is obtained
