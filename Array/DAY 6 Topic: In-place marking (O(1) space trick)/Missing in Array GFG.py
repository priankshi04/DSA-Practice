class Solution:
    def missingNum(self, arr):
        # code here
        hashmap={}
        n=len(arr)
        for i in arr:
            hashmap[i]=1
        for i in range(1,n+2):
            if i not in hashmap:
                return i