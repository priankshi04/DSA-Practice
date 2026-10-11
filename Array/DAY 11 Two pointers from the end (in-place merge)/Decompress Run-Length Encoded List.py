class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        size = 0
        for i in range(0, len(nums), 2):
            size += nums[i]

        answer = [0] * size
        k = 0
        for i in range(0, len(nums), 2):
            freq = nums[i]
            val = nums[i + 1]
            for j in range(freq):
                answer[k] = val
                k += 1
        return answer
