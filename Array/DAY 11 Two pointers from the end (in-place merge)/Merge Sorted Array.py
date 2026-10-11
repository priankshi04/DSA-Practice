class Solution:
    # brute force approach as first i can join both of the list and then perform normal sort , the time complexity here is O(m+n)^2
    """def merge(self, nums1, m, nums2, n):
        for i in range(n):
            nums1[m+i]= nums2[i]
        for i in range(1,m+n):
            for j in range(i+1,m+n):
                if nums1[i]>nums1[j]:
                    temp=nums1[i]
                    nums1[i]=nums1[j]
                    nums1[j]=temp
        return nums1"""
# here unsorted array wont work so we need to use optimal approach 
    def merge(self, nums1, m, nums2, n):
        k = m+n-1 #3rd pointer , m , n 1st and 2nd
        # merging in reverse order
        while m>0 and n>0:
            if nums1[m-1]>nums2[n-1]:# otherwise index out of range as indexing starts with 0
                nums1[k]=nums1[m-1]
                m-=1 # updation of pointers
            else:
                nums1[k]= nums2[n-1]
                n-=1
            k-=1# need to decrease it regardless of comparison
        # filling nums1 with remaining values in nums2 
        while n>0:
            nums1[k]=nums2[n-1]
            n-=1
            k-=1
        return nums1
