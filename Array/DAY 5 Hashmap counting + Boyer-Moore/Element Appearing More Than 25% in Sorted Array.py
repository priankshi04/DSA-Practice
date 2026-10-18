class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        hashmap={}#same as other Hashmap counting + Boyer-Moore method
        for i in arr:
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i]=1
        for i in hashmap:
            if hashmap[i]>len(arr)*0.25: #Element Appearing More Than 25% in Sorted Array
                return i
