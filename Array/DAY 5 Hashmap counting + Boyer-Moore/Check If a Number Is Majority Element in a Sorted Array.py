class Solutions:
    def majorityElement(self,nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hashmap={}
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        for i in hashmap:
            if hashmap[i] > len(nums) // 2:
                return i
