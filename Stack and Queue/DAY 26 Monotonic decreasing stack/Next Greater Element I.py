class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n=len(nums2)
        m=len(nums1)
        ans=[-1]*m
        stack=[0]*n
        top=-1
        for i in range(m):
            for j in range(n):
                if nums1[i]==nums2[j]:#to find the same no in nums2 if found
                    for k in range(j+1,n): #check its right value , if greater than the no , store it and stop the code
                        if nums2[k]>nums2[j]:
                            ans[i]=nums2[k]
                            break
                    break #else return -1
        return ans
