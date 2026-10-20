class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        slow = 0
        fast = 1
        while slow < len(nums) and fast < len(nums):
            if nums[slow] % 2 == 0:  # to see if the even index has even no
                slow += 2
            elif nums[fast] % 2 != 0:  # to check if the odd index has odd no
                fast -= 2
            else:  # if not swap them
                temp = nums[slow]
                nums[slow] = nums[fast]
                nums[fast] = temp

        return nums