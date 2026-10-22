class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total =0
        for i in range(len(nums)):
            total+=nums[i] # add all the numbers

        left=0 # sum from the left side side of the array
        for i in range(len(nums)):
            right=total-left-nums[i] # to get the right sum by subtracting the total from the left sum and the left elements of the array *THE VALUE IS NOT STORED IN RIGHT ONLY FOR COMPARISON*

            if left==right: # to check the left sum and right sum
                return i
            left+=nums[i] # to add the value from the left side of the array
        return -1
