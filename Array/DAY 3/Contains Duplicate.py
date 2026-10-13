class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        # using brute force , but it result in TLE
        slow = 0
        fast = len(nums)-1

        if len(nums) == 0 and 1:
            return False
        for slow in range(0, len(nums)-1):
            for fast in range(slow+1, len(nums)):
                if nums[slow]==nums[fast]:
                    return True
                
                
        return False
        # USING TWO POINTER Approach , still result in TLE
        slow = 0
        fast = 1
        while slow<len(nums)-1:
            if nums[slow]== nums[fast]:
                return True
            fast+=1
            if fast==len(nums):
                slow+=1
                fast= slow+1
        return False
        """
        seen = set() # used set
        for num in nums: # to get each element from the list
            if num in seen: # to check if the element is already in the list
                return True
            seen.add(num) # else need to add that number in the seen
        return False


                
