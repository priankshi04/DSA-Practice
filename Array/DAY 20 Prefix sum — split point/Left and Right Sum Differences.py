class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        leftSum= 0
        rightSum = 0
        p=[]
        q=[]
        r=[]
        answer=[]
        for i in range(0,len(nums)):# used to store from the addition of 0 to second last element
            p+=[leftSum]
            leftSum+=nums[i]

        for j in range(len(nums)-1,-1,-1): # used to access from the last element till second element to store in q
            q+=[rightSum]
            rightSum+=nums[j]

        for l in range(len(q)-1,-1,-1):# to reverse the q list
            r+=[q[l]]

        for k in range(len(nums)):# to return the final answer
            answer+= [abs(p[k] - r[k])]
        return answer
"""
        total = 0  # using prefix sum approach
        for i in range(len(nums)):
            total += nums[i]
        left = 0
        ans = [0] * len(nums)
        for i in range(len(nums)):
            right = total - left - nums[i]  # to get the right sum
            diff = left - right  # to get the diff

            if diff < 0:
                diff = -diff
            ans[i] = diff
            left += nums[i]
        return ans
