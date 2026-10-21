class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
    # USING BRUTE FORCE 
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]==nums[j] and abs(i-j)<=k:
                    return True
                
        return False
        """
        hashmap={} 

        for i in range(len(nums)): # to get each element
            if nums[i] in hashmap: # if the lement is already present in hashmap
                if abs(i-hashmap[nums[i]]) <=k: # check if the index value is greater or equal to the k value
                    return True
            hashmap[nums[i]]= i # else put the nums [i] as key in hashmap using the index as value
        return False
