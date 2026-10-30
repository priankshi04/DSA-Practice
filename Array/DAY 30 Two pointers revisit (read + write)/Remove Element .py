class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        read=0
        write=0
        while read<len(nums):
            if nums[read]!=val:# use of two pointers in same direction and check only for that value
                nums[write]= nums[read]
                write+=1
            read+=1
        return write
        
