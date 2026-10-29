class Solution:
    def maxSubArray(self, nums):
        """
        #brute force approach
        max_sum=nums[0]
        for i in range(0,len(nums)):
            currentSum=0
            for j in range(i,len(nums)):
                currentSum+=nums[j]
                if currentSum>max_sum:
                    max_sum=currentSum
        return max_sum
        """
        # KADANE ALGORITHM
        currentSum = nums[0]
        maxSum = nums[0]
        for i in range(1, len(nums)):
            if currentSum + nums[i] < nums[i]:
                currentSum = nums[i]
            else:
                currentSum += nums[i]
            if currentSum > maxSum:
                maxSum = currentSum
        return maxSum
