class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        mid= n #mid value
        k=[] # empty list to store x values
        l=[] # empty list to store y values
        ans=[] # empty list to return final ans
        for i in range(0,mid): # to take upto before mid value for k
            k+=[nums[i]] # adding element
        for j in range(mid,len(nums)): #to take from mid value to last for l
            l+=[nums[j]] # adding element
        for a in range(n):# To access each element from both the list as the size is of n  to append to final list
            ans+=[k[a]] # first appending x value
            ans+=[l[a]] # next appending y values
        return ans # to return final answer