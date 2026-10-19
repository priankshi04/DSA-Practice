class Solution:
    def majorityElement(self, arr):
        # code here
        hashmap = {}
        for i in arr:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        for i in hashmap:
            if hashmap[i] > len(arr) // 2:
                return i

        return -1 # to return -1 if no value is repeated than the half of length of array