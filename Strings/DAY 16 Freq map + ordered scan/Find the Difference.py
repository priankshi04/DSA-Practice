class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        hashmap1={}
        for i in s:
            if i in hashmap1:
                hashmap1[i]+=1
            else:
                hashmap1[i]=1 # to take the frequency count of shorter string
        for ch in t: # taking range of longer string
            if ch not in hashmap1 or hashmap1[ch]==0: #comparing each char which is not present
                return ch # to return that char
            else:
                hashmap1[ch]-=1