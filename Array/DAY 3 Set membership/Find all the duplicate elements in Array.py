class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        k=[0]*len(nums) #use this to make the list of nums value to store the elements
        count = 0 # to traverse the position
        for i in range (len(nums)): # to view each element
            num = abs (nums[i])
            index = num-1
            if nums[index]<0:
                k[count]=num
                count+=1
            else:
                nums[index]= - nums[index]
        return k[:count]    