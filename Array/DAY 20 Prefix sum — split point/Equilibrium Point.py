class Solution:
    def findEquilibrium(self, arr):
        # code here
        total=0
        for i in range(len(arr)):
            total+=arr[i]
        left=0
        for i in range(len(arr)):
            right=total-left-arr[i]
            if left==right:
                return i
            left+=arr[i]
        return -1
