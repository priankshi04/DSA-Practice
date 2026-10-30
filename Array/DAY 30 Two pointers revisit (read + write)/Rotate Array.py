class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k % n #gives remainder as k to get how many numbers need to go forward after that no
        start=0
        end=n-1
        # reverse entire array
        while start<end:
            nums[start], nums[end]=nums[end], nums[start]
            start+=1
            end-=1
        start=0
        end=k-1
        #reverse upto k elements
        while start<end:
            nums[start], nums[end]=nums[end], nums[start]
            start+=1
            end-=1
        start = k
        end = n-1
        #reverse remaining elements
        while start<end:
            nums[start], nums[end]=nums[end], nums[start]
            start+=1
            end-=1
        """
        BRUTE FORCE 
        n=len(nums)
        k=k % n
        for i in range(k):# loops runs k times
            last=nums[n-1]# to get the last no
            for j in range(n-1,0,-1):
                nums[j]=nums[j-1]# to trace from reverse
            nums[0]=last # to get the last element to the first
        """