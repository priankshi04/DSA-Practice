class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        slow = 0
        fast = len(nums) - 1
        answer = [0] * len(nums)
        wr = len(nums) - 1
        while slow <= fast:
            if abs(nums[slow]) > abs(nums[fast]):  # to check if the last no is less than the first no
                answer[wr] = nums[slow] * nums[
                    slow]  # the index wr is at the last so it squares and put the largest no at last
                slow += 1
            else:
                answer[wr] = nums[fast] * nums[fast]
                fast -= 1
            wr -= 1  # decrement of the index

        return answer
