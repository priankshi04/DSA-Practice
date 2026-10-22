class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hashmap = {0: 1}
        total = 0
        count = 0
        for i in range(len(nums)):
            total += nums[i]
            needed = total - k
            if needed in hashmap:
                count += hashmap[needed]
            if total in hashmap:
                hashmap[total] += 1
            else:
                hashmap[total] = 1
        return count
